"""
Exercise 3: Chain-of-Thought Prompting
Module 2 — Prompt Engineering & APIs
Sprint 1: Foundation

Task: Create a function called build_cot_prompt that adds step-by-step
reasoning to prompts.
"""


def build_cot_prompt(question: str, context: str = "") -> str:
    """Build a chain-of-thought prompt that encourages step-by-step reasoning."""
    prompt = ""
    if context:
        prompt += f"Context: {context}\n\n"

    prompt += f"Question: {question}\n\n"
    prompt += "Let's think through this step by step:\n"
    prompt += "1. First, identify the key information.\n"
    prompt += "2. Then, analyze the relationships.\n"
    prompt += "3. Consider any edge cases or exceptions.\n"
    prompt += "4. Finally, provide a clear conclusion.\n\n"
    prompt += "Your step-by-step analysis:"
    return prompt


# Real-world AI career scenario
prompt = build_cot_prompt(
    "Should a Java developer with 8 years of experience pursue LLM development or ML engineering?",
    "The developer knows basic Python, has used ChatGPT casually, and wants to change careers to AI."
)
print(prompt)
