import streamlit as st
from modules.investment import Investment
st.set_page_config(
    page_title="Investment Planner",
    page_icon="📈",
    layout="wide"
)
investment = Investment()
if "logged_in" not in st.session_state:
    st.warning("Please login first.")
    st.stop()

USER_ID = st.session_state["user_id"]

st.sidebar.success(f"Welcome, {st.session_state['user_name']}")

st.title("📈 Investment Planner")

st.markdown(
    """
    Estimate the future value of your investments using compound interest.
    """
)

st.markdown("---")

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


# st.markdown("---")

# st.subheader("Recommended Investments")

# recommendations = investment.investment_suggestion(risk)

# for item in recommendations:
#     st.write(f"✅ {item}")
sip = investment.sip_calculator(
    monthly,
    rate,
    years
)

future_value = sip["maturity_value"] + initial
invested = sip["invested_amount"] + initial
profit = future_value - invested



col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Invested", f"₹{invested:,.2f}")

with col2:
    st.metric("Estimated Value", f"₹{future_value:,.2f}")

with col3:
    st.metric("Estimated Profit", f"₹{profit:,.2f}")

st.info(
    "This calculation is only an estimate and does not guarantee future returns."
)
st.markdown("---")

st.subheader("Recommended Investments")

recommendations = investment.investment_suggestion(risk)

for item in recommendations:
    st.write(f"✅ {item}")