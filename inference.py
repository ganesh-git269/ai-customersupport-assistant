import os
import random

# 🔹 Environment Variables
API_BASE_URL = os.getenv("API_BASE_URL", "")
MODEL_NAME = os.getenv("MODEL_NAME", "")
HF_TOKEN = os.getenv("HF_TOKEN")

# 🔹 Global State
state = {}

# 🔹 Reset Function
def reset():
    global state
    print("START")

    state = {
        "input": "",
        "response": "",
        "category": "",
        "priority": "",
        "score": 0
    }

    print("END")
    return state


# 🔹 AI Response Generator
def get_ai_response(user_input):
    text = user_input.lower()

    if "refund" in text:
        return "Your refund request has been successfully initiated. You will receive the amount within 3-5 business days."

    elif "order" in text and "delay" in text:
        return "We apologize for the delay. Your order is on the way and will reach you soon."

    elif "order" in text:
        return "Your order has been placed successfully and is being processed."

    elif "password" in text or "login" in text:
        return "You can reset your password using the 'Forgot Password' option on the login page."

    elif "payment" in text:
        return "Your payment was successful. If any issue persists, please contact support."

    else:
        responses = [
            "I'm not sure about that. Could you please provide more details?",
            "I don't have enough information to help with this.",
            "Not sure how to answer that. Please clarify your question.",
            "Please explain your concern so we can assist better."
        ]
        return random.choice(responses)


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


# 🔥 MAIN FUNCTION (IMPORTANT)
def process_query(user_input):
    global state

    print("START")

    state["input"] = user_input

    print("STEP: Generating response")
    response = get_ai_response(user_input)

    print("STEP: Classifying category")
    category = classify_category(user_input)

    print("STEP: Assigning priority")
    priority = assign_priority(user_input)

    print("STEP: Calculating score")
    score = calculate_score(response)

    state.update({
        "response": response,
        "category": category,
        "priority": priority,
        "score": score
    })

    print("END")

    return state
