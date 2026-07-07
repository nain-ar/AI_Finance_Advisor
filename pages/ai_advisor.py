import streamlit as st
from modules.expense_manager import ExpenseManager
from modules.chat_boat import finance_chat


def show_ai_advisor():

    # ===============================
    # Login Check
    # ===============================

    if not st.session_state.get("logged_in", False):
        st.session_state.page = "login"
        st.rerun()

    expense_manager = ExpenseManager()

    USER_ID = st.session_state["user_id"]

    # ===============================
    # CSS
    # ===============================

    st.markdown("""
    <style>

    <style>

.stApp{
    background: #A8DCAB;
}

/* Hide Streamlit Menu */
#MainMenu{
    visibility:hidden;
}

header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

/* Title */

.title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#1B4332;
}

/* Subtitle */

.subtitle{
    text-align:center;
    color:#4F6F52;
    margin-bottom:25px;
}

/* Cards */

div[data-testid="stMetric"]{
    background:white;
    border-radius:18px;
    padding:18px;
    border:1px solid #D8EFD3;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
}

/* Buttons */

.stButton>button{
    width:100%;
    background:#2E7D32;
    color:white;
    border:none;
    border-radius:12px;
    font-weight:600;
    height:45px;
}

.stButton>button:hover{
    background:#388E3C;
}

/* Text Input */

.stTextInput input,
.stNumberInput input,
.stDateInput input,
textarea{
    border-radius:10px;
    border:1px solid #B7D9B5;
}

/* Select Box */

.stSelectbox div{
    border-radius:10px;
}

/* DataFrame */

[data-testid="stDataFrame"]{
    border-radius:15px;
    background:white;
}



    </style>
    """, unsafe_allow_html=True)

    # ===============================
    # Header
    # ===============================

    st.markdown(
        '<div class="title">🤖 AI Financial Advisor</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="subtitle">Welcome, <b>{st.session_state.username}</b></div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "🏠 Dashboard",
            use_container_width=True
        ):
            st.session_state.page = "dashboard"
            st.rerun()

    with col2:

        if st.button(
            "💸 Expense Manager",
            use_container_width=True
        ):
            st.session_state.page = "expense_manager"
            st.rerun()

    st.divider()

    tab1, tab2 = st.tabs(
        [
            "📊 AI Insights",
            "💬 Chatbot"
        ]
    )
        # ==========================================
    # TAB 1 : AI INSIGHTS
    # ==========================================

    with tab1:

        total_expense = expense_manager.get_total_expense(USER_ID)

        category_summary = expense_manager.category_summary(USER_ID)

        if total_expense == 0:

            st.info(
                "Add some expenses first to receive AI suggestions."
            )

        else:

            st.metric(
                "Total Expenses",
                f"₹{total_expense:.2f}"
            )

            st.subheader("💡 AI Suggestions")

            if total_expense < 5000:

                st.success(
                    "✅ Great! Your spending is under control."
                )

            elif total_expense < 15000:

                st.warning(
                    "⚠️ Your spending is moderate. Review unnecessary expenses."
                )

            else:

                st.error(
                    "🚨 Your spending is high. Reduce unnecessary expenses and create a budget."
                )

            if category_summary:

                highest = max(
                    category_summary,
                    key=lambda x: x[1]
                )

                st.subheader(
                    "📊 Highest Spending Category"
                )

                st.write(
                    f"**{highest[0]}** : ₹{highest[1]:.2f}"
                )

                if highest[0] == "Food":

                    st.info(
                        "🍽️ Try cooking at home more often."
                    )

                elif highest[0] == "Shopping":

                    st.info(
                        "🛍️ Reduce impulse buying."
                    )

                elif highest[0] == "Travel":

                    st.info(
                        "🚗 Plan trips in advance."
                    )

                elif highest[0] == "Entertainment":

                    st.info(
                        "🎮 Set a monthly entertainment budget."
                    )

                else:

                    st.info(
                        "💰 Review this category for savings."
                    )
                        # ==========================================
    # TAB 2 : AI CHATBOT
    # ==========================================

    with tab2:

        st.subheader("💬 AI Finance Chatbot")

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

        # --------------------------
        # User Input
        # --------------------------

        prompt = st.chat_input(
            "Ask a finance question..."
        )

        if prompt:

            # Store user message

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": prompt
                }
            )

            with st.chat_message("user"):
                st.markdown(prompt)

            # Generate AI response

            with st.chat_message("assistant"):

                with st.spinner("Thinking..."):

                    reply = finance_chat(prompt)

                    st.markdown(reply)

            # Save AI response

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": reply
                }
            )

        st.divider()

        col1, col2 = st.columns([1, 1])

        with col1:

            if st.button(
                "🗑 Clear Chat",
                use_container_width=True,
                key="clear_chat"
            ):

                st.session_state.messages = []

                st.rerun()

        with col2:

            st.info(f"Messages: {len(st.session_state.messages)}")
                # ==========================================
    # Footer
    # ==========================================

    st.divider()

    if st.button(
        "⬅ Back to Dashboard",
        use_container_width=True,
        key="back_dashboard"
    ):

        st.session_state.page = "dashboard"
        st.rerun()