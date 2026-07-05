import streamlit as st
import pandas as pd
from modules.dashboard import Dashboard

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)
dashboard = Dashboard()
# if "logged_in" not in st.session_state:
#     st.warning("Please login first.")
#     st.stop()
if not st.session_state.get("logged_in"):
    st.switch_page("pages/login.py")
    st.stop()

USER_ID = st.session_state["user_id"]

st.sidebar.success(f"Welcome, {st.session_state['user_name']}")
if st.sidebar.button("🚪 Logout", use_container_width=True):
    st.session_state.clear()
    st.switch_page("pages/login.py")
    st.stop()

st.title("📊 Financial Dashboard")


st.markdown("### Welcome to your Finance Dashboard")

st.write(
    """
    Here you can monitor your financial health,
    expenses, savings, investments, and AI recommendations.
    """
)

st.markdown("---")
total_expense = dashboard.total_expense(USER_ID)
expenses = dashboard.all_expenses(USER_ID)
category_data = dashboard.category_summary(USER_ID)

monthly_income = 0      # Will come from Budget Planner later
savings = monthly_income - total_expense
health_score = 100 if total_expense == 0 else max(0, 100 - int(total_expense / 100))

# ============================
# Metrics
# ============================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Monthly Expense", f"₹{total_expense:.2f}")

with col2:
    st.metric("Monthly Income", f"₹{monthly_income:.2f}")

with col3:
    st.metric("Savings", f"₹{savings:.2f}")

with col4:
    st.metric("Health Score", f"{health_score}/100")

st.markdown("---")

# ============================
# Placeholder Charts
# ============================

left, right = st.columns(2)

with left:
    st.subheader("Expense Distribution")
    if category_data:

        df = pd.DataFrame(
            category_data,
            columns=["Category", "Amount"]
        )

        st.dataframe(df, use_container_width=True)

    else:
        st.info("No expense data available.")

with right:
    st.subheader("Monthly Spending")
    if expenses:

        df = pd.DataFrame(
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

        st.dataframe(df, use_container_width=True)

    else:
        st.info("No expense history found.")

st.markdown("---")

st.subheader("Recent Transactions")

if expenses:

    recent = pd.DataFrame(
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

    st.dataframe(
        recent.head(5),
        use_container_width=True
    )

else:
    st.info("No recent transactions.")

st.success("Dashboard Loaded Successfully ✅")