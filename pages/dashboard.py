import streamlit as st
import pandas as pd
from modules.dashboard import Dashboard


def show_dashboard():

    # -----------------------------
    # Login Check
    # -----------------------------
    if not st.session_state.get("logged_in", False):
        st.session_state.page = "login"
        st.rerun()

    dashboard = Dashboard()

    user_id = st.session_state["user_id"]

    total_expense = dashboard.total_expense(user_id)
    expenses = dashboard.all_expenses(user_id)
    category_data = dashboard.category_summary(user_id)

    # Temporary values
    monthly_income = 0
    savings = monthly_income - total_expense

    if total_expense == 0:
        health_score = 100
    elif total_expense < 5000:
        health_score = 95
    elif total_expense < 10000:
        health_score = 85
    elif total_expense < 20000:
        health_score = 70
    else:
        health_score = 55

    # -----------------------------
    # Custom CSS
    # -----------------------------
    st.markdown("""
<style>

/* ==========================
Background
========================== */

# <style>

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

/* ==========================


/* ==========================
Divider
========================== */

hr{
    border-color:#334155;
}

</style>
""", unsafe_allow_html=True)
    # -----------------------------
    # Hero Section
    # -----------------------------
    st.markdown(f"""
    <div class="hero">

    <h1>💰 AI Finance Advisor</h1>

    <p>
    Welcome back,
    <b>{st.session_state.username}</b> 👋
    <br>
    Manage your expenses smarter with AI.
    </p>

    </div>
    """, unsafe_allow_html=True)

    # -----------------------------
    # KPI Cards
    # -----------------------------
    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric(
            "💸 Expenses",
            f"₹{total_expense:,.2f}"
        )

    with c2:
        st.metric(
            "💰 Income",
            f"₹{monthly_income:,.2f}"
        )

    with c3:
        st.metric(
            "🏦 Savings",
            f"₹{savings:,.2f}"
        )

    with c4:
        st.metric(
            " Health Score",
            f"{health_score}/100"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # -----------------------------
    # Quick Actions
    # -----------------------------
    st.markdown(
        '<div class="section-title">🚀 Quick Actions</div>',
        unsafe_allow_html=True
    )

    row1 = st.columns(3)

    with row1[0]:
        if st.button(
            "🤖 AI Advisor",
            use_container_width=True
        ):
            st.session_state.page = "ai_advisor"
            st.rerun()

    with row1[1]:
        if st.button(
            "💸 Expense Manager",
            use_container_width=True
        ):
            st.session_state.page = "expense_manager"
            st.rerun()

    with row1[2]:
        if st.button(
            "🏦 Loan Predictor",
            use_container_width=True
        ):
            st.session_state.page = "loan_prediction"
            st.rerun()

    row2 = st.columns(3)

    with row2[0]:
        if st.button(
            "📈 Investment",
            use_container_width=True
        ):
            st.session_state.page = "investment"
            st.rerun()

    with row2[1]:
        if st.button(
            "💼 Budget Planner",
            use_container_width=True
        ):
            st.session_state.page = "budget_planner"
            st.rerun()

    with row2[2]:
        if st.button(
            "🧾 Receipt Scanner",
            use_container_width=True
        ):
            st.session_state.page = "receipt_scanner"
            st.rerun()

    st.markdown("---")
        # -----------------------------
    # Expense Summary & Transactions
    # -----------------------------
    left, right = st.columns([1, 1.4])

    with left:

        st.markdown(
            '<div class="section-title">📊 Expense Summary</div>',
            unsafe_allow_html=True
        )

        if category_data:

            summary_df = pd.DataFrame(
                category_data,
                columns=[
                    "Category",
                    "Amount"
                ]
            )

            summary_df["Amount"] = summary_df["Amount"].apply(
                lambda x: f"₹{x:,.2f}"
            )

            st.dataframe(
                summary_df,
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info("No expense data available.")

    with right:

        st.markdown(
            '<div class="section-title">📋 Recent Transactions</div>',
            unsafe_allow_html=True
        )

        if expenses:

            history = pd.DataFrame(
                expenses,
                columns=[
                    "ID",
                    "User ID",
                    "Category",
                    "Amount",
                    "Description",
                    "Date"
                ]
            )

            display_df = history[
                [
                    "Category",
                    "Amount",
                    "Description",
                    "Date"
                ]
            ].copy()

            display_df["Amount"] = display_df["Amount"].apply(
                lambda x: f"₹{x:,.2f}"
            )

            st.dataframe(
                display_df.head(10),
                use_container_width=True,
                hide_index=True
            )

        else:

            st.info("No transactions found.")

    st.markdown("---")

    # -----------------------------
    # Financial Overview
    # -----------------------------
    st.markdown(
        '<div class="section-title">📈 Financial Overview</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:

        st.progress(
            min(
                health_score,
                100
            )
        )

        st.caption(
            "Financial Health Score"
        )

    with col2:

        st.metric(
            "Total Transactions",
            len(expenses)
        )

        st.metric(
            "Expense Categories",
            len(category_data)
        )

    st.markdown("---")

    # -----------------------------
    # AI Insights
    # -----------------------------
    st.markdown(
        '<div class="section-title">🤖 AI Financial Insights</div>',
        unsafe_allow_html=True
    )

    if category_data:

        highest = max(
            category_data,
            key=lambda x: x[1]
        )

        category_name = highest[0]
        category_amount = highest[1]

        st.markdown(
            f"""
<div class="ai-card">

### 💡 Smart Recommendation

• Highest spending category:
**{category_name}**
(₹{category_amount:,.2f})

• Review this category to identify
possible savings.

• Track your expenses weekly instead
of waiting until the end of the month.

• Building a monthly budget can improve
your financial health score.

</div>
""",
            unsafe_allow_html=True
        )

    else:

        st.info(
            "Start adding expenses to receive AI-powered insights."
        )

    st.markdown("<div class='footer-space'></div>", unsafe_allow_html=True)
        # ---------------------------------
    # Tips Section
    # ---------------------------------

    st.markdown("---")

    st.markdown(
        '<div class="section-title">📌 Financial Tips</div>',
        unsafe_allow_html=True
    )

    tip_col1, tip_col2 = st.columns(2)

    with tip_col1:

        st.info(
            """
💡 **Save Before Spending**

Try saving at least **20% of your monthly income**
before making non-essential purchases.
            """
        )

    with tip_col2:

        st.info(
            """
📈 **Track Every Expense**

Recording every expense helps you understand
where your money goes and improves financial planning.
            """
        )

    st.markdown("---")

    # ---------------------------------
    # Logout
    # ---------------------------------

    c1, c2, c3 = st.columns([1, 2, 1])

    with c2:

        if st.button(
            " Logout",
            use_container_width=True,
            type="primary"
        ):

            st.session_state.logged_in = False

            st.session_state.page = "welcome"

            st.session_state.pop("user_id", None)
            st.session_state.pop("username", None)

            st.rerun()