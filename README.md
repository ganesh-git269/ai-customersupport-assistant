🤖 AI Customer Support Assistant (OpenEnv Compatible)

📌 Overview

This project is a simple AI-powered customer support system that simulates real-world customer queries and generates automated responses. It is built following the OpenEnv specification, making it suitable for environments like the Scalar Hackathon.

The system processes user queries, classifies them, assigns priority, generates responses, and evaluates the response quality.

---

🚀 Features

- 🔹 AI-like response generation (rule-based simulation)
- 🔹 Query classification (billing, order, account, general)
- 🔹 Priority assignment (high, medium, low)
- 🔹 Response evaluation with reward scoring (+1 / -1)
- 🔹 OpenEnv compliant API:
  - "/reset"
  - "/step"
  - "/state"

---

🧠 How It Works

1. User sends a query
2. System:
   - Generates response
   - Classifies category
   - Assigns priority
   - Calculates reward score
3. Returns structured output in OpenEnv format

---

📂 Project Structure

.
├── inference.py
├── Dockerfile
├── requirements.txt
├── pyproject.toml
├── uv.lock
└── server/
    └── app.py

---

⚙️ Installation & Run (Local)

Step 1: Install dependencies

pip install fastapi uvicorn pydantic openenv-core

Step 2: Run server

python -m uvicorn server.app:app --reload

Step 3: Open API Docs

http://127.0.0.1:8000/docs

---

📡 API Endpoints

🔹 Reset Environment

"POST /reset"

Resets the system state.

---

🔹 Step Execution

"POST /step"

Request:

{
  "user_input": "refund my money"
}

Response:

{
  "observation": {
    "input": "refund my money",
    "category": "billing",
    "priority": "high",
    "response": "Your refund request has been successfully initiated.",
    "score": 1
  },
  "reward": 1,
  "done": false,
  "info": {}
}

---

🔹 Get State

"GET /state"

Returns current environment status.

---

🎯 Scoring Logic

- ✅ +1 → Helpful / confident responses
- ❌ -1 → Uncertain / unclear responses

---

🛠️ Tech Stack

- Python
- FastAPI
- Uvicorn
- Pydantic
- OpenEnv

---

🌐 Deployment

This project is deployed using:

- Hugging Face Spaces (Docker)
- GitHub Repository

---

📌 Use Case

This system simulates real-world tasks like:

- Customer support automation
- Query classification
- AI response evaluation

---

🙌 Conclusion

This project demonstrates how AI-based systems can automate customer support tasks while following standardized environment protocols like OpenEnv.

---

🔗 Links

- GitHub Repo: (Add your link here)
- Hugging Face Space: (Add your link here)

---
