# Pipeline Design Architect

## Metadata

- **Category**: Technical/Data-Engineering
- **Tags**: data pipeline, ETL, data architecture, streaming, batch processing
- **Created**: 2025-07-20
- **Version**: 2.0.0
- **Use Cases**: pipeline design, data orchestration, ETL optimization, real-time processing
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

This prompt helps you design robust, scalable data pipelines that efficiently process data while maintaining quality, reliability, and performance.

## Prompt

```
I'll help you design a robust data pipeline that meets your processing needs. Let me understand your requirements:

**Data characteristics:**
1. What are your data sources? (databases, APIs, files, streams)
2. What's the data volume and velocity? (GB/day, records/second)
3. What formats are you dealing with? (JSON, CSV, Parquet, etc.)
4. Is this batch, streaming, or hybrid processing?

**Processing requirements:**
5. What transformations are needed? (cleaning, aggregation, enrichment)
6. Any data quality requirements or validation rules?
7. What's the acceptable latency? (real-time, near real-time, daily)
8. What are your downstream consumers? (warehouse, analytics, applications)

**Technical context:**
9. What's your current tech stack or preferences?
10. Any scalability requirements? (expected growth)
11. What's your team's expertise level?
12. Any compliance or security requirements?

Based on your answers, I'll provide:

**PIPELINE ARCHITECTURE** - End-to-end design with component selection
**DATA FLOW DESIGN** - Detailed processing stages and transformations
**SCALABILITY STRATEGY** - How to handle growth and peak loads
**MONITORING & RELIABILITY** - Observability and error handling
**IMPLEMENTATION PLAN** - Phased approach with best practices

Share your pipeline requirements and let's build something reliable!
```

## Example Usage

**User Input:**
```
1. Multiple sources: PostgreSQL (transactional), REST APIs (3rd party), S3 files (logs), Kafka (clickstream)
2. 50GB/day batch, 10K events/second streaming, expecting 3x growth in 1 year
3. Mostly JSON and CSV, some nested JSON from APIs, compressed log files
4. Hybrid - both batch and streaming pipelines needed

5. Data cleaning, deduplication, joining with reference data, aggregations, ML feature engineering
6. Need data quality checks - completeness, freshness, schema validation, anomaly detection
7. Streaming: <1 minute, Batch: within 2 hours of availability
8. Snowflake warehouse, Tableau dashboards, ML platform, some real-time APIs

9. Currently using Python scripts and cron jobs, want to modernize. Team knows Python, SQL, some Spark
10. Must handle 3x current volume, seasonal 5x spikes during holidays
11. 4 data engineers, intermediate level, eager to learn
12. GDPR compliance, PII masking required, SOC2 audit trail
```

**Assistant Output:**

Based on your hybrid data pipeline needs, here's a comprehensive architecture design:

## PIPELINE ARCHITECTURE

### Recommended Technology Stack

**Orchestration**: Apache Airflow (batch) + Kafka (streaming)
**Processing**: Apache Spark (batch) + Flink (streaming)
**Storage**: S3 (data lake) + Delta Lake (ACID transactions)
**Data Quality**: Great Expectations + custom frameworks
**Monitoring**: Datadog + Airflow UI + custom dashboards

### High-Level Architecture

```
Data Sources                Processing Layer              Storage & Serving
━━━━━━━━━━━━━              ━━━━━━━━━━━━━━━━━           ━━━━━━━━━━━━━━━━━
                                                         
PostgreSQL ──┐                                          ┌─→ Snowflake DW
             ├─→ Airflow ─→ Spark Batch ─→ S3/Delta ───┤
REST APIs ───┤   (Batch)     (Transform)    (Lake)     ├─→ ML Platform
             │                                          │
S3 Files ────┘                                          └─→ Tableau
                                                         
Kafka ───────→ Flink ─→ Feature Store ─→ Real-time APIs
          (Streaming)   (Low latency)
```

## DATA FLOW DESIGN

### Batch Pipeline (Airflow + Spark)

**DAG Structure**:
```python
# Conceptual Airflow DAG
with DAG('daily_data_pipeline', schedule='0 2 * * *'):
    
    # Stage 1: Ingestion (parallel)
    extract_postgres = SparkSubmitOperator(task_id='extract_postgres')
    extract_apis = PythonOperator(task_id='extract_apis')
    extract_s3_logs = SparkSubmitOperator(task_id='extract_s3')
    
    # Stage 2: Data Quality
    validate_schemas = DataQualityOperator(
        expectations_suite='raw_data_suite'
    )
    
    # Stage 3: Transformation
    clean_deduplicate = SparkSubmitOperator(
        application='transformations/clean_dedup.py',
        conf={'spark.sql.adaptive.enabled': 'true'}
    )
    
    # Stage 4: Enrichment
    join_reference_data = SparkSubmitOperator()
    feature_engineering = SparkSubmitOperator()
    
    # Stage 5: Load
    load_to_snowflake = SnowflakeOperator()
    update_ml_features = SparkSubmitOperator()
```

### Streaming Pipeline (Kafka + Flink)

