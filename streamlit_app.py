import streamlit as st
from inference import process_query
st.set_page_config(
    page_title="AI Support Assistant",
    page_icon="🤖"
)

st.title("🤖 AI Customer Support")
st.write("Ask your question and get instant help.")
# User input
user_input = st.text_input("Type your query here:")
# Button click action
if st.button("Get Response"):

    if user_input.strip() == "":
        st.warning("Please enter something first.")
    else:
        result = process_query(user_input)

        st.divider()
        # Show response
        st.subheader("Response")
        st.write(result["response"])
        # Show details
        st.subheader("Details")

        col1, col2, col3 = st.columns(3)

        col1.write(f"**Category:** {result['category']}")
        col2.write(f"**Priority:** {result['priority']}")

        if result["score"] == 1:
            col3.write("**Score:** +1 ✅")
        else:
            col3.write("**Score:** -1 ❌")