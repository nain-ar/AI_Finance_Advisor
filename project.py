import streamlit as st


# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

if "user_name" not in st.session_state:
    st.session_state["user_name"] = ""

if "user_id" not in st.session_state:
    st.session_state["user_id"] = None

# ======================================
# Page Configuration
# ======================================

st.set_page_config(
    page_title="AI Finance Advisor",
    page_icon="💰",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ======================================
# Hide Streamlit UI
# ======================================

st.markdown("""
<style>

[data-testid="stSidebar"]{
    display:none;
}

#MainMenu{
    visibility:hidden;
}

header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)

# ======================================
# Session State
# ======================================

if "page" not in st.session_state:
    st.session_state.page = "welcome"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# ======================================
# Navigation
# ======================================

page = st.session_state.page

if page == "welcome":

    from pages.welcome import show_welcome
    show_welcome()

elif page == "login":

    from pages.login import show_login
    show_login()

elif page == "dashboard":

    if st.session_state.logged_in:

        from pages.dashboard import show_dashboard
        show_dashboard()

    else:

        st.session_state.page = "login"
        st.rerun()

elif page == "expense_manager":

    from pages.expense_manager import show_expense_manager
    show_expense_manager()

elif page == "ai_advisor":

    from pages.ai_advisor import show_ai_advisor
    show_ai_advisor()

elif page == "loan_prediction":

    from pages.loan_predictor import show_loan_predictor
    show_loan_predictor()

elif page == "budget_planner":

    from pages.budget_planner import show_budget_planner
    show_budget_planner()

elif page == "investment":

    from pages.investment import show_investment
    show_investment()

elif page == "receipt_scanner":

    from pages.receipts_scanner import show_receipt_scanner
    show_receipt_scanner()

else:

    st.session_state.page = "welcome"
    st.rerun()