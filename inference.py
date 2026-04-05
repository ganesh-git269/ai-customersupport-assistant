import random


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

    if "urgent" in text or "immediately" in text or "money" in text or "delay"  in text or "order" in text or "refund" in text:
        return "high"

    elif   "late" in text:
        return "medium"

    else:
        return "low"


# 🔹 Smart Scoring (FINAL FIX)
def calculate_score(response_text):
    text = response_text.lower()

    # ❌ Bad responses
    bad_words = [
        "not sure",
        "don't know",
        "cannot",
        "unable",
        "provide more details"
    ]

    for word in bad_words:
        if word in text:
            return -1

    # ✅ Good responses
    good_words = [
        "successfully",
        "initiated",
        "processed",
        "resolved",
        "will",
        "assist",
        "help"
    ]

    for word in good_words:
        if word in text:
            return 1

    # ⚖️ Neutral → based on length
    if len(text) > 60:
        return 1
    else:
        return -1


# 🔹 Main Function
def process_query(user_input):
    response = get_ai_response(user_input)
    category = classify_category(user_input)
    priority = assign_priority(user_input)
    score = calculate_score(response)

    return {
        "input": user_input,
        "category": category,
        "priority": priority,
        "response": response,
        "score": score
    }