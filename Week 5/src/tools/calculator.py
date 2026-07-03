import re

def execute_calculator(expression: str) -> str:
    """
    Evaluates a mathematical expression.
    Example: execute_calculator("2 + 2 * 3") -> "8"
    """
    try:
        # Strip out anything that isn't a number, operator, or parenthesis for safety
        clean_expr = re.sub(r'[^0-9\+\-\*\/\(\)\.\s]', '', str(expression))
        
        if not clean_expr.strip():
            return "Error: Empty or invalid expression."
            
        result = eval(clean_expr, {"__builtins__": None}, {})
        return str(result)
    except Exception as e:
        return f"Error evaluating expression '{expression}': {str(e)}"
