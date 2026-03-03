# Cross-Database Migration

## Cross-Database Migration

```python
from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
import logging

logger = logging.getLogger(__name__)

class CrossDatabaseMigration:
    def __init__(self, source_url: str, target_url: str):
        self.source_engine = create_engine(source_url)
        self.target_engine = create_engine(target_url)

        self.source_session = sessionmaker(bind=self.source_engine)()
        self.target_session = sessionmaker(bind=self.target_engine)()

    def migrate_table(self, table_name: str, batch_size: int = 1000):
        """Migrate table from source to target database."""
        logger.info(f"Starting migration of table: {table_name}")

        # Get table metadata
        metadata = MetaData()
        source_table = Table(
            table_name,
            metadata,
            autoload_with=self.source_engine
        )

        # Get total count
        total = self.source_session.execute(
            source_table.select().with_only_columns(func.count())
        ).scalar()

        logger.info(f"Total records to migrate: {total}")

        # Migrate in batches
        offset = 0
        while offset < total:
            # Fetch batch from source
            results = self.source_session.execute(
                source_table.select()
                .limit(batch_size)
                .offset(offset)
            ).fetchall()

            if not results:
                break

            # Transform and insert to target
            rows = [dict(row._mapping) for row in results]
            transformed = [self.transform_row(row) for row in rows]

            self.target_session.execute(
                source_table.insert(),
                transformed
            )
            self.target_session.commit()

            offset += batch_size
            logger.info(f"Migrated {offset}/{total} records")

        logger.info(f"Completed migration of {table_name}")

    def transform_row(self, row: dict) -> dict:
        """Transform row data if needed."""
        # Apply any transformations
        return row

    def cleanup(self):
        """Close connections."""
        self.source_session.close()
        self.target_session.close()
```
