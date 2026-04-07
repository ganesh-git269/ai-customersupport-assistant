from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from inference import process_query, reset

app = FastAPI(title="AI Customer Support System")


class UserInput(BaseModel):
    user_input: str


# 🔥 Home Page
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


# 🔹 RESET
@app.post("/reset")
def reset_env():
    reset()
    return {"message": "Environment reset"}


# 🔹 STEP (OPENENV FORMAT)
@app.post("/step")
def step_env(input_data: UserInput):
    result = process_query(input_data.user_input)

    return {
        "observation": result,
        "reward": result["score"],
        "done": False,
        "info": {}
    }


# 🔹 STATE
@app.get("/state")
def state():
    return {"status": "running"}


def main():
    import uvicorn
    uvicorn.run("server.app:app", host="0.0.0.0", port=7860)


if __name__ == "__main__":
    main()
