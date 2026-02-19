"""
Exercise 1: Basic Prompt Construction
Module 2 — Prompt Engineering & APIs
Sprint 1: Foundation

Task: Create a function called format_prompt(topic, style) that generates
structured prompts for an LLM.
"""


def format_prompt(topic: str, style: str = "concise") -> str:
    """Generate a structured prompt for an LLM."""
    style_instructions = {
        "concise": "Be brief and to the point. Use bullet points.",
        "detailed": "Provide thorough explanations with examples.",
        "eli5": "Explain like I'm 5. Use simple analogies.",
        "technical": "Use precise technical language. Include code examples.",
    }

    instruction = style_instructions.get(style, style_instructions["concise"])

    return f"""You are a helpful AI assistant.

Topic: {topic}
Style: {style}

Instructions: {instruction}

Please provide your response now."""


def create_system_prompt(role: str, background: str) -> str:
    """Create a system prompt personalized to the user's background."""
    return f"""You are an AI career mentor called Nyra.
You are helping a {background} professional transition to the role of {role}.
Always relate AI concepts back to their existing {background} experience.
Be encouraging but honest. Focus on practical, actionable advice."""


# Test
print("=== Basic Prompt ===")
print(format_prompt("RAG architecture", "technical"))
print()
print("=== System Prompt ===")
print(create_system_prompt("LLM Developer", "Java/Spring Developer"))
