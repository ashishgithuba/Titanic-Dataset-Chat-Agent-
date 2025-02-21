from fastapi import FastAPI
from backend.models import QueryRequest
from backend.query_handler import process_query

app = FastAPI()

@app.post("/query")
async def handle_query(request: QueryRequest):
    response = process_query(request.query)
    return {"response": response}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.main:app", host="127.0.0.1", port=8000, reload=True)
