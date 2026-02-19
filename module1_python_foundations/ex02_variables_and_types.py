"""
Exercise 2: Python Variables & Data Types for AI
Module 1 — Python & AI Foundations
Sprint 1: Foundation (Day 2)

Task: Create variables to model an AI project evaluation.
"""

project_name = "Customer Support Chatbot"
estimated_cost = 45000.00
expected_roi_percent = 280
team_size = 4
uses_llm = True
tech_stack = ["Python", "LangChain", "OpenAI", "FastAPI"]

print(f"Project: {project_name}")
print(f"Cost: ${estimated_cost:,.2f}")
print(f"Expected ROI: {expected_roi_percent}%")
print(f"Team size: {team_size}")
print(f"Uses LLM: {uses_llm}")
print(f"Tech stack: {', '.join(tech_stack)}")

# Type checking (bridge from Java's strict typing)
print(f"\n--- Type Check (for Java devs) ---")
print(f"project_name: {type(project_name).__name__} (like String in Java)")
print(f"estimated_cost: {type(estimated_cost).__name__} (like double)")
print(f"team_size: {type(team_size).__name__} (like int)")
print(f"uses_llm: {type(uses_llm).__name__} (like boolean)")
print(f"tech_stack: {type(tech_stack).__name__} (like ArrayList<String>)")
