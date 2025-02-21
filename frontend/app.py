import streamlit as st
import requests

# Set your deployed backend URL here
BACKEND_URL = "https://titnaicchatbot.onrender.com/query"  # Replace with your actual deployed FastAPI URL

st.title("🚢 Titanic Chat Agent")
st.write("Ask me about the Titanic dataset!")

query = st.text_input("Enter your question:")
if st.button("Ask"):
    if query:
        try:
            response = requests.post(BACKEND_URL, json={"query": query}, timeout=10)
            response.raise_for_status()  # Raise an error if the response is not 200 OK
            result = response.json()
            st.write(result.get("response", "No response from the server."))
        except requests.exceptions.RequestException as e:
            st.error(f"Error: Unable to connect to backend. {e}")
