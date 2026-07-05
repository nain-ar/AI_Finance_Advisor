import streamlit as st

from modules.chat_boat import finance_chat

st.set_page_config(
    page_title="AI Finance Chat",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Finance Assistant")

st.caption("Ask anything about finance.")

# --------------------------
# Chat History
# --------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input

prompt = st.chat_input("Ask a finance question...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            reply = finance_chat(prompt)

            st.markdown(reply)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": reply
        }
    )

# --------------------------
# Clear Chat
# --------------------------

st.sidebar.title("Options")

if st.sidebar.button("🗑 Clear Chat"):

    st.session_state.messages = []

    st.rerun()