import streamlit as st
import google.generativeai as genai

# Set Gemini API key
# filepath: c:\Users\shubh\OneDrive\Desktop\cr\app.py
# ...existing code...
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
# ...existing code...

st.title("🤖 Code Reviewer & Explainer")

code_input = st.text_area("Paste your Python code here", height=300)

if st.button("Review Code"):
    if not code_input.strip():
        st.warning("Please paste some code!")
    else:
        with st.spinner("Analyzing your code..."):
            prompt = f"""
            You are a helpful programming assistant.
            Analyze the following Python code and:
            1. Explain what the code does in simple language.
            2. Identify any bugs or issues.
            3. Suggest improvements or best practices.

            Code:
            {code_input}

            Provide your answer as a detailed report.
            """
            try:
                model = genai.GenerativeModel("gemini-1.5-flash")
                response = model.generate_content(prompt)
                st.markdown("### Review & Explanation:")
                st.write(response.text)
            except Exception as e:
                st.error("Error communicating with API. Please check your API key and model name.")