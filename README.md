# 🛳️ Titanic Dataset Chat Agent

A chatbot that answers questions about the famous **Titanic dataset** using **FastAPI**, **LangChain**, and **Streamlit**. Users can ask natural language questions and receive insightful responses with visualizations.

## 🚀 Features
✅ Accepts natural language questions  
✅ Returns clear text-based responses  
✅ Generates visual insights (charts, histograms, etc.)  
✅ Simple and interactive Streamlit frontend  

---

## 📌 Tech Stack
- **Backend:** FastAPI
- **Agent Framework:** LangChain
- **Frontend:** Streamlit
- **Data Processing:** Pandas, Matplotlib, Seaborn

---

## 🔧 Setup Instructions

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/your-username/titanic-chatbot.git
cd titanic-chatbot


python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows

# Install Dependencies
pip install -r requirements.txt

# Run the FastAPI Backend
uvicorn backend.main:app --reload --port 8080

Backend will start at: http://127.0.0.1:8080
You can test API using http://127.0.0.1:8080/docs

#Run the Streamlit Frontend
streamlit run app.py

Frontend will be accessible at: http://localhost:8501
