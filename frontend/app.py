import streamlit as st
import requests

st.title("🚢 Titanic Chat Agent")
st.write("Ask me about the Titanic dataset!")

query = st.text_input("Enter your question:")
if st.button("Ask"):
    if query:
        response = requests.post("http://127.0.0.1:8080/query/", json={"query": query})
        result = response.json()
        st.write(result["response"])
