import random

def run(user_input: str):
    text = user_input.lower()

    # 🔹 Response
    if "refund" in text:
        response = "Your refund request has been initiated."
    elif "order" in text and "delay" in text:
        response = "Sorry for the delay. Your order is on the way."
    elif "order" in text:
        response = "Your order has been placed successfully."
    elif "password" in text or "login" in text:
        response = "You can reset your password using the forgot password option."
    elif "payment" in text:
        response = "Your payment was successful."
    else:
        response = random.choice([
            "Not sure, please provide more details.",
            "I don't understand your query.",
            "Please explain your issue clearly."
        ])

    # 🔹 Category
    if "refund" in text or "payment" in text:
        category = "billing"
    elif "order" in text:
        category = "order"
    elif "password" in text or "login" in text:
        category = "account"
    else:
        category = "general"

    # 🔹 Priority
    if "urgent" in text or "delay" in text or "refund" in text:
        priority = "high"
    elif "late" in text:
        priority = "medium"
    else:
        priority = "low"

    # 🔹 Score
    if "not sure" in response.lower() or "don't understand" in response.lower():
        score = -1
    else:
        score = 1

    return {
        "response": response,
        "category": category,
        "priority": priority,
        "score": score
    }
