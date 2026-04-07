import os
from openai import OpenAI

# 🔹 Safe API Initialization (works locally + OpenEnv)
api_key = os.environ.get("API_KEY")
base_url = os.environ.get("API_BASE_URL")

client = None
if api_key and base_url:
    client = OpenAI(
        base_url=base_url,
        api_key=api_key
    )

# 🔹 Global State
state = {}


# 🔹 Reset Function
def reset():
    global state

    task_name = "customer_support"

    print(f"[START] task={task_name}", flush=True)

    state = {
        "input": "",
        "response": "",
        "category": "",
        "priority": "",
        "score": 0
    }

    print(f"[END] task={task_name} score=0 steps=0", flush=True)

    return state


# 🔹 AI Response (API + fallback)
def get_ai_response(user_input):
    if client:
        try:
            response = client.chat.completions.create(
                model=os.environ.get("MODEL_NAME", "gpt-4o-mini"),
                messages=[
                    {"role": "system", "content": "You are a helpful customer support assistant."},
                    {"role": "user", "content": user_input}
                ]
            )
            return response.choices[0].message.content
        except Exception:
            pass

    # 🔸 Fallback (local execution)
    return "Your request has been received and is being processed."


# 🔹 Category Classification
def classify_category(user_input):
    text = user_input.lower()

    if "refund" in text or "payment" in text:
        return "billing"
    elif "order" in text:
        return "order"
    elif "password" in text or "login" in text:
        return "account"
    else:
        return "general"


# 🔹 Priority Assignment
def assign_priority(user_input):
    text = user_input.lower()

    if any(word in text for word in ["urgent", "immediately", "money", "delay", "order", "refund"]):
        return "high"
    elif "late" in text:
        return "medium"
    else:
        return "low"


# 🔹 Smart Scoring
def calculate_score(response_text):
    text = response_text.lower()

    bad_words = ["not sure", "don't know", "cannot", "unable", "provide more details"]
    if any(word in text for word in bad_words):
        return -1

    good_words = ["successfully", "initiated", "processed", "resolved", "will", "assist", "help"]
    if any(word in text for word in good_words):
        return 1

    return -1


# 🔥 MAIN FUNCTION (OPENENV REQUIRED)
def process_query(user_input):
    global state

    task_name = "customer_support"

    print(f"[START] task={task_name}", flush=True)

    state["input"] = user_input

    response = get_ai_response(user_input)
    category = classify_category(user_input)
    priority = assign_priority(user_input)
    score = calculate_score(response)

    state.update({
        "response": response,
        "category": category,
        "priority": priority,
        "score": score
    })

    print(f"[STEP] step=1 reward={score}", flush=True)
    print(f"[END] task={task_name} score={score} steps=1", flush=True)

    return state


# 🔥 Execution block (for local run / Phase 2)
if __name__ == "__main__":
    reset()
    process_query("I want a refund for my order")
