import google.generativeai as genai
from src.config import GEMINI_MODEL

def generate_report(query: str, findings: list) -> str:
    model = genai.GenerativeModel(GEMINI_MODEL)
    
    context = "\n\n".join([f"Finding {i+1}:\n{f}" for i, f in enumerate(findings)])
    prompt = f"""
    You are an expert research assistant. 
    Write a comprehensive, final report answering the user's original query based ONLY on the provided findings.
    Use Markdown formatting. Include citations/references to the findings where appropriate.
    If the findings do not fully answer the query, state what is missing.
    
    User Query: {query}
    
    Findings:
    {context}
    """
    try:
        res = model.generate_content(prompt)
        return res.text
    except Exception as e:
        return f"Error generating report: {e}"
