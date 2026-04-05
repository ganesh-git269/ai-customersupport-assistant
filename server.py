from fastapi import FastAPI
from inference import process_query
from pydantic import BaseModel


app = FastAPI()


# 🔹 Create input model (THIS FIXES YOUR PROBLEM)
class Query(BaseModel):
    input: str


@app.get("/")
def home():
    return {"message": "Server is running"}


@app.post("/run")
def run_ai(data: Query):
    return process_query(data.input)