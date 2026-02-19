"""
Mini Project: Research Agent
Module 4 — AI Agents & Tool Use (Week 4)
Sprint 2: Build

Simulates an AI agent that uses tools to answer research questions.
"""
import json


class ResearchAgent:
    """An agent that uses tools to answer research questions."""

    def __init__(self):
        self.tools = {}
        self.memory = []
        self.max_steps = 5

    def register_tool(self, name: str, description: str, handler):
        self.tools[name] = {"description": description, "handler": handler}

    def think(self, question: str) -> list[dict]:
        """Plan which tools to use (simplified decision logic)."""
        plan = []
        q = question.lower()
        if any(w in q for w in ["calculate", "cost", "roi", "how much"]):
            plan.append({"tool": "calculator", "reason": "Needs numerical computation"})
        if any(w in q for w in ["search", "find", "what is", "who"]):
            plan.append({"tool": "search", "reason": "Needs information retrieval"})
        if any(w in q for w in ["summarize", "explain", "describe"]):
            plan.append({"tool": "summarize", "reason": "Needs text summarization"})
        return plan or [{"tool": "search", "reason": "Default to search"}]

    def execute(self, question: str) -> str:
        """Run the agent loop: think → act → observe."""
        self.memory.append({"role": "user", "content": question})
        plan = self.think(question)

        results = []
        for step in plan[:self.max_steps]:
            tool = self.tools.get(step["tool"])
            if tool:
                result = tool["handler"](question)
                results.append(f"[{step['tool']}]: {result}")
                self.memory.append({"role": "tool", "tool": step["tool"], "content": result})

        answer = f"Based on my research:\n" + "\n".join(results)
        self.memory.append({"role": "assistant", "content": answer})
        return answer


if __name__ == "__main__":
    agent = ResearchAgent()
    agent.register_tool("search", "Search knowledge base", lambda q: "AI market size: $200B by 2025")
    agent.register_tool("calculator", "Math operations", lambda q: "ROI: 280%")
    agent.register_tool("summarize", "Summarize text", lambda q: "AI adoption is accelerating across industries")

    answer = agent.execute("What is the ROI of AI investment and how much is the market worth?")
    print(answer)
    print(f"\nAgent memory: {len(agent.memory)} entries")
