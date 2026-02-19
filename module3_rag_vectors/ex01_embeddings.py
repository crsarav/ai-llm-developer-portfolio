"""
Exercise 1: Understanding Embeddings
Module 3 — RAG & Vector Databases
Sprint 2: Build

Task: Create a function called compute_similarity that computes
cosine similarity between text representations.
"""
import math


def compute_similarity(vec_a: list[float], vec_b: list[float]) -> float:
    """Compute cosine similarity between two vectors."""
    if len(vec_a) != len(vec_b):
        raise ValueError("Vectors must be the same length")

    dot_product = sum(a * b for a, b in zip(vec_a, vec_b))
    magnitude_a = math.sqrt(sum(a ** 2 for a in vec_a))
    magnitude_b = math.sqrt(sum(b ** 2 for b in vec_b))

    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0
    return round(dot_product / (magnitude_a * magnitude_b), 4)


# Simulated embeddings (in production these come from OpenAI/Cohere)
embeddings = {
    "Python is great for AI": [0.8, 0.9, 0.2, 0.1],
    "Machine learning uses data": [0.7, 0.85, 0.3, 0.15],
    "I love pizza": [0.1, 0.05, 0.9, 0.8],
    "Java Spring Boot framework": [0.6, 0.3, 0.1, 0.05],
}

query = "AI programming languages"
query_vec = [0.75, 0.88, 0.15, 0.08]

print(f"Query: '{query}'\n")
for text, vec in embeddings.items():
    sim = compute_similarity(query_vec, vec)
    print(f"  Similarity to '{text}': {sim}")
