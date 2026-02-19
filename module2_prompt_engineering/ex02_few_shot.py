"""
Exercise 2: Few-Shot Prompting
Module 2 — Prompt Engineering & APIs
Sprint 1: Foundation

Task: Build a few-shot prompt constructor for classification tasks.
"""


def build_few_shot_classifier(task: str, examples: list[tuple[str, str]], input_text: str) -> str:
    """Build a few-shot classification prompt."""
    prompt = f"Task: {task}\n\n"
    prompt += "Examples:\n"

    for text, label in examples:
        prompt += f'  Input: "{text}"\n  Label: {label}\n\n'

    prompt += f'Now classify:\n  Input: "{input_text}"\n  Label:'
    return prompt


examples = [
    ("The stock market crashed today", "negative"),
    ("Our revenue grew 40% this quarter", "positive"),
    ("The meeting is scheduled for 3pm", "neutral"),
    ("We lost our biggest client", "negative"),
    ("The new AI product launch exceeded expectations", "positive"),
]

test_inputs = [
    "AI adoption is accelerating across enterprises",
    "Budget cuts forced us to cancel the ML project",
    "The quarterly report will be published Friday",
]

for inp in test_inputs:
    prompt = build_few_shot_classifier("Sentiment Classification", examples, inp)
    print(f"Input: {inp}")
    print(f"Prompt length: {len(prompt)} chars")
    print("---")
