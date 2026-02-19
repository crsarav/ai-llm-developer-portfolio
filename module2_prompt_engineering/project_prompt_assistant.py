"""
Mini Project: AI Prompt Engineering Assistant
Module 2 — Prompt Engineering & APIs (Week 4)
Sprint 1: Foundation

A tool that helps users create effective prompts for different AI tasks.
"""


class PromptBuilder:
    """Build structured prompts with configurable parameters."""

    TEMPLATES = {
        "classify": "Classify the following text into one of these categories: {categories}.\n\nText: {input}\nCategory:",
        "summarize": "Summarize the following text in {length} words or fewer.\n\nText: {input}\nSummary:",
        "extract": "Extract the following information from the text: {fields}.\n\nText: {input}\nExtracted:",
        "generate": "Generate {count} {type} about {topic}.\nStyle: {style}\n\nOutput:",
        "translate": "Translate the following from {source_lang} to {target_lang}.\n\nText: {input}\nTranslation:",
    }

    def __init__(self):
        self.system_prompt = ""
        self.examples = []
        self.constraints = []

    def set_system(self, prompt: str) -> "PromptBuilder":
        self.system_prompt = prompt
        return self

    def add_example(self, input_text: str, output_text: str) -> "PromptBuilder":
        self.examples.append((input_text, output_text))
        return self

    def add_constraint(self, constraint: str) -> "PromptBuilder":
        self.constraints.append(constraint)
        return self

    def build(self, template_name: str, **kwargs) -> str:
        template = self.TEMPLATES.get(template_name, "{input}")
        prompt_parts = []

        if self.system_prompt:
            prompt_parts.append(f"System: {self.system_prompt}")

        if self.constraints:
            prompt_parts.append("Constraints:\n" + "\n".join(f"- {c}" for c in self.constraints))

        if self.examples:
            prompt_parts.append("Examples:")
            for inp, out in self.examples:
                prompt_parts.append(f"  Input: {inp}\n  Output: {out}")

        prompt_parts.append(template.format(**kwargs))
        return "\n\n".join(prompt_parts)


if __name__ == "__main__":
    builder = PromptBuilder()
    prompt = (
        builder
        .set_system("You are an expert text classifier for a tech company.")
        .add_constraint("Respond with only the category name")
        .add_constraint("If unsure, respond with 'unclear'")
        .add_example("Our server crashed at 3am", "incident")
        .add_example("Can we add dark mode?", "feature-request")
        .add_example("Login page shows wrong error", "bug")
        .build("classify",
               categories="bug, feature-request, incident, question",
               input="The API returns 500 when uploading files over 10MB")
    )
    print(prompt)
