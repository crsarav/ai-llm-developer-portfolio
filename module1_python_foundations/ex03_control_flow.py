"""
Exercise 3: Control Flow & Error Handling
Module 1 — Python & AI Foundations
Sprint 1: Foundation (Day 3)

Task: Write a function called safe_parse_json(text) that safely parses JSON.
"""
import json


def safe_parse_json(text: str) -> dict | None:
    """Safely parse JSON, returning None on failure instead of crashing."""
    try:
        return json.loads(text)
    except (json.JSONDecodeError, TypeError):
        return None


def classify_ai_readiness(score: int) -> str:
    """Classify organization's AI readiness based on score (0-100)."""
    if score >= 80:
        return "Ready — start building"
    elif score >= 60:
        return "Promising — invest in training"
    elif score >= 40:
        return "Developing — build data foundation"
    else:
        return "Early stage — start with awareness"


# Test safe_parse_json
valid = safe_parse_json('{"model": "gpt-4", "temperature": 0.7}')
invalid = safe_parse_json('not json at all')
empty = safe_parse_json('')

print(f"Valid JSON: {valid}")
print(f"Invalid JSON: {invalid}")
print(f"Empty string: {empty}")

# Test AI readiness classifier
for score in [25, 45, 65, 85]:
    result = classify_ai_readiness(score)
    print(f"Score {score}: {result}")
