import streamlit as st
from modules.loan_predictor import LoanPredictor

st.set_page_config(
    page_title="Loan Predictor",
    page_icon="🏦",
    layout="wide"
)

predictor = LoanPredictor()

st.title("🏦 Loan Predictor")

st.markdown("""
Estimate your monthly EMI and get AI-powered loan advice before taking a loan.
""")

st.markdown("---")

# ==========================================
# User Inputs
# ==========================================

loan_amount = st.number_input(
    "Loan Amount (₹)",
    min_value=0.0,
    format="%.2f"
)

monthly_income = st.number_input(
    "Monthly Income (₹)",
    min_value=0.0,
    format="%.2f"
)

interest_rate = st.slider(
    "Annual Interest Rate (%)",
    1.0,
    25.0,
    8.5
)

loan_years = st.slider(
    "Loan Tenure (Years)",
    1,
    30,
    10
)

st.markdown("---")

# ==========================================
# Buttons
# ==========================================

col1, col2 = st.columns(2)

with col1:
    calculate = st.button(
        "🧮 Calculate EMI",
        use_container_width=True
    )

with col2:
    advisor = st.button(
        "🤖 AI Loan Advisor",
        use_container_width=True
    )

# ==========================================
# Calculate Loan
# ==========================================

if (calculate or advisor):

    if loan_amount <= 0:
        st.warning("Please enter a valid loan amount.")
        st.stop()

    emi = predictor.calculate_emi(
        loan_amount,
        interest_rate,
        loan_years
    )

    total_interest = predictor.total_interest(
        loan_amount,
        interest_rate,
        loan_years
    )

    total_payment = predictor.total_payment(
        loan_amount,
        interest_rate,
        loan_years
    )

    eligibility = predictor.loan_eligibility(
        monthly_income,
        emi
    )

    ratio = predictor.emi_ratio(
        monthly_income,
        emi
    )

    health_score = predictor.loan_health_score(
        monthly_income,
        emi
    )

    st.markdown("## 📊 Loan Summary")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.metric(
            "Monthly EMI",
            f"₹{emi:,.2f}"
        )

    with c2:
        st.metric(
            "Total Interest",
            f"₹{total_interest:,.2f}"
        )

    with c3:
        st.metric(
            "Total Payment",
            f"₹{total_payment:,.2f}"
        )

    st.markdown("---")

    c4, c5, c6 = st.columns(3)

    with c4:
        st.metric(
            "EMI Ratio",
            f"{ratio}%"
        )

    with c5:
        st.metric(
            "Eligibility",
            eligibility
        )

    with c6:
        st.metric(
            "Health Score",
            f"{health_score}/100"
        )

    # ==========================================
    # Amortization Schedule
    # ==========================================

    with st.expander("📅 Amortization Schedule"):

        schedule = predictor.amortization_schedule(
            loan_amount,
            interest_rate,
            loan_years
        )

        st.dataframe(
            schedule,
            use_container_width=True,
            hide_index=True
        )

    # ==========================================
    # AI Loan Advisor
    # ==========================================

    if advisor:

        if monthly_income <= 0:
            st.warning("Please enter your monthly income.")
        else:

            with st.spinner("🤖 AI is analyzing your loan..."):

                advice = predictor.loan_advice(
                    loan_amount,
                    monthly_income,
                    interest_rate,
                    loan_years,
                    emi,
                    total_interest
                )

            st.markdown("---")
            st.subheader("🤖 AI Loan Advisor")
            st.write(advice)