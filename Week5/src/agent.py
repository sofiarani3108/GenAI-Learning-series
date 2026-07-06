import google.generativeai as genai
from src.config import GOOGLE_API_KEY, GEMINI_MODEL
from src.planner import plan_steps
from src.evaluator import evaluate_result
from src.query_rewriter import rewrite_query
from src.report_generator import generate_report

from src.tools.web_search import execute_web_search
from src.tools.document_search import execute_document_search
from src.tools.calculator import execute_calculator

genai.configure(api_key=GOOGLE_API_KEY)

def select_and_run_tool(query: str) -> tuple[str, str]:
    model = genai.GenerativeModel(
        model_name=GEMINI_MODEL,
        tools=[execute_web_search, execute_document_search, execute_calculator]
    )
    
    prompt = f"Use the appropriate tool to answer this query. If it's math, use execute_calculator. If it's about local documents, use execute_document_search. Otherwise use execute_web_search. Query: {query}"
    
    try:
        response = model.generate_content(prompt)
        
        if response.parts:
            for part in response.parts:
                if part.function_call:
                    func_name = part.function_call.name
                    
                    args = {}
                    for k, v in part.function_call.args.items():
                        args[k] = v
                        
                    if func_name == "execute_web_search":
                        return "Web Search", execute_web_search(**args)
                    elif func_name == "execute_document_search":
                        return "Document Search", execute_document_search(**args)
                    elif func_name == "execute_calculator":
                        return "Calculator", execute_calculator(**args)
                        
        return "Web Search (Fallback)", execute_web_search(query)
    except Exception as e:
        return "Error", str(e)

def run_agent(query: str, update_callback=None):
    def log(msg):
        if update_callback:
            update_callback(msg)
        else:
            print(msg)
            
    log("🧠 Planning steps...")
    steps = plan_steps(query)
    log(f"📋 Steps planned: {steps}")
    
    all_findings = []
    
    for i, step in enumerate(steps):
        log(f"\n🔄 Executing step {i+1}: {step}")
        
        current_query = step
        max_retries = 2
        success = False
        
        for attempt in range(max_retries):
            log(f"  Attempt {attempt+1}: Selecting tool for '{current_query}'...")
            tool_name, result = select_and_run_tool(current_query)
            log(f"  🔧 Used {tool_name}. Result length: {len(result)} chars")
            
            log("  ⚖️ Evaluating result...")
            is_good = evaluate_result(current_query, result)
            
            if is_good:
                log("  ✅ Result is sufficient.")
                all_findings.append(f"Step: {step}\nTool: {tool_name}\nResult: {result}")
                success = True
                break
            else:
                log("  ❌ Result insufficient.")
                if attempt < max_retries - 1:
                    log("  ✍️ Rewriting query...")
                    current_query = rewrite_query(current_query)
                    log(f"  🆕 New query: {current_query}")
                    
        if not success:
            log(f"  ⚠️ Failed to find good information for step {i+1} after retries.")
            all_findings.append(f"Step: {step}\nResult: No sufficient information found.")
            
    log("\n📝 Generating final report...")
    report = generate_report(query, all_findings)
    log("🎉 Report generated.")
    return report
