# pytest-benchmark for Python

## pytest-benchmark for Python

```python
# test_performance.py
import pytest
from app.services import DataProcessor, SearchEngine
from app.models import User, Product

class TestDataProcessorPerformance:
    @pytest.fixture
    def large_dataset(self):
        """Create large dataset for testing."""
        return [{'id': i, 'value': i * 2} for i in range(10000)]

    def test_process_data_performance(self, benchmark, large_dataset):
        """Benchmark data processing."""
        processor = DataProcessor()

        result = benchmark(processor.process, large_dataset)

        assert len(result) == len(large_dataset)
        # Benchmark will report execution time

    def test_filter_data_performance(self, benchmark, large_dataset):
        """Test filtering performance with different conditions."""
        processor = DataProcessor()

        def filter_operation():
            return processor.filter(large_dataset, lambda x: x['value'] > 5000)

        result = benchmark(filter_operation)
        assert all(item['value'] > 5000 for item in result)

    @pytest.mark.parametrize('dataset_size', [100, 1000, 10000])
    def test_scalability(self, benchmark, dataset_size):
        """Test performance at different scales."""
        processor = DataProcessor()
        data = [{'id': i, 'value': i} for i in range(dataset_size)]

        benchmark(processor.process, data)

class TestSearchPerformance:
    @pytest.fixture
    def search_engine(self):
        """Setup search engine with indexed data."""
        engine = SearchEngine()
        # Index 10,000 products
        for i in range(10000):
            engine.index(Product(id=i, name=f"Product {i}"))
        return engine

    def test_search_performance(self, benchmark, search_engine):
        """Benchmark search query."""
        result = benchmark(search_engine.search, "Product 5000")
        assert len(result) > 0

    def test_search_with_filters(self, benchmark, search_engine):
        """Benchmark search with filters."""
        def search_with_filters():
            return search_engine.search(
                "Product",
                filters={'price_min': 10, 'price_max': 100}
            )

        result = benchmark(search_with_filters)

# Run benchmarks
# pytest test_performance.py --benchmark-only
# pytest test_performance.py --benchmark-compare
```
