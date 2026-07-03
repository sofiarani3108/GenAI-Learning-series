import google.generativeai as genai
import json
from src.config import GEMINI_MODEL

def plan_steps(query: str):
    model = genai.GenerativeModel(GEMINI_MODEL)
    prompt = f"""
    You are an AI planner. Break down the user's research query into a list of 1-3 simple retrieval steps.
    Each step should be a clear question or action.
    Return ONLY a JSON array of strings. No markdown formatting.
    Query: {query}
    """
    try:
        res = model.generate_content(prompt)
        text = res.text.replace('```json', '').replace('```', '').strip()
        steps = json.loads(text)
        return steps
    except Exception as e:
        print(f"Planner error: {e}")
        return [query]
