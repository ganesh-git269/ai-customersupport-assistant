🤖 AI Customer Support Assistant (OpenEnv Project)

📌 Overview

This project is an AI-powered customer support system designed to simulate real-world customer service tasks.
It can understand user queries, generate meaningful responses, classify the issue, assign priority, and evaluate the response quality.

---

🎯 Problem Statement

Customer support teams handle a large number of repetitive queries daily.
This project automates that process using AI to:

- Respond instantly to user queries
- Categorize issues
- Prioritize requests
- Evaluate response quality

---

🚀 Features

- 🧠 AI-generated human-like responses
- 📂 Automatic category classification
- ⚡ Priority assignment (High / Medium / Low)
- 📊 Response evaluation with scoring (+1 / -1)
- 💻 Interactive UI using Streamlit

---

🧠 OpenEnv Implementation

🔹 Task

AI-based Customer Support Assistant

🔹 Observation

User input (customer query)

🔹 Action

System generates:

- Response to the query
- Category (billing, order, account, general)
- Priority level

🔹 Reward

Score based on response quality:

- +1 → Helpful / polite response
- -1 → Generic / unclear response

---

🛠️ Tech Stack

- Python
- FastAPI (Backend API)
- Streamlit (Frontend UI)

---

📁 Project Structure

ai-support-assistant/
│
├── inference.py        # AI logic
├── server.py           # FastAPI backend
├── streamlit_app.py    # User interface
├── requirements.txt    # Dependencies
├── README.md           # Documentation
└── .gitignore          # Ignore unnecessary files

---

⚙️ Installation & Setup

1️⃣ Install dependencies

pip install -r requirements.txt

2️⃣ Run backend server

uvicorn server:app --reload

3️⃣ Run frontend UI

streamlit run streamlit_app.py

---

🌐 How It Works

1. User enters a query in the UI
2. Backend processes the query
3. AI generates a response
4. System classifies category & priority
5. Score is assigned (+1 / -1)
6. Results are displayed to the user


✅ Example Output

- Input: "My order is delayed"
- Category: Order
- Priority: Medium
- Response: "We apologize for the delay..."
- Score: +1

- 
🔥 Conclusion
This project demonstrates how AI can be used to automate customer support tasks efficiently while maintaining response quality and structured evaluation using OpenEnv principles.
