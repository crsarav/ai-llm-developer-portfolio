"""
Exercise 4: Working with Files & Data
Module 1 — Python & AI Foundations
Sprint 1: Foundation (Day 4)

Task: Build a function that processes text and computes basic stats.
"""
import re
from collections import Counter


def analyze_text(text: str) -> dict:
    """Analyze text and return statistics relevant to AI/NLP work."""
    words = text.lower().split()
    sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]
    word_freq = Counter(words)

    return {
        "total_words": len(words),
        "unique_words": len(set(words)),
        "total_sentences": len(sentences),
        "avg_words_per_sentence": round(len(words) / max(len(sentences), 1), 1),
        "top_5_words": word_freq.most_common(5),
        "vocabulary_richness": round(len(set(words)) / max(len(words), 1), 3),
    }


sample_text = """
Artificial intelligence is transforming every industry. Companies that adopt AI
early will have a significant competitive advantage. Machine learning models
can process data at scale, finding patterns that humans might miss. The key to
successful AI adoption is starting with clear business problems and building
from there. AI is not magic — it is mathematics, data, and engineering.
"""

stats = analyze_text(sample_text)
print("=== Text Analysis Results ===")
for key, value in stats.items():
    print(f"  {key}: {value}")
