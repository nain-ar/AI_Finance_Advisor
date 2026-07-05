import streamlit as st
from modules.budget_planner import BudgetPlanner
from modules.expense_manager import ExpenseManager

st.set_page_config(
    page_title="Budget Planner",
    page_icon="💰",
    layout="wide"
)

expense_manager = ExpenseManager()
budget_planner = BudgetPlanner()

if "logged_in" not in st.session_state:
    st.warning("Please login first.")
    st.stop()

USER_ID = st.session_state["user_id"]

st.sidebar.success(f"Welcome, {st.session_state['user_name']}")

st.title("💰 Budget Planner")

st.markdown("Plan your monthly budget and monitor your spending.")

st.markdown("---")

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

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Monthly Budget", f"₹{monthly_budget:.2f}")

with col2:
    st.metric("Total Expenses", f"₹{total_expense:.2f}")

with col3:
    st.metric("Remaining Budget", f"₹{remaining_budget:.2f}")

st.markdown("---")
if monthly_budget > 0:

    status = budget_planner.budget_status(
        USER_ID,
        monthly_budget
    )

    percentage = budget_planner.expense_percentage(
        USER_ID,
        monthly_budget
    )

    st.progress(min(percentage / 100, 1.0))

    st.write(f"### Budget Used: {percentage}%")

    if status == "Budget Exceeded":
        st.error("⚠️ You have exceeded your monthly budget.")

    elif status == "Budget Fully Utilized":
        st.warning("⚠️ You have fully utilized your budget.")

    else:
        st.success("✅ You are within your budget.")

else:
    st.info("Enter a monthly budget to start tracking.")