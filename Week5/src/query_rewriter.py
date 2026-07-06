import google.generativeai as genai
from src.config import GEMINI_MODEL

def rewrite_query(query: str) -> str:
    model = genai.GenerativeModel(GEMINI_MODEL)
    prompt = f"""
    The previous search for the query '{query}' failed to find good results.
    Rewrite the query to be simpler or use different keywords to improve search results.
    Return ONLY the new query string.
    """
    try:
        res = model.generate_content(prompt)
        return res.text.strip()
    except:
        return query
