import streamlit as st
import os
import sys

# print("Current Working Directory:")
# print(os.getcwd())

# print("\nPython Path:")
# for p in sys.path:
#     print(p)

# ======================================
# Page Configuration
# ======================================
st.set_page_config(
    page_title="AI Finance Advisor",
    page_icon="💰",
    layout="wide"
)

# ======================================
# Sidebar
# ======================================
st.sidebar.title("💰 AI Finance Advisor")

st.sidebar.markdown("---")

st.sidebar.success("Welcome!")

st.sidebar.info(
    """
    Navigate using the pages menu.

    Features:
    - Dashboard
    - Expense Manager
    - Budget Planner
    - Investment Calculator
    - Loan Prediction
    - Receipt Scanner
    - AI Advisor
    """
)

# ======================================
# Main Page
# ======================================
st.title("💰 AI Finance Advisor")

st.markdown("## Welcome!")

st.write("""
Welcome to **AI Finance Advisor**.

This application helps you:

✅ Track your expenses

✅ Manage your monthly budget

✅ Calculate investments

✅ Predict loan approval

✅ Scan receipts using OpenCV

✅ Get AI-powered financial suggestions
""")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Expenses Managed", "0")

with col2:
    st.metric("Savings", "₹0")

with col3:
    st.metric("Health Score", "0/100")

st.markdown("---")

# st.subheader("🚀 Upcoming Features")

# st.write("""
# - Expense Tracker
# - Budget Planner
# - Investment Calculator
# - Loan Prediction (Machine Learning)
# - Receipt Scanner (OpenCV + OCR)
# - Financial Health Score
# - AI Chatbot
# """)

# st.success("Project initialized successfully! 🎉")