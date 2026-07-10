import streamlit as st
import pandas as pd
from datetime import date

from modules.expense_manager import ExpenseManager


def show_expense_manager():

    # ----------------------------------------
    # Login Check
    # ----------------------------------------

    if not st.session_state.get("logged_in", False):
        st.session_state.page = "login"
        st.rerun()

    USER_ID = st.session_state["user_id"]

    expense_manager = ExpenseManager()

    # ----------------------------------------
    # CSS
    # ----------------------------------------

    st.markdown("""
   <style>

/* ==========================================
Main Background
========================================== */

.stApp{
    background: #F4F8FC;
}

/* Main Container */

.block-container{
    padding-top:2rem;
    max-width:1200px;
}

/* ==========================================
Section Title
========================================== */

h1,h2,h3{
    color:#1E3A5F;
    font-weight:700;
}

/* ==========================================
Form Container
========================================== */

.expense-card{
    background:white;
    padding:25px;
    border-radius:18px;
    border:1px solid #D8E6F3;
    box-shadow:0 8px 25px rgba(0,0,0,.08);
    margin-bottom:25px;
}

/* ==========================================
Buttons
========================================== */

.stButton>button{
    width:100%;
    height:48px;
    border:none;
    border-radius:12px;
    background:#3B82F6;
    color:white;
    font-size:16px;
    font-weight:600;
}

.stButton>button:hover{
    background:#2563EB;
}

/* ==========================================
Input Boxes
========================================== */

.stTextInput input,
.stNumberInput input,
.stDateInput input,
.stSelectbox div[data-baseweb="select"]{
    background:white;
    border:2px solid #D6E6F7;
    border-radius:12px;
}

/* ==========================================
Metric Cards
========================================== */

div[data-testid="stMetric"]{
    background:#EAF4FF;
    border-radius:20px;
    padding:20px;
    border:1px solid #C9E2FF;
    box-shadow:0 4px 12px rgba(0,0,0,.06);
}

/* Metric Label */

div[data-testid="stMetricLabel"]{
    color:#4B6B88;
    font-size:15px;
    font-weight:600;
}

/* Metric Value */

div[data-testid="stMetricValue"]{
    color:#1565C0;
    font-size:34px;
    font-weight:700;
}

/* ==========================================
Dataframe
========================================== */

[data-testid="stDataFrame"]{
    background:white;
    border-radius:18px;
    border:1px solid #D8E6F3;
}

/* ==========================================
Expander
========================================== */

.streamlit-expanderHeader{
    background:#EDF6FF;
    border-radius:12px;
}

/* ==========================================
Horizontal Line
========================================== */

hr{
    border-color:#D7E5F2;
}

</style>
""", unsafe_allow_html=True)
    # ----------------------------------------
    # Header
    # ----------------------------------------

    st.markdown(
        '<div class="title">💸 Expense Manager</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="subtitle">Welcome, <b>{st.session_state.username}</b></div>',
        unsafe_allow_html=True
    )

    # ----------------------------------------
    # Dashboard Buttons
    # ----------------------------------------

    nav1, nav2 = st.columns(2)

    with nav1:

        if st.button(
            "🏠 Dashboard",
            use_container_width=True
        ):
            st.session_state.page = "dashboard"
            st.rerun()

    with nav2:

        if st.button(
            "🤖 AI Advisor",
            use_container_width=True
        ):
            st.session_state.page = "ai_advisor"
            st.rerun()

    st.divider()

    # ----------------------------------------
    # Add Expense
    # ----------------------------------------

    st.subheader("➕ Add New Expense")

    with st.form("expense_form"):

        col1, col2 = st.columns(2)

        with col1:

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

        with col2:

            amount = st.number_input(
                "Amount (₹)",
                min_value=0.0,
                format="%.2f"
            )

        description = st.text_input(
            "Description"
        )

        expense_date = st.date_input(
            "Expense Date",
            value=date.today()
        )

        submitted = st.form_submit_button(
            "Add Expense",
            use_container_width=True
        )

        if submitted:

            success = expense_manager.add_expense(
                USER_ID,
                category,
                amount,
                description,
                str(expense_date)
            )

            if success is True or (isinstance(success, tuple) and success[0]):
                st.success("✅ Expense added successfully.")
                st.rerun()

            else:
                st.error(
                    success[1] if isinstance(success, tuple)
                    else "Failed to add expense."
                )

    st.divider()

    # ----------------------------------------
    # Load Expense Data
    # ----------------------------------------

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
        # ----------------------------------------
    # Summary Card
    # ----------------------------------------

    total_expense = expense_manager.get_total_expense(USER_ID)

    metric1, metric2 = st.columns(2)

    with metric1:
        st.metric(
            "💸 Total Expense",
            f"₹{total_expense:,.2f}"
        )

    with metric2:
        st.metric(
            "🧾 Total Records",
            len(df)
        )

    st.divider()

    # ----------------------------------------
    # Filters
    # ----------------------------------------

    st.subheader("🔍 Search & Filter")

    filter_col1, filter_col2 = st.columns(2)

    with filter_col1:

        search_text = st.text_input(
            "Search Description",
            placeholder="Search..."
        )

    with filter_col2:

        category_options = ["All"]

        if not df.empty:
            category_options.extend(
                sorted(df["Category"].unique().tolist())
            )

        selected_category = st.selectbox(
            "Category",
            category_options
        )

    filtered_df = df.copy()

    if not filtered_df.empty:

        if search_text.strip():

            filtered_df = filtered_df[
                filtered_df["Description"]
                .astype(str)
                .str.contains(
                    search_text,
                    case=False,
                    na=False
                )
            ]

        if selected_category != "All":

            filtered_df = filtered_df[
                filtered_df["Category"] == selected_category
            ]

    st.divider()

    # ----------------------------------------
    # Expense History
    # ----------------------------------------

    st.subheader("📋 Expense History")

    if filtered_df.empty:

        st.info("No expenses found.")

    else:

        display_df = filtered_df[
            [
                "ID",
                "Category",
                "Amount",
                "Description",
                "Expense Date"
            ]
        ].copy()

        display_df["Amount"] = display_df["Amount"].apply(
            lambda x: f"₹{x:,.2f}"
        )

        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True
        )

    st.divider()
        # ----------------------------------------
    # Delete Expense
    # ----------------------------------------

    if not df.empty:

        st.subheader("🗑 Delete Expense")

        selected_id = st.selectbox(
            "Select Expense ID",
            df["ID"].tolist()
        )

        delete_col1, delete_col2 = st.columns(2)

        with delete_col1:

            if st.button(
                "Delete Selected Expense",
                type="primary",
                use_container_width=True
            ):

                success = expense_manager.delete_expense(
                    selected_id
                )

                if success is True or (
                    isinstance(success, tuple) and success[0]
                ):

                    st.success(
                        "Expense deleted successfully."
                    )

                    st.rerun()

                else:

                    st.error(
                        success[1]
                        if isinstance(success, tuple)
                        else "Unable to delete expense."
                    )

        with delete_col2:

            if st.button(
                "Refresh",
                use_container_width=True
            ):
                st.rerun()

    st.divider()

    # ----------------------------------------
    # Tips
    # ----------------------------------------

    st.subheader("💡 Expense Tips")

    st.info(
        """
• Record every expense daily.

• Review your highest spending category every week.

• Small savings every day lead to large savings over time.

• Build a monthly budget and compare it with actual spending.
        """
    )

    st.divider()

    # ----------------------------------------
    # Bottom Navigation
    # ----------------------------------------

    nav1, nav2 = st.columns(2)

    with nav1:

        if st.button(
            "⬅ Back to Dashboard",
            use_container_width=True
        ):

            st.session_state.page = "dashboard"
            st.rerun()

    with nav2:

        if st.button(
            "🚪 Logout",
            use_container_width=True
        ):

            st.session_state.logged_in = False

            st.session_state.page = "welcome"

            st.session_state.pop("user_id", None)
            st.session_state.pop("username", None)

            st.rerun()