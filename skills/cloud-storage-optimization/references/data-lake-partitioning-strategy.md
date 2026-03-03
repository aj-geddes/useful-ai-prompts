# Data Lake Partitioning Strategy

## Data Lake Partitioning Strategy

```python
# Optimized partitioning for data lakes
def create_partitioned_data_lake(source_file, bucket, format='parquet'):
    import pyarrow.parquet as pq
    import pyarrow as pa

    # Read data
    table = pq.read_table(source_file)
    df = table.to_pandas()

    # Create partitions
    partitions = {
        'year': df['date'].dt.year,
        'month': df['date'].dt.month,
        'day': df['date'].dt.day,
        'region': df['region']
    }

    # Group by partitions
    for year, year_group in df.groupby(partitions['year']):
        for month, month_group in year_group.groupby(partitions['month']):
            for day, day_group in month_group.groupby(partitions['day']):
                for region, region_group in day_group.groupby(partitions['region']):
                    # Create partition path
                    path = f"s3://{bucket}/data/year={year}/month={month:02d}/day={day:02d}/region={region}"

                    # Save as Parquet with compression
                    table = pa.Table.from_pandas(region_group)
                    pq.write_table(
                        table,
                        f"{path}/data.parquet",
                        compression='snappy',
                        use_dictionary=True
                    )
```
