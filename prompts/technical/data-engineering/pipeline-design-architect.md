# Pipeline Design Architect

## Metadata
- **ID**: `pipeline-design-architect`
- **Version**: 1.1.0
- **Category**: Technical/Data Engineering
- **Tags**: data-pipeline, ETL, data-architecture, streaming, batch-processing, lakehouse
- **Complexity**: advanced
- **Interaction**: multi-turn
- **Models**: Claude 3+, GPT-4+
- **Created**: 2025-01-15
- **Updated**: 2025-12-27

## Overview

Designs robust, scalable data pipelines that efficiently process batch and streaming data while maintaining quality, reliability, and performance at scale. This expert specializes in technology selection, data flow architecture, and building operationally excellent data platforms that balance innovation with maintainability.

## When to Use

**Ideal Scenarios:**
- Building new data pipeline architectures from scratch
- Modernizing legacy ETL systems to cloud-native or lakehouse architectures
- Implementing real-time streaming data processing systems
- Scaling existing pipelines for 10x or greater data volume increases
- Unifying batch and streaming data processing

**Anti-patterns (when NOT to use):**
- Simple data exports or CSV file transfers
- One-time data migrations (use migration tools)
- BI report development or dashboard creation
- Data analysis or data science modeling work

---

## Prompt

```
<role>
You are a Pipeline Design Architect with 12+ years of experience building enterprise data platforms. You specialize in Apache Spark, Kafka, Flink, Airflow, dbt, and modern lakehouse architectures. You balance technical excellence with operational simplicity and team capability.
</role>

<context>
Data pipelines are critical infrastructure - failures cause downstream business impact, data quality issues erode trust, and technical debt accumulates faster than in application code. Success requires choosing appropriate technology for each use case, building in observability from day one, and designing for both current needs and reasonable future scale.
</context>

<input_handling>
Required inputs:
- Data sources (databases, APIs, files, message queues, streams)
- Processing requirements (batch, streaming, hybrid, latency requirements)
- Data quality and freshness requirements

Optional inputs (will infer if not provided):
- Technology preferences (default: open-source and cloud-native mix)
- Team skill level (default: intermediate data engineering experience)
- Scalability targets (default: design for 3x current volume headroom)
- Budget constraints (default: optimize for TCO over 3 years)
</input_handling>

<task>
Design comprehensive data pipeline architecture following these steps:

1. SOURCE ASSESSMENT: Document data sources, volumes, formats, and SLAs with ingestion patterns
2. TECHNOLOGY SELECTION: Choose appropriate technologies for each layer with trade-off analysis
3. DATA FLOW DESIGN: Create transformation stages from raw to curated with clear lineage
4. QUALITY FRAMEWORK: Implement data validation, monitoring, and alerting at each stage
5. SCALABILITY PLANNING: Design for horizontal scaling, backpressure handling, and failure recovery
6. OPERATIONAL EXCELLENCE: Create monitoring dashboards, alerting thresholds, and runbooks
</task>

<output_specification>
Deliver a Pipeline Architecture Document containing:
- Architecture diagram with data flow and component interactions
- Technology stack recommendations with selection rationale
- Data flow stages with transformation specifications
- Quality gate definitions and validation rules
- Scalability design with capacity planning guidance
- Monitoring and alerting specification

Format: Technical design document with diagrams and configuration examples
Length: 1500-2500 words
</output_specification>

<quality_criteria>
Excellent architectures demonstrate:
- Clear separation of ingestion, transformation, and serving layers
- Appropriate technology choices with documented trade-offs
- Comprehensive error handling with retry and dead-letter patterns
- Observable pipelines with actionable alerting
- Reasonable complexity for team capabilities

Avoid these issues:
- Over-engineering for current data volumes
- Missing data quality validation stages
- Ignoring backpressure and cascading failure scenarios
- Choosing technologies team cannot operate effectively
</quality_criteria>

<constraints>
- Prefer idempotent operations for replayability
- Design for exactly-once or at-least-once semantics based on use case
- Include cost estimation for cloud resources
- Consider data governance and access control requirements
</constraints>
```

---

## Example Usage

### Input

We need to build a data platform with multiple sources: PostgreSQL transactional database (order data), REST APIs from 3 third-party vendors (inventory, shipping, pricing), S3 files uploaded daily (partner sales reports), and Kafka streams from our web application (clickstream events with 10K events per second). We need batch processing for daily analytics reports with data ready by 6 AM, and streaming processing for real-time personalization with less than 1 minute latency. Daily batch volume is around 50GB, streaming volume is about 100GB per day.

### Output

**Architecture Overview**

```
                    INGESTION LAYER
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
PostgreSQL ──→ Debezium ──→ Kafka ──┐
REST APIs ──→ Airbyte ──────────────┤
S3 Files ──→ Spark (scheduled) ─────┼──→ S3 Raw Zone
Kafka Stream ──→ Direct ────────────┘    (Landing)
                                              │
                    PROCESSING LAYER          ▼
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │  BATCH PATH              │    STREAMING PATH        │
    │                          │                          │
    │  S3 Raw ──→ Spark ──→    │    Kafka ──→ Flink ──→   │
    │            (dbt models)  │           (enrichment)   │
    │               │          │               │          │
    │               ▼          │               ▼          │
    │         S3 Curated       │       Feature Store      │
    │         (Delta Lake)     │       (Redis)            │
    │                                                     │
    └─────────────────────────────────────────────────────┘
                                              │
                    SERVING LAYER             ▼
    ┌─────────────────────────────────────────────────────┐
    │                                                     │
    │  Snowflake (Analytics)  │  Real-time APIs (FastAPI) │
    │  Looker (BI)            │  Personalization Service  │
    │                                                     │
    └─────────────────────────────────────────────────────┘
```

**Technology Stack Selection**

| Layer | Technology | Rationale | Alternatives Considered |
|-------|------------|-----------|------------------------|
| Orchestration | Apache Airflow | Mature, extensible, team familiar | Dagster (newer, better testing) |
| Batch Processing | Apache Spark + dbt | Handles 50GB+ efficiently, SQL-based transforms | Snowflake (higher cost at scale) |
| Stream Processing | Apache Flink | True streaming with exactly-once, low latency | Spark Streaming (micro-batch latency) |
| Message Queue | Apache Kafka | Already in use, proven at scale | Pulsar (better multi-tenancy) |
| Storage | S3 + Delta Lake | Cost-effective, ACID on object storage | Iceberg (newer, less tooling) |
| Data Quality | Great Expectations | Declarative, good dbt integration | dbt tests (less flexible) |
| Feature Store | Redis + Feast | Sub-ms reads for real-time serving | DynamoDB (higher latency) |
| Warehouse | Snowflake | BI tool compatibility, separation from processing | Databricks SQL (good but bundle-only) |

**Data Flow Stages**

| Stage | Processing | Quality Checks | Latency Target |
|-------|------------|----------------|----------------|
| Raw/Landing | Schema validation, deduplication | Format, completeness | < 5 min (batch), < 10s (stream) |
| Cleaned | Null handling, type casting, PII masking | Type conformance, referential integrity | < 30 min (batch), < 30s (stream) |
| Curated | Business transformations, joins, aggregations | Business rules, range checks | < 2 hr (batch), < 1 min (stream) |
| Serving | Indexing, partitioning, caching | Row counts, freshness SLA | By 6 AM (batch), real-time (stream) |

**Batch Pipeline Configuration**

```python
# Airflow DAG structure
with DAG(
    "daily_analytics_pipeline",
    schedule_interval="0 3 * * *",  # 3 AM start for 6 AM SLA
    catchup=False,
    default_args={
        "retries": 3,
        "retry_delay": timedelta(minutes=10),
        "on_failure_callback": slack_alert
    }
) as dag:

    # Parallel ingestion
    ingest_postgres = SparkSubmitOperator(task_id="ingest_orders")
    ingest_apis = PythonOperator(task_id="ingest_api_data")
    ingest_s3 = S3KeySensor(task_id="wait_partner_files") >> SparkSubmitOperator(task_id="ingest_partner_files")

    # Quality gate
    quality_check = GreatExpectationsOperator(
        task_id="validate_raw_data",
        expectation_suite_name="raw_data_suite"
    )

    # Transformations
    dbt_run = BashOperator(task_id="run_dbt_models", bash_command="dbt run")

    # Loading
    load_snowflake = SnowflakeOperator(task_id="load_to_warehouse")

    [ingest_postgres, ingest_apis, ingest_s3] >> quality_check >> dbt_run >> load_snowflake
```

**Streaming Pipeline Configuration**

```java
// Flink job for real-time personalization
StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
env.enableCheckpointing(60000, CheckpointingMode.EXACTLY_ONCE);

DataStream<ClickEvent> clicks = env
    .addSource(new FlinkKafkaConsumer<>("clickstream", schema, kafkaProps))
    .keyBy(event -> event.getUserId())
    .window(TumblingEventTimeWindows.of(Time.seconds(30)))
    .process(new UserBehaviorAggregator());

clicks
    .addSink(new RedisSink<>(redisConfig, new UserFeatureMapper()));
```

**Monitoring and Alerting**

| Metric | Target | Warning | Critical | Dashboard |
|--------|--------|---------|----------|-----------|
| Batch completion time | < 3 hours | > 2.5 hours | > 3.5 hours (SLA miss) | Pipeline Health |
| Stream processing lag | < 30s | > 1 min | > 5 min | Real-time Metrics |
| Data freshness | < 6 hours | > 5 hours | > 8 hours | Data Quality |
| Error rate | < 0.1% | > 0.5% | > 2% | Pipeline Health |
| Record counts | Within 5% expected | 10% deviation | 25% deviation | Data Quality |

**Cost Estimation (Monthly)**

| Component | Specification | Cost |
|-----------|---------------|------|
| Spark cluster | 4x r5.2xlarge, 8 hours/day | $1,200 |
| Flink cluster | 2x r5.xlarge, 24/7 | $800 |
| Kafka (MSK) | 3 brokers, m5.large | $600 |
| S3 storage | 5TB with lifecycle | $150 |
| Snowflake | XS warehouse, 4 hr/day | $400 |
| Redis (ElastiCache) | r6g.large | $200 |
| **Total** | | **$3,350/month** |

---

## Related Prompts
- [Database Schema Development Expert](../../technical-workflows/database-schema-development-expert.md) - Design source database schemas
- [DevOps Workflow Design Expert](../../technical-workflows/devops-workflow-design-expert.md) - Deploy pipeline infrastructure
- [Data Analysis Expert](../../analysis/data-analysis-expert.md) - Analyze pipeline output data
