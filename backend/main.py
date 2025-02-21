import os
import uvicorn
from fastapi import FastAPI
from backend.models import QueryRequest
from backend.query_handler import process_query

app = FastAPI()

@app.post("/query")
async def handle_query(request: QueryRequest):
    response = process_query(request.query)
    return {"response": response}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Use PORT from environment if deploying
    uvicorn.run("backend.main:app", host="0.0.0.0", port=port)
