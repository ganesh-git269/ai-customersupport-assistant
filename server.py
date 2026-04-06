from fastapi import FastAPI
from pydantic import BaseModel
from inference import reset, step, state

app = FastAPI(title="CustomerSupportEnv")


# 🔹 Input schema for step
class UserInput(BaseModel):
    user_input: str


# 🔹 Home route
@app.get("/web")
def home():
    return {"message": "Customer Support Environment Running"}


# 🔹 Reset API
@app.post("/reset")
def reset_env():
    return reset()


# 🔹 Step API
@app.post("/step")
def step_env(input_data: UserInput):
    return step(input_data.user_input)


# 🔹 Get current state
@app.get("/state")
def get_state():
    return state


# 🔹 Health check
@app.get("/health")
def health():
    return {"status": "ok"}
