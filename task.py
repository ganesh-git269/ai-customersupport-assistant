TASKS = [
    {
        "query": "Where is my order?",
        "expected": {
            "category": "delivery",
            "priority": "low",
            "sentiment": "neutral"
        }
    },
    {
        "query": "My order is delayed and I'm upset",
        "expected": {
            "category": "delivery",
            "priority": "medium",
            "sentiment": "angry"
        }
    },
    {
        "query": "Money deducted but order not placed",
        "expected": {
            "category": "billing",
            "priority": "high",
            "sentiment": "angry"
        }
    }
]