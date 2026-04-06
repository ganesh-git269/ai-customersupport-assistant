import streamlit as st
from inference import process_query  # 🔥 correct import

# 🔹 Page config
st.set_page_config(page_title="AI Customer Support", page_icon="🤖", layout="centered")

# 🔹 Title
st.title("🤖 AI Customer Support System")
st.markdown("Enter your query and get AI-generated response with category, priority, and score.")

# 🔹 Input box
user_input = st.text_input("💬 Enter your query:")

# 🔹 Button
if st.button("Submit"):

    if user_input.strip() == "":
        st.warning("⚠️ Please enter a query")
    else:
        try:
            # 🔥 Direct function call (NO FastAPI)
            data = process_query(user_input)

            # 🔹 Display results
            st.subheader("📊 Results")

            st.success(f"🤖 Response: {data['response']}")
            st.info(f"📂 Category: {data['category']}")
            st.warning(f"⚡ Priority: {data['priority']}")

            # 🔹 Score display
            if data["score"] == 1:
                st.success(f"✅ Score: {data['score']} (Good Response)")
            else:
                st.error(f"❌ Score: {data['score']} (Needs Improvement)")

        except Exception as e:
            st.error(f"🚫 Error: {str(e)}")

# 🔹 Footer
st.markdown("---")
st.caption("Built using Streamlit + Custom AI Logic")
