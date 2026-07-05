import streamlit as st
import pandas as pd
from datetime import date

from modules.expense_manager import ExpenseManager


st.set_page_config(
    page_title="Expense Manager",
    page_icon="💸",
    layout="wide"
)

st.title("💸 Expense Manager")

expense_manager = ExpenseManager()

if "logged_in" not in st.session_state:
    st.warning("Please login first.")
    st.stop()

USER_ID = st.session_state["user_id"]

st.sidebar.success(f"Welcome, {st.session_state['user_name']}")
# ==========================
# Add Expense Form
# ==========================

st.subheader("Add New Expense")

with st.form("expense_form"):

    category = st.selectbox(
        "Category",
        [
            "Food",
            "Travel",
            "Shopping",
            "Bills",
            "Health",
            "Education",
            "Entertainment",
            "Other"
        ]
    )

    amount = st.number_input(
        "Amount",
        min_value=0.0,
        format="%.2f"
    )

    description = st.text_input("Description")

    expense_date = st.date_input(
        "Expense Date",
        value=date.today()
    )

    submitted = st.form_submit_button("Add Expense")

    if submitted:

        success = expense_manager.add_expense(
            USER_ID,
            category,
            amount,
            description,
            str(expense_date)
        )

        if success is True:
            st.success("Expense Added Successfully ✅")
            st.rerun()

        else:
            st.error(success[1])

st.markdown("---")

# ==========================
# Expense History
# ==========================

st.subheader("Expense History")

expenses = expense_manager.get_all_expenses(USER_ID)

df = pd.DataFrame(
    expenses,
    columns=[
        "ID",
        "User ID",
        "Category",
        "Amount",
        "Description",
        "Expense Date"
    ]
)

if df.empty:
    st.info("No expenses available.")

else:
    st.dataframe(
        df,
        use_container_width=True
    )

    total = expense_manager.get_total_expense(USER_ID)

    st.metric(
        "Total Expense",
        f"₹{total:.2f}"
    )

    st.markdown("---")

    st.subheader("🗑️ Delete Expense")

    selected_id = st.selectbox(
        "Select Expense ID",
        df["ID"].tolist()
    )

    if st.button("Delete Expense", type="primary"):

        success = expense_manager.delete_expense(selected_id)

        if success:
            st.success("Expense Deleted Successfully ✅")
            st.rerun()

        else:
            st.error(success[1])