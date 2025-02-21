from fastapi import FastAPI
from backend.models import QueryRequest
from backend.query_handler import process_query

app = FastAPI()

# Add a default route for root URL
@app.get("/")
async def root():
    return {"message": "Titanic Chatbot API is running!"}

@app.post("/query")
async def handle_query(request: QueryRequest):
    response = process_query(request.query)
    return {"response": response}
