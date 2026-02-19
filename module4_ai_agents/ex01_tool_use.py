"""
Exercise 1: Tool Use Patterns
Module 4 — AI Agents & Tool Use
Sprint 2: Build

Task: Create a function called execute_tool that dispatches
tool calls based on name and arguments.
"""
import json
import math


TOOLS = {
    "calculator": {
        "description": "Perform mathematical calculations",
        "handler": lambda args: str(eval(args.get("expression", "0"))),
    },
    "word_count": {
        "description": "Count words in text",
        "handler": lambda args: str(len(args.get("text", "").split())),
    },
    "sentiment": {
        "description": "Basic sentiment analysis",
        "handler": lambda args: "positive" if any(
            w in args.get("text", "").lower()
            for w in ["great", "good", "excellent", "love", "amazing"]
        ) else "negative" if any(
            w in args.get("text", "").lower()
            for w in ["bad", "terrible", "hate", "awful", "worst"]
        ) else "neutral",
    },
}


def execute_tool(tool_name: str, arguments: dict) -> str:
    """Execute a tool by name with given arguments."""
    tool = TOOLS.get(tool_name)
    if not tool:
        return f"Error: Unknown tool '{tool_name}'"
    try:
        return tool["handler"](arguments)
    except Exception as e:
        return f"Error: {e}"


# Simulate agent tool calls
calls = [
    ("calculator", {"expression": "45000 * 1.3 - 12000"}),
    ("word_count", {"text": "AI is transforming how we build software applications"}),
    ("sentiment", {"text": "The new AI product launch was amazing and exceeded all expectations"}),
]

for name, args in calls:
    result = execute_tool(name, args)
    print(f"Tool: {name}({json.dumps(args)[:60]}...) → {result}")
