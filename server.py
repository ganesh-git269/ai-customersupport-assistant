from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from inference import run

# ✅ IMPORTANT: app must be named 'app'
app = FastAPI(title="AI Customer Support System")


# 🔹 Input model
class UserInput(BaseModel):
    user_input: str


# 🔥 Home page
@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
        <body style="text-align:center; font-family:Arial;">
            <h1>🤖 AI Customer Support System</h1>

            <br>

            <a href="/docs">
                <button style="padding:10px 20px;">API Docs</button>
            </a>

            <br><br>

            <a href="https://github.com/ganesh-git269/ai-customersupport-assistant">
                <button style="padding:10px 20px;">GitHub Repo</button>
            </a>
        </body>
    </html>
    """


# 🔹 Reset endpoint
@app.post("/reset")
def reset():
    return {"message": "Environment reset successful"}


# 🔹 Step endpoint
@app.post("/step")
def step(input_data: UserInput):
    result = run(input_data.user_input)
    return result


# 🔹 State endpoint
@app.get("/state")
def state():
    return {"status": "running"}
