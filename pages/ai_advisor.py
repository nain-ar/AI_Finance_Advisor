import streamlit as st
from modules.expense_manager import ExpenseManager

st.set_page_config(
    page_title="AI Financial Advisor",
    page_icon="🤖",
    layout="wide"
)

expense_manager = ExpenseManager()

if "logged_in" not in st.session_state:
    st.warning("Please login first.")
    st.stop()

USER_ID = st.session_state["user_id"]

st.sidebar.success(f"Welcome, {st.session_state['user_name']}")

st.title("🤖 AI Financial Advisor")

st.write(
    "Get personalized financial suggestions based on your spending."
)

st.markdown("---")

total_expense = expense_manager.get_total_expense(USER_ID)
category_summary = expense_manager.category_summary(USER_ID)

if total_expense == 0:

    st.info("Add some expenses first to receive financial advice.")

else:

    st.metric("Total Expenses", f"₹{total_expense:.2f}")

    st.markdown("### 💡 AI Suggestions")

    if total_expense < 5000:
        st.success("✅ Your expenses are currently under control. Keep tracking your spending.")

    elif total_expense < 15000:
        st.warning("⚠️ Your spending is moderate. Review non-essential expenses regularly.")

    else:
        st.error("🚨 Your expenses are quite high. Consider reducing unnecessary spending and creating a monthly budget.")

    if category_summary:

        highest = max(category_summary, key=lambda x: x[1])

        st.markdown("### 📊 Highest Spending Category")

        st.write(f"**{highest[0]}** : ₹{highest[1]:.2f}")

        if highest[0] == "Food":
            st.info("🍽️ Try meal planning or cooking at home to reduce food expenses.")

        elif highest[0] == "Shopping":
            st.info("🛍️ Avoid impulse purchases and compare prices before buying.")

        elif highest[0] == "Travel":
            st.info("🚗 Plan your trips in advance to save on transportation costs.")

        elif highest[0] == "Entertainment":
            st.info("🎮 Set a monthly entertainment budget to avoid overspending.")

        else:
            st.info("💰 Review this category and see if there are opportunities to save.")

st.markdown("---")

st.success("AI Financial Advisor Ready ✅")
# import os
# from dotenv import load_dotenv
# import google.generativeai as genai

# load_dotenv()

# api_key = os.getenv("GEMINI_API_KEY")

# genai.configure(api_key=api_key)

# model = genai.GenerativeModel("gemini-2.5-flash")


# def loan_advice(
#     loan_amount,
#     income,
#     interest,
#     years,
#     emi,
#     total_interest
# ):
#     prompt = f"""
# You are an expert financial advisor.

# Analyze this loan.

# Loan Amount: ₹{loan_amount}
# Monthly Income: ₹{income}
# Interest Rate: {interest}%
# Loan Tenure: {years} years
# Monthly EMI: ₹{emi:.2f}
# Total Interest: ₹{total_interest:.2f}

# Provide:
# 1. Overall assessment
# 2. Risk level
# 3. Pros
# 4. Cons
# 5. Suggestions
# 6. Final recommendation

# Keep the response under 250 words.
# """

#     response = model.generate_content(prompt)
#     return response.text




