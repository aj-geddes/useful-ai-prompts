---
name: ML Pipeline Automation
description: Build end-to-end ML pipelines with automated data processing, training, validation, and deployment using Airflow, Kubeflow, and Jenkins
---

# ML Pipeline Automation

ML pipeline automation orchestrates the entire machine learning workflow from data ingestion through model deployment, ensuring reproducibility, scalability, and reliability.

## Pipeline Components

- **Data Ingestion**: Collecting data from multiple sources
- **Data Processing**: Cleaning, transformation, feature engineering
- **Model Training**: Training and hyperparameter tuning
- **Validation**: Cross-validation and testing
- **Deployment**: Moving models to production
- **Monitoring**: Tracking performance metrics

## Orchestration Platforms

- **Apache Airflow**: Workflow scheduling with DAGs
- **Kubeflow**: Kubernetes-native ML workflows
- **Jenkins**: CI/CD for ML pipelines
- **Prefect**: Modern data flow orchestration
- **Dagster**: Asset-driven orchestration

## Python Implementation

```python
import pandas as pd
import numpy as np
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score
import joblib
import logging
from datetime import datetime
import json
import os

# Airflow imports
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

# MLflow for tracking
import mlflow
import mlflow.sklearn

# Logging setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

print("=== 1. Modular Pipeline Functions ===")

# Data ingestion
def ingest_data(**context):
    """Ingest and load data"""
    logger.info("Starting data ingestion...")

    X, y = make_classification(n_samples=2000, n_features=30,
                              n_informative=20, random_state=42)
    data = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(X.shape[1])])
    data['target'] = y

    # Save to disk
    data_path = '/tmp/raw_data.csv'
    data.to_csv(data_path, index=False)

    context['task_instance'].xcom_push(key='data_path', value=data_path)
    logger.info(f"Data ingested: {len(data)} rows")
    return {'status': 'success', 'samples': len(data)}

# Data processing
def process_data(**context):
    """Clean and preprocess data"""
    logger.info("Starting data processing...")

    # Get data path from previous task
    task_instance = context['task_instance']
    data_path = task_instance.xcom_pull(key='data_path', task_ids='ingest_data')

    data = pd.read_csv(data_path)

    # Handle missing values
    data = data.fillna(data.mean())

    # Remove duplicates
    data = data.drop_duplicates()

    # Remove outliers (simple approach)
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        Q1 = data[col].quantile(0.25)
        Q3 = data[col].quantile(0.75)
        IQR = Q3 - Q1
        data = data[(data[col] >= Q1 - 1.5 * IQR) & (data[col] <= Q3 + 1.5 * IQR)]

    processed_path = '/tmp/processed_data.csv'
    data.to_csv(processed_path, index=False)

    task_instance.xcom_push(key='processed_path', value=processed_path)
    logger.info(f"Data processed: {len(data)} rows after cleaning")
    return {'status': 'success', 'rows_remaining': len(data)}

# Feature engineering
def engineer_features(**context):
    """Create new features"""
    logger.info("Starting feature engineering...")

    task_instance = context['task_instance']
    processed_path = task_instance.xcom_pull(key='processed_path', task_ids='process_data')

    data = pd.read_csv(processed_path)

    # Create interaction features
    feature_cols = [col for col in data.columns if col.startswith('feature_')]
    for i in range(min(5, len(feature_cols))):
        for j in range(i+1, min(6, len(feature_cols))):
            data[f'interaction_{i}_{j}'] = data[feature_cols[i]] * data[feature_cols[j]]

    # Create polynomial features
    for col in feature_cols[:5]:
        data[f'{col}_squared'] = data[col] ** 2

    engineered_path = '/tmp/engineered_data.csv'
    data.to_csv(engineered_path, index=False)

    task_instance.xcom_push(key='engineered_path', value=engineered_path)
    logger.info(f"Features engineered: {len(data.columns)} total features")
    return {'status': 'success', 'features': len(data.columns)}

# Train model
def train_model(**context):
    """Train ML model"""
    logger.info("Starting model training...")

    task_instance = context['task_instance']
    engineered_path = task_instance.xcom_pull(key='engineered_path', task_ids='engineer_features')

    data = pd.read_csv(engineered_path)

    X = data.drop('target', axis=1)
    y = data['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train model
    model = RandomForestClassifier(n_estimators=100, max_depth=15, random_state=42)
    model.fit(X_train_scaled, y_train)

    # Evaluate
    y_pred = model.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    # Save model
    model_path = '/tmp/model.pkl'
    scaler_path = '/tmp/scaler.pkl'
    joblib.dump(model, model_path)
    joblib.dump(scaler, scaler_path)

    task_instance.xcom_push(key='model_path', value=model_path)
    task_instance.xcom_push(key='scaler_path', value=scaler_path)

    # Log to MLflow
    with mlflow.start_run():
        mlflow.log_param('n_estimators', 100)
        mlflow.log_param('max_depth', 15)
        mlflow.log_metric('accuracy', accuracy)
        mlflow.log_metric('f1_score', f1)
        mlflow.sklearn.log_model(model, 'model')

    logger.info(f"Model trained: Accuracy={accuracy:.4f}, F1={f1:.4f}")
    return {'status': 'success', 'accuracy': accuracy, 'f1_score': f1}

# Validate model
def validate_model(**context):
    """Validate model performance"""
    logger.info("Starting model validation...")

    task_instance = context['task_instance']
    model_path = task_instance.xcom_pull(key='model_path', task_ids='train_model')
    engineered_path = task_instance.xcom_pull(key='engineered_path', task_ids='engineer_features')

    model = joblib.load(model_path)
    data = pd.read_csv(engineered_path)

    X = data.drop('target', axis=1)
    y = data['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    scaler_path = task_instance.xcom_pull(key='scaler_path', task_ids='train_model')
    scaler = joblib.load(scaler_path)
    X_test_scaled = scaler.transform(X_test)

    # Validate
    y_pred = model.predict(X_test_scaled)
    accuracy = accuracy_score(y_test, y_pred)

    validation_result = {
        'status': 'success' if accuracy > 0.85 else 'failed',
        'accuracy': accuracy,
        'threshold': 0.85,
        'timestamp': datetime.now().isoformat()
    }

    task_instance.xcom_push(key='validation_result', value=json.dumps(validation_result))

    logger.info(f"Validation result: {validation_result}")
    return validation_result

# Deploy model
def deploy_model(**context):
    """Deploy validated model"""
    logger.info("Starting model deployment...")

    task_instance = context['task_instance']
    validation_result = json.loads(task_instance.xcom_pull(
        key='validation_result', task_ids='validate_model'))

    if validation_result['status'] != 'success':
        logger.warning("Validation failed, deployment skipped")
        return {'status': 'skipped', 'reason': 'validation_failed'}

    model_path = task_instance.xcom_pull(key='model_path', task_ids='train_model')
    scaler_path = task_instance.xcom_pull(key='scaler_path', task_ids='train_model')

    # Simulate deployment
    deploy_path = '/tmp/deployed_model/'
    os.makedirs(deploy_path, exist_ok=True)

    import shutil
    shutil.copy(model_path, os.path.join(deploy_path, 'model.pkl'))
    shutil.copy(scaler_path, os.path.join(deploy_path, 'scaler.pkl'))

    logger.info(f"Model deployed to {deploy_path}")
    return {'status': 'success', 'deploy_path': deploy_path}

# 2. Airflow DAG Definition
print("\n=== 2. Airflow DAG ===")

dag_definition = '''
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'ml-team',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'ml_pipeline_dag',
    default_args=default_args,
    description='End-to-end ML pipeline',
    schedule_interval='0 2 * * *',  # Daily at 2 AM
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    # Task 1: Ingest Data
    ingest = PythonOperator(
        task_id='ingest_data',
        python_callable=ingest_data,
    )

    # Task 2: Process Data
    process = PythonOperator(
        task_id='process_data',
        python_callable=process_data,
    )

    # Task 3: Engineer Features
    engineer = PythonOperator(
        task_id='engineer_features',
        python_callable=engineer_features,
    )

    # Task 4: Train Model
    train = PythonOperator(
        task_id='train_model',
        python_callable=train_model,
    )

    # Task 5: Validate Model
    validate = PythonOperator(
        task_id='validate_model',
        python_callable=validate_model,
    )

    # Task 6: Deploy Model
    deploy = PythonOperator(
        task_id='deploy_model',
        python_callable=deploy_model,
    )

    # Define dependencies
    ingest >> process >> engineer >> train >> validate >> deploy
'''

print("Airflow DAG defined with 6 tasks")

# 3. Pipeline execution summary
print("\n=== 3. Pipeline Execution ===")

class PipelineOrchestrator:
    def __init__(self):
        self.execution_log = []
        self.start_time = None
        self.end_time = None

    def run_pipeline(self):
        self.start_time = datetime.now()
        logger.info("Starting ML pipeline execution")

        try:
            # Execute pipeline tasks
            result1 = ingest_data(task_instance=self)
            self.execution_log.append(('ingest_data', result1))

            result2 = process_data(task_instance=self)
            self.execution_log.append(('process_data', result2))

            result3 = engineer_features(task_instance=self)
            self.execution_log.append(('engineer_features', result3))

            result4 = train_model(task_instance=self)
            self.execution_log.append(('train_model', result4))

            result5 = validate_model(task_instance=self)
            self.execution_log.append(('validate_model', result5))

            result6 = deploy_model(task_instance=self)
            self.execution_log.append(('deploy_model', result6))

            self.end_time = datetime.now()
            logger.info("Pipeline execution completed successfully")

        except Exception as e:
            logger.error(f"Pipeline execution failed: {str(e)}")

    def xcom_push(self, key, value):
        if not hasattr(self, 'xcom_storage'):
            self.xcom_storage = {}
        self.xcom_storage[key] = value

    def xcom_pull(self, key, task_ids):
        if hasattr(self, 'xcom_storage') and key in self.xcom_storage:
            return self.xcom_storage[key]
        return None

    def get_summary(self):
        duration = (self.end_time - self.start_time).total_seconds() if self.end_time else 0
        return {
            'start_time': self.start_time.isoformat() if self.start_time else None,
            'end_time': self.end_time.isoformat() if self.end_time else None,
            'duration_seconds': duration,
            'tasks_executed': len(self.execution_log),
            'execution_log': self.execution_log
        }

# Execute pipeline
orchestrator = PipelineOrchestrator()
orchestrator.run_pipeline()
summary = orchestrator.get_summary()

print("\n=== Pipeline Summary ===")
for key, value in summary.items():
    if key != 'execution_log':
        print(f"{key}: {value}")

print("\nTask Execution Log:")
for task_name, result in summary['execution_log']:
    print(f"  {task_name}: {result}")

print("\nML pipeline automation setup completed!")
```

## Pipeline Best Practices

- **Modularity**: Each step should be independent
- **Idempotency**: Tasks should be safely repeatable
- **Error Handling**: Graceful degradation and alerting
- **Versioning**: Track data, code, and model versions
- **Monitoring**: Track execution metrics and logs

## Scheduling Strategies

- **Daily**: Standard for daily retraining
- **Weekly**: For larger feature engineering
- **On-demand**: Triggered by data updates
- **Real-time**: For streaming applications

## Deliverables

- Automated pipeline DAG
- Task dependency graph
- Execution logs and monitoring
- Performance metrics
- Rollback procedures
- Documentation
