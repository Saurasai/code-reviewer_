# 🤖 AI Code Reviewer & Explainer (Powered by Google Gemini)

A GenAI-powered tool that intelligently **analyzes Python code**, explains it in plain language, detects bugs, and suggests improvements — all using **LLMs (Large Language Models)** and prompt engineering via **Google’s Gemini API**.

---

## 🌟 Key Features

- 🔍 **Code Understanding**: Uses a generative LLM to deeply understand Python code
- 🧠 **Explainability**: Converts code logic into simple human-readable explanations
- 🐞 **Bug Detection**: Finds logical or syntax issues using natural language reasoning
- 💡 **Best Practice Suggestions**: Suggests cleaner, more efficient Python code
- ✨ **Powered by GenAI**: Uses Google's Gemini (`gemini-1.5-flash`) model

---

📌 How It Works
The app sends your code to Google's Gemini LLM, along with a custom-designed prompt using prompt engineering principles.

The LLM returns a response including:

Code functionality summary

Bug detection results

Refactoring or improvement advice




## 🧠 Technologies Used

| Tech          | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| `Streamlit`   | Fast, Python-based UI framework for building web apps                      |
| `Google Gemini` | Generative AI model from Google for advanced code analysis & NLP tasks    |
| `LLM`         | Large Language Models understand and generate human-like explanations       |
| `Prompt Engineering` | Structured input prompts to steer model responses                   |
| `Python`      | Core programming language for backend and model communication               |

---

## 📂 Folder Structure


AI_Code_Reviewer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── .streamlit/
└── secrets.toml

