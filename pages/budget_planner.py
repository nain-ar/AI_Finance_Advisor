import streamlit as st
from modules.budget_planner import BudgetPlanner
from modules.expense_manager import ExpenseManager


def show_budget_planner():

    # ======================================
    # Login Check
    # ======================================

    if not st.session_state.get("logged_in", False):
        st.session_state.page = "login"
        st.rerun()

    expense_manager = ExpenseManager()
    budget_planner = BudgetPlanner()

    USER_ID = st.session_state["user_id"]


     # ======================================
     # CSS
     # ======================================

    st.markdown("""
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

#     # ======================================
#     # Header
#     # ======================================

#     st.markdown(
#         '<div class="title">💰 Budget Planner</div>',
#         unsafe_allow_html=True
#     )

#     st.markdown(
#         f'<div class="subtitle">Welcome, <b>{st.session_state.username}</b></div>',
#         unsafe_allow_html=True
#     )


    # ======================================
    # Navigation
    # ======================================

    c1, c2 = st.columns(2)

    with c1:

        if st.button(
            "🏠 Dashboard",
            use_container_width=True
        ):
            st.session_state.page = "dashboard"
            st.rerun()

    with c2:

        if st.button(
            "💸 Expense Manager",
            use_container_width=True
        ):
            st.session_state.page = "expense_manager"
            st.rerun()

    st.divider()

    # ======================================
    # Budget Inputs
    # ======================================

    monthly_income = st.number_input(
        "Monthly Income (₹)",
        min_value=0.0,
        format="%.2f"
    )

    monthly_budget = st.number_input(
        "Monthly Budget (₹)",
        min_value=0.0,
        format="%.2f"
    )

    total_expense = expense_manager.get_total_expense(USER_ID)

    remaining_budget = budget_planner.remaining_budget(
        USER_ID,
        monthly_budget
    )

    st.divider()

    # ======================================
    # Metrics
    # ======================================

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric(
            "Monthly Budget",
            f"₹{monthly_budget:.2f}"
        )

    with m2:
        st.metric(
            "Total Expenses",
            f"₹{total_expense:.2f}"
        )

    with m3:
        st.metric(
            "Remaining Budget",
            f"₹{remaining_budget:.2f}"
        )

    st.divider()

    # ======================================
    # Budget Analysis
    # ======================================

    if monthly_budget > 0:

        status = budget_planner.budget_status(
            USER_ID,
            monthly_budget
        )

        percentage = budget_planner.expense_percentage(
            USER_ID,
            monthly_budget
        )

        st.subheader("Budget Usage")

        st.progress(min(percentage / 100, 1.0))

        st.write(f"### {percentage:.2f}% Used")

        if status == "Budget Exceeded":

            st.error(
                "⚠️ You have exceeded your monthly budget."
            )

        elif status == "Budget Fully Utilized":

            st.warning(
                "⚠️ Your monthly budget is fully utilized."
            )

        else:

            st.success(
                "✅ Great! You are within your budget."
            )

    else:

        st.info(
            "Enter your monthly budget to begin tracking."
        )

    st.divider()

    # ======================================
    # Bottom Navigation
    # ======================================

    b1, b2 = st.columns(2)

    with b1:

        if st.button(
            "⬅ Back to Dashboard",
            use_container_width=True
        ):
            st.session_state.page = "dashboard"
            st.rerun()

    with b2:

        if st.button(
            "🤖 AI Advisor",
            use_container_width=True
        ):
            st.session_state.page = "ai_advisor"
            st.rerun()