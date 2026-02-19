"""
Capstone Project: AI Career Assistant
Module 6 — Portfolio & Job Prep (Week 4)
Sprint 3: Launch

The final portfolio piece — an AI-powered career transition assistant
that combines everything learned across all 6 modules.
"""
import json


class AICareerAssistant:
    """
    Combines all skills from the 90-day sprint:
    - Module 1: Python fundamentals
    - Module 2: Prompt engineering
    - Module 3: RAG-style knowledge retrieval
    - Module 4: Agent-style tool use
    - Module 5: API design patterns
    - Module 6: Putting it all together
    """

    def __init__(self, user_background: str, target_role: str):
        self.user_background = user_background
        self.target_role = target_role
        self.knowledge_base = self._build_knowledge_base()
        self.conversation_history = []

    def _build_knowledge_base(self) -> list[dict]:
        """Module 3 skill: Build a searchable knowledge base."""
        return [
            {"topic": "resume", "content": f"Highlight {self.user_background} experience. Show AI projects."},
            {"topic": "interview", "content": f"For {self.target_role}: expect system design + coding + AI concepts."},
            {"topic": "portfolio", "content": "GitHub repos with README, working code, and deployment guides."},
            {"topic": "networking", "content": "Join AI meetups, contribute to open source, write blog posts."},
            {"topic": "salary", "content": f"{self.target_role} roles: $120k-$200k depending on experience."},
        ]

    def search_knowledge(self, query: str) -> list[dict]:
        """Module 3 skill: Retrieve relevant knowledge."""
        query_words = set(query.lower().split())
        scored = []
        for entry in self.knowledge_base:
            text_words = set(f"{entry['topic']} {entry['content']}".lower().split())
            overlap = len(query_words & text_words)
            if overlap > 0:
                scored.append({**entry, "relevance": overlap})
        return sorted(scored, key=lambda x: -x["relevance"])[:3]

    def generate_advice(self, question: str) -> str:
        """Module 2 + 4 skill: Generate personalized advice."""
        context = self.search_knowledge(question)
        context_text = "\n".join(f"- {c['content']}" for c in context)

        prompt = f"""As an AI career advisor for a {self.user_background} transitioning to {self.target_role}:

Question: {question}

Relevant context:
{context_text}

Provide specific, actionable advice:"""

        self.conversation_history.append({"role": "user", "content": question})
        response = f"Based on your {self.user_background} background targeting {self.target_role}:\n"
        for c in context:
            response += f"  → {c['content']}\n"
        self.conversation_history.append({"role": "assistant", "content": response})
        return response

    def get_status(self) -> dict:
        """Module 5 skill: API-style status endpoint."""
        return {
            "user_background": self.user_background,
            "target_role": self.target_role,
            "knowledge_entries": len(self.knowledge_base),
            "conversation_turns": len(self.conversation_history),
        }


if __name__ == "__main__":
    assistant = AICareerAssistant(
        user_background="Java/Spring Developer (8 years)",
        target_role="LLM Developer"
    )

    questions = [
        "How should I update my resume?",
        "What salary can I expect?",
        "How do I prepare for interviews?",
    ]

    for q in questions:
        print(f"Q: {q}")
        print(assistant.generate_advice(q))
        print()

    print(f"Session status: {json.dumps(assistant.get_status(), indent=2)}")