**Processing Topology**:
```
Kafka Input → Flink Job
├── Stream 1: Deduplication Window (1 min)
├── Stream 2: Enrichment with Reference Data
├── Stream 3: Real-time Aggregations
└── Stream 4: Anomaly Detection
    ↓
├── Kafka Output (enriched stream)
├── Feature Store (ML features)
└── S3/Delta (archive)
```

### Data Transformation Patterns

**1. Deduplication Strategy**:
```python
# Batch: Use window functions
df.withWatermark("event_time", "10 minutes") \
  .dropDuplicates(["user_id", "event_id"])

# Streaming: State store with TTL
```

**2. PII Masking**:
```python
# Centralized masking function
def mask_pii(df):
    return df.withColumn("email", 
        sha2(col("email"), 256)
    ).withColumn("phone",
        regexp_replace("phone", r"\d", "X")
    )
```

**3. Data Quality Checks**:
```yaml
# Great Expectations suite
expectations:
  - expect_column_values_to_not_be_null: 
      column: user_id
  - expect_column_values_to_be_between:
      column: age
      min_value: 0
      max_value: 120
  - expect_table_row_count_to_be_between:
      min_value: 100000
      max_value: 10000000
```

## SCALABILITY STRATEGY

### Auto-scaling Configuration

**Spark Cluster**:
```
Base: 4 nodes (m5.xlarge)
Peak: 20 nodes (auto-scale)
Trigger: CPU > 70% for 5 min
```

**Flink Configuration**:
```
Parallelism: 16 (4x input partitions)
Checkpointing: 1 minute intervals
State Backend: RocksDB for large state
```

### Performance Optimization

**1. Partitioning Strategy**:
- S3/Delta: Partition by date + hour
- Kafka: 16 partitions (4x consumers)
- Snowflake: Cluster by user_id

**2. Caching Strategy**:
- Reference data in Redis (1hr TTL)
- Spark broadcast joins for small tables
- Materialized views in Snowflake

**3. Resource Management**:
```python
# Dynamic allocation
spark.conf.set("spark.dynamicAllocation.enabled", "true")
spark.conf.set("spark.dynamicAllocation.minExecutors", "4")
spark.conf.set("spark.dynamicAllocation.maxExecutors", "20")
```

## MONITORING & RELIABILITY

### Observability Stack

**1. Pipeline Metrics**:
```
Key Metrics Dashboard:
├── Processing Time (P50, P95, P99)
├── Record Count by Stage
├── Error Rate by Component
├── Data Freshness (lag from source)
└── Resource Utilization
```

**2. Data Quality Monitoring**:
```python
# Custom quality metrics
quality_metrics = {
    "completeness": count_nulls / total_records,
    "freshness": max(current_time - event_time),
    "validity": failed_validations / total_records,
    "uniqueness": duplicate_count / total_records
}
```

**3. Alerting Rules**:
- Pipeline failure: PagerDuty (immediate)
- Data quality below threshold: Slack (15 min)
- Performance degradation: Email (hourly)
- Cost anomaly: Daily report

### Error Handling

**Retry Strategy**:
```python
# Airflow task retry
retry_delay=timedelta(minutes=5),
retries=3,
retry_exponential_backoff=True
```

**Dead Letter Queue**:
- Failed records → DLQ topic
- Manual inspection UI
- Reprocessing workflow

## IMPLEMENTATION PLAN

### Phase 1: Foundation (Weeks 1-4)
1. **Environment Setup**
   - Provision Airflow (managed or EKS)
   - Configure Spark clusters
   - Set up monitoring

2. **Pilot Pipeline**
   - Pick simplest data source
   - Implement basic transformations
   - Establish CI/CD

### Phase 2: Batch Pipeline (Weeks 5-8)
1. **Core Implementation**
   - Migrate all batch sources
   - Implement data quality
   - Build error handling

2. **Testing & Optimization**
   - Load testing at 3x volume
   - Performance tuning
   - Cost optimization

### Phase 3: Streaming Pipeline (Weeks 9-12)
1. **Streaming Setup**
   - Deploy Flink cluster
   - Implement deduplication
   - Real-time analytics

2. **Integration**
   - Connect to feature store
   - API endpoints
   - Monitoring dashboard

### Phase 4: Production Hardening (Weeks 13-16)
- Disaster recovery testing
- Security audit
- Documentation
- Team training

### Team Enablement

**Week 1-2**: Spark fundamentals workshop
**Week 3-4**: Airflow patterns and best practices
**Week 5-6**: Streaming concepts with Flink
**Ongoing**: Pair programming and code reviews

### Success Metrics

- **Latency**: Batch <2hr, Streaming <1min ✓
- **Reliability**: 99.9% uptime
- **Quality**: <0.1% bad records
- **Scale**: Handle 5x peak loads
- **Cost**: <$0.10 per GB processed

This architecture provides a solid foundation that can grow with your needs while maintaining reliability and performance.

## Related Prompts

- [Data Quality Framework](./data-quality-expert.md)
- [Stream Processing Expert](./stream-processing-expert.md)
- [Data Warehouse Architect](./data-warehouse-expert.md)