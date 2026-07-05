import os
from dotenv import load_dotenv
import google.generativeai as genai

# ==========================
# Load Environment Variables
# ==========================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError(
        "GEMINI_API_KEY not found. Please check your .env file."
    )

# ==========================
# Configure Gemini
# ==========================

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

# ==========================
# Finance Chatbot
# ==========================

def finance_chat(user_message):

    if not user_message.strip():
        return "Please enter a valid finance-related question."

    prompt = f"""
You are AI Finance Advisor.

You are a professional financial assistant.

You ONLY answer questions related to:

• Personal Finance
• Budget Planning
• Expense Management
• Savings
• Investments
• SIP
• Mutual Funds
• Stock Market Basics
• Loans
• EMI
• Insurance
• Tax Basics
• Financial Planning
• Banking

Rules:

1. Give accurate financial advice.
2. Explain in simple English.
3. Use bullet points whenever possible.
4. Keep answers concise and practical.
5. If the question is NOT related to finance, politely reply:

"I'm your AI Finance Advisor. I can help with budgeting, expenses, investments, loans, savings, insurance, and other finance-related topics."

User Question:
{user_message}
"""

    try:
        response = model.generate_content(prompt)

        if response and hasattr(response, "text"):
            return response.text

        return "Sorry, I couldn't generate a response."

    except Exception:
        return (
            "⚠️ Unable to contact the AI service right now. "
            "Please check your internet connection or API configuration and try again."
        )