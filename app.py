import streamlit as st
import requests

# Page settings
st.set_page_config(
    page_title="Ollama AI",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 Ollama AI Chatbot")
st.write("Powered by Llama 3.2 1B")

# User input
prompt = st.text_input(
    "Enter your question:",
    placeholder="Explain Python in simple terms"
)

# Ask button
if st.button("Ask AI"):

    if prompt:

        url = "http://localhost:11434/api/generate"

        data = {
            "model": "llama3.2:1b",
            "prompt": prompt,
            "stream": False
        }

        try:
            response = requests.post(
                url,
                json=data
            )

            result = response.json()

            if "response" in result:
                st.success("AI Response")
                st.write(result["response"])
            else:
                st.error(result.get("error", "Unknown error"))

        except Exception as e:
            st.error("Ollama is not running. Please start Ollama.")

    else:
        st.warning("Please enter a question.")