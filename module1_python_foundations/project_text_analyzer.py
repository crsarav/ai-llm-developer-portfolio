"""
Mini Project: Text Analyzer
Module 1 — Python & AI Foundations (Week 4)
Sprint 1: Foundation

A complete text analysis tool that an LLM Developer would build
as their first portfolio piece.
"""
import re
import json
from collections import Counter


def analyze_document(text: str) -> dict:
    """Full document analysis pipeline."""
    words = text.lower().split()
    sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
    word_freq = Counter(words)

    ai_keywords = ["ai", "artificial", "intelligence", "machine", "learning",
                    "model", "data", "neural", "deep", "nlp", "llm", "gpt"]
    ai_mentions = sum(1 for w in words if w in ai_keywords)

    return {
        "word_count": len(words),
        "sentence_count": len(sentences),
        "unique_words": len(set(words)),
        "avg_sentence_length": round(len(words) / max(len(sentences), 1), 1),
        "vocabulary_richness": round(len(set(words)) / max(len(words), 1), 3),
        "top_10_words": word_freq.most_common(10),
        "ai_keyword_density": round(ai_mentions / max(len(words), 1) * 100, 2),
        "reading_time_minutes": round(len(words) / 200, 1),
    }


def generate_summary(analysis: dict) -> str:
    """Generate a human-readable summary of the analysis."""
    lines = [
        f"📊 Document has {analysis['word_count']} words in {analysis['sentence_count']} sentences.",
        f"📖 Estimated reading time: {analysis['reading_time_minutes']} minutes.",
        f"🔤 Vocabulary richness: {analysis['vocabulary_richness']:.1%}",
        f"🤖 AI keyword density: {analysis['ai_keyword_density']}%",
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    sample = """
    The rise of large language models has fundamentally changed how we build
    software. Companies like OpenAI, Anthropic, and Google have released
    increasingly powerful AI models. Developers who understand prompt engineering,
    RAG architectures, and AI agent design patterns are in extremely high demand.
    The transition from traditional software development to AI engineering
    requires learning new skills, but the fundamentals of good engineering
    still apply. Data quality, testing, and deployment remain critical.
    """

    result = analyze_document(sample)
    print(generate_summary(result))
    print(f"\nFull analysis:\n{json.dumps(result, indent=2, default=str)}")
