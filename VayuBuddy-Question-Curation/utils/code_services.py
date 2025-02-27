from pathlib import Path
import os
import subprocess

def execute_code(code_content):
    """Executes the given Python code and returns output/errors."""
    temp_path = "temp_code.py"
    Path(temp_path).write_text(code_content, encoding="utf-8")
    
    try:
        output = subprocess.check_output(["python", temp_path], stderr=subprocess.STDOUT, text=True)
        os.remove(temp_path)
        return output, None
    except subprocess.CalledProcessError as e:
        os.remove(temp_path)
        return None, e.output
    

def format_code(user_code):
    if user_code.strip().startswith("def true_code()"):
        return user_code
    else:
        return f"def true_code():\n    " + "\n    ".join(user_code.splitlines()) + "\n\ntrue_code()"  # Wrap in function
