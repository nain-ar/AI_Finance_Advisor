import streamlit as st
import pandas as pd
from modules.expense_manager import ExpenseManager

st.set_page_config(
    page_title="Reports",
    page_icon="📄",
    layout="wide"
)

expense_manager = ExpenseManager()

if "logged_in" not in st.session_state:
    st.warning("Please login first.")
    st.stop()

USER_ID = st.session_state["user_id"]

st.sidebar.success(f"Welcome, {st.session_state['user_name']}")

st.title("📄 Financial Reports")

st.markdown(
    "View, download, and analyze your financial records."
)

st.markdown("---")

expenses = expense_manager.get_all_expenses(USER_ID)

if expenses:

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

    st.subheader("Expense Report")

    st.dataframe(
        df,
        use_container_width=True
    )

    total = expense_manager.get_total_expense(USER_ID)

    st.metric(
        "Total Expenses",
        f"₹{total:.2f}"
    )

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download CSV Report",
        data=csv,
        file_name="expense_report.csv",
        mime="text/csv"
    )

else:
    st.info("No expense records found.")

st.markdown("---")

st.success("Reports Module Ready ✅")