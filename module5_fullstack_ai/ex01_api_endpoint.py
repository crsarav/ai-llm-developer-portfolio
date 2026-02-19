"""
Exercise 1: AI API Endpoint Design
Module 5 — Full-Stack AI Applications
Sprint 3: Launch

Task: Design a FastAPI-style endpoint for an AI chat service.
"""


def create_chat_endpoint_spec() -> dict:
    """Define the API spec for an AI chat endpoint."""
    return {
        "endpoint": "/api/chat",
        "method": "POST",
        "request_body": {
            "message": "string (required) — user's message",
            "conversation_id": "string (optional) — for context",
            "model": "string (optional) — default: gpt-4",
            "temperature": "float (optional) — 0.0 to 1.0, default: 0.7",
            "max_tokens": "int (optional) — default: 1000",
        },
        "response": {
            "reply": "string — AI's response",
            "conversation_id": "string — for follow-up",
            "tokens_used": "int — for cost tracking",
            "model": "string — model used",
        },
        "errors": {
            "400": "Invalid request body",
            "401": "Missing or invalid API key",
            "429": "Rate limit exceeded",
            "500": "AI model error",
        },
    }


def estimate_api_cost(tokens: int, model: str = "gpt-4") -> float:
    """Estimate the cost of an API call based on token usage."""
    rates = {
        "gpt-4": {"input": 0.03, "output": 0.06},
        "gpt-3.5-turbo": {"input": 0.001, "output": 0.002},
        "claude-sonnet": {"input": 0.003, "output": 0.015},
    }
    rate = rates.get(model, rates["gpt-4"])
    avg_rate = (rate["input"] + rate["output"]) / 2
    return round(tokens / 1000 * avg_rate, 4)


if __name__ == "__main__":
    spec = create_chat_endpoint_spec()
    print("=== AI Chat API Spec ===")
    print(f"Endpoint: {spec['method']} {spec['endpoint']}")
    print(f"Request fields: {len(spec['request_body'])}")
    print(f"Error codes: {list(spec['errors'].keys())}")
    print()

    for model in ["gpt-4", "gpt-3.5-turbo", "claude-sonnet"]:
        cost = estimate_api_cost(1000, model)
        print(f"1000 tokens on {model}: ${cost}")
