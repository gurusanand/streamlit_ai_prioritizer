"""
Framework data loader - Loads the 31-dimension evaluation framework
"""

import json
from pathlib import Path

def load_framework_data():
    """Load framework data from JSON file"""
    framework_file = Path(__file__).parent.parent / 'data' / 'framework_data.json'
    
    if not framework_file.exists():
        # Return default framework if file doesn't exist
        return get_default_framework()
    
    with open(framework_file, 'r') as f:
        return json.load(f)

def get_categories(framework):
    """Get unique categories from framework"""
    categories = []
    seen = set()
    for item in framework:
        if item['category'] not in seen:
            categories.append(item['category'])
            seen.add(item['category'])
    return categories

def get_default_framework():
    """Return default framework structure"""
    return [
        {
            "category": "Strategic & Business",
            "dimension": "Business Impact & Value",
            "default_weight": 10,
            "description": "Potential revenue increase, cost savings, customer satisfaction improvement, competitive advantage",
            "scores": {
                "1": "Minimal impact (<$100K annual value)",
                "2": "Low impact ($100K-$500K)",
                "3": "Moderate impact ($500K-$2M)",
                "4": "High impact ($2M-$10M)",
                "5": "Transformational (>$10M or strategic differentiator)"
            }
        },
        # Add more dimensions as needed
    ]

