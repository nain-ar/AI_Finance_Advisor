import streamlit as st
from modules.investment import Investment


def show_investment():

    # ======================================
    # Login Check
    # ======================================

    if not st.session_state.get("logged_in", False):
        st.session_state.page = "login"
        st.rerun()

    investment = Investment()

    # ======================================
    # CSS
    # ======================================

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

    # ======================================
    # Header
    # ======================================

    st.markdown(
        '<div class="title">📈 Investment Planner</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="subtitle">Welcome, <b>{st.session_state.username}</b></div>',
        unsafe_allow_html=True
    )

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
            "💰 Budget Planner",
            use_container_width=True
        ):
            st.session_state.page = "budget_planner"
            st.rerun()

    st.divider()

    # ======================================
    # Inputs
    # ======================================

    initial = st.number_input(
        "Initial Investment (₹)",
        min_value=0.0,
        format="%.2f"
    )

    monthly = st.number_input(
        "Monthly Investment (₹)",
        min_value=0.0,
        format="%.2f"
    )

    rate = st.slider(
        "Expected Annual Return (%)",
        1.0,
        20.0,
        12.0
    )

    years = st.slider(
        "Investment Period (Years)",
        1,
        40,
        10
    )

    risk = st.selectbox(
        "Risk Profile",
        [
            "Low",
            "Medium",
            "High"
        ]
    )

    st.divider()

    # ======================================
    # Calculation
    # ======================================

    sip = investment.sip_calculator(
        monthly,
        rate,
        years
    )

    future_value = sip["maturity_value"] + initial
    invested = sip["invested_amount"] + initial
    profit = future_value - invested

    # ======================================
    # Metrics
    # ======================================

    m1, m2, m3 = st.columns(3)

    with m1:
        st.metric(
            "Total Invested",
            f"₹{invested:,.2f}"
        )

    with m2:
        st.metric(
            "Estimated Value",
            f"₹{future_value:,.2f}"
        )

    with m3:
        st.metric(
            "Estimated Profit",
            f"₹{profit:,.2f}"
        )

    st.info(
        "This is only an estimated calculation. Actual returns may vary."
    )

    st.divider()

    # ======================================
    # Recommendations
    # ======================================

    st.subheader("📊 Recommended Investments")

    recommendations = investment.investment_suggestion(risk)

    for item in recommendations:
        st.success(item)

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