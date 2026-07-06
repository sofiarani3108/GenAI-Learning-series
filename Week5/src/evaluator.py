import google.generativeai as genai
from src.config import GEMINI_MODEL

def evaluate_result(query: str, result: str) -> bool:
    if not result or "Error" in result or "No relevant" in result or "No web search results" in result:
        return False
        
    model = genai.GenerativeModel(GEMINI_MODEL)
    prompt = f"""
    You are an evaluator. Does the following context contain the answer or useful information for the query?
    Answer ONLY 'YES' or 'NO'.
    Query: {query}
    Context: {result}
    """
    try:
        res = model.generate_content(prompt)
        return "YES" in res.text.upper()
    except:
        return True
