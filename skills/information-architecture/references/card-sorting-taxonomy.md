# Card Sorting & Taxonomy

## Card Sorting & Taxonomy

```python
# Organize content into logical groups

class InformationArchitecture:
    def conduct_card_sort(self, items):
        """Uncover user mental models"""
        return {
            'method': 'Open card sort (users create own categories)',
            'participants': 15,
            'items_sorted': len(items),
            'analysis': self.analyze_card_sort_results(items),
            'dendrograms': 'Show similarity between user groupings',
            'categories': self.identify_categories(items)
        }

    def identify_categories(self, items):
        """Find natural groupings"""
        categories = {}
        frequency = {}

        # Track how often items are grouped together
        # Find dominant groupings

        return {
            'primary_categories': self.get_primary_categories(frequency),
            'ambiguous_items': self.identify_ambiguous_items(frequency),
            'user_created_labels': self.extract_labels()
        }

    def create_taxonomy(self, categories):
        """Build hierarchical structure"""
        return {
            'level1': ['Products', 'Services', 'Support', 'Company'],
            'level2_products': ['Electronics', 'Clothing', 'Books'],
            'level3_electronics': ['Phones', 'Laptops', 'Accessories'],
            'relationships': 'Define parent-child and related items',
            'synonyms': 'Identify similar terms'
        }

    def validate_ia(self, structure):
        """Test with users"""
        return {
            'testing_method': 'Tree testing',
            'tasks': [
                'Find product return policy',
                'Locate shipping information',
                'Access account settings'
            ],
            'success_metrics': {
                'task_completion': '90% target',
                'time_to_complete': '<3 minutes',
                'satisfaction': '>4/5'
            }
        }
```
