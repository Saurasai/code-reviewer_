import google.generativeai as genai

# Configure Gemini once at import time
def configure_gemini(api_key: str):
    if not getattr(configure_gemini, "configured", False):
        genai.configure(api_key=api_key)
        configure_gemini.configured = True

def analyze_code(code: str, api_key: str) -> str:
    configure_gemini(api_key)
    prompt = f"""
    You are a helpful programming assistant.
    Analyze the following Python code and:
    1. Explain what the code does in simple language.
    2. Identify any bugs or issues.
    3. Suggest improvements or best practices.
    4. At the end , provide a summary in hinglish with real life example

    Code:
    {code}

    Provide your answer as a detailed report.
    """
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error communicating with API: {e}"