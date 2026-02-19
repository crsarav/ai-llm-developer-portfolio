"""
Mini Project: Document Q&A System (RAG Pipeline)
Module 3 — RAG & Vector Databases (Week 4)
Sprint 2: Build

Simulates a complete RAG pipeline: chunk → embed → search → answer.
"""
import math
import json


def chunk_text(text: str, chunk_size: int = 200, overlap: int = 50) -> list[str]:
    """Split text into overlapping chunks for embedding."""
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size - overlap):
        chunk = " ".join(words[i:i + chunk_size])
        if chunk.strip():
            chunks.append(chunk.strip())
    return chunks


def simple_embed(text: str) -> list[float]:
    """Simplified embedding (hash-based, for demo purposes)."""
    words = text.lower().split()
    vec = [0.0] * 8
    for i, word in enumerate(words):
        idx = hash(word) % 8
        vec[idx] += 1.0 / (i + 1)
    magnitude = math.sqrt(sum(v ** 2 for v in vec)) or 1.0
    return [round(v / magnitude, 4) for v in vec]


def cosine_similarity(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    mag_a = math.sqrt(sum(x ** 2 for x in a))
    mag_b = math.sqrt(sum(x ** 2 for x in b))
    return dot / (mag_a * mag_b) if mag_a and mag_b else 0.0


def search(query: str, documents: list[dict], top_k: int = 3) -> list[dict]:
    """Search documents by embedding similarity."""
    query_emb = simple_embed(query)
    scored = []
    for doc in documents:
        sim = cosine_similarity(query_emb, doc["embedding"])
        scored.append({**doc, "score": round(sim, 4)})
    return sorted(scored, key=lambda x: -x["score"])[:top_k]


if __name__ == "__main__":
    knowledge_base = """
    Large Language Models (LLMs) are neural networks trained on vast amounts of text.
    They can generate human-like text, answer questions, and assist with coding.
    RAG (Retrieval Augmented Generation) combines LLMs with external knowledge bases.
    Instead of relying solely on training data, RAG retrieves relevant documents first,
    then passes them as context to the LLM for more accurate answers.
    Vector databases store text as numerical embeddings for fast similarity search.
    Popular vector databases include ChromaDB, Pinecone, Weaviate, and Qdrant.
    The embedding process converts text into high-dimensional vectors that capture meaning.
    """

    chunks = chunk_text(knowledge_base, chunk_size=30, overlap=5)
    documents = [{"text": c, "embedding": simple_embed(c)} for c in chunks]

    query = "How does RAG work with vector databases?"
    results = search(query, documents)

    print(f"Query: {query}\n")
    print("Top results:")
    for i, r in enumerate(results):
        print(f"  {i+1}. (score: {r['score']}) {r['text'][:100]}...")
