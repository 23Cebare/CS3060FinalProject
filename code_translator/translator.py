import requests
import ast

OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama2"


# Optional: Add validators for other languages if needed

import re

def clean_code_output(output, language):
    code = output.strip()
    # Try to extract code from a code block (``` ... ```)
    code_block = re.search(r'```[a-zA-Z]*\n([\s\S]*?)```', code)
    if code_block:
        code = code_block.group(1).strip()
    else:
        # Remove lines before the first 'import' or 'def' or class for Python
        if language.lower() == 'python':
            lines = code.splitlines()
            for i, line in enumerate(lines):
                if line.strip().startswith(('import ', 'def ', 'class ')):
                    code = '\n'.join(lines[i:])
                    break
    return code

def is_valid_code(code, language):
    if language.lower() == "python":
        try:
            ast.parse(code)
            return True
        except SyntaxError:
            return False
    # For other languages, skip validation or add more logic
    return True




def translate_code(source_code, source_language, target_language):
    prompt = (
        "You are a code translation agent.\n"
        f"If the input is not valid {source_language} code, reply with 'ERROR: This is not code.'\n"
        f"If the input IS code, then translate it strictly from {source_language} to {target_language}. "
        f"Only output valid {target_language} code, no explanations or comments. "
        f"Output ONLY a code block in this format:\n"
        f"```{target_language.lower()}\n<code>\n``` and nothing else. "
        "If the input code is incomplete or ambiguous, reply with 'ERROR: Please clarify the input.' "
        "If translation is not possible, reply with 'ERROR: Cannot translate this code.'\n\n"
        f"{source_language} code:\n{source_code}\n\n{target_language} code:"
    )
    response = requests.post(OLLAMA_API_URL, json={
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    })
    result = response.json()
    raw_output = result.get("response", "").strip()
    cleaned_output = clean_code_output(raw_output, target_language)

    # If the cleaned output is empty or looks like the source code, error out
    if not cleaned_output or cleaned_output.strip() == source_code.strip():
        return f"ERROR: No translation to {target_language} was found.\n\nRaw output from LLM:\n{raw_output}"

    # Agent post-processing: Validate code if possible
    if cleaned_output.startswith("ERROR"):
        return cleaned_output
    if not is_valid_code(cleaned_output, target_language):
        # Show raw output for debugging
        return f"ERROR: Output is not valid {target_language} code.\n\nRaw output from LLM:\n{raw_output}"
    return cleaned_output
