import math
import os
from dotenv import load_dotenv
import google.generativeai as genai

# ==========================================
# Load Environment Variables
# ==========================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env file")

# ==========================================
# Configure Gemini
# ==========================================

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


class LoanPredictor:
    """
    Handles Loan Calculations and AI Loan Analysis
    """

    # ==========================================
    # EMI Calculator
    # ==========================================

    def calculate_emi(
        self,
        principal,
        annual_rate,
        years
    ):

        if principal <= 0 or years <= 0:
            return 0

        monthly_rate = annual_rate / (12 * 100)
        months = years * 12

        if monthly_rate == 0:
            emi = principal / months

        else:
            emi = (
                principal
                * monthly_rate
                * math.pow(1 + monthly_rate, months)
            ) / (
                math.pow(1 + monthly_rate, months) - 1
            )

        return round(emi, 2)

    # ==========================================
    # Total Payment
    # ==========================================

    def total_payment(
        self,
        principal,
        annual_rate,
        years
    ):

        emi = self.calculate_emi(
            principal,
            annual_rate,
            years
        )

        return round(
            emi * years * 12,
            2
        )

    # ==========================================
    # Total Interest
    # ==========================================

    def total_interest(
        self,
        principal,
        annual_rate,
        years
    ):

        return round(
            self.total_payment(
                principal,
                annual_rate,
                years
            ) - principal,
            2
        )

    # ==========================================
    # EMI Ratio
    # ==========================================

    def emi_ratio(
        self,
        monthly_income,
        monthly_emi
    ):

        if monthly_income <= 0:
            return 0

        return round(
            (monthly_emi / monthly_income) * 100,
            2
        )
        # ==========================================
    # Loan Eligibility
    # ==========================================

    def loan_eligibility(
        self,
        monthly_income,
        monthly_emi
    ):

        ratio = self.emi_ratio(
            monthly_income,
            monthly_emi
        )

        if ratio == 0:
            return "Income Required"

        elif ratio <= 40:
            return "Eligible"

        elif ratio <= 50:
            return "Moderate Risk"

        else:
            return "Not Eligible"

    # ==========================================
    # Loan Health Score
    # ==========================================

    def loan_health_score(
        self,
        monthly_income,
        monthly_emi
    ):

        ratio = self.emi_ratio(
            monthly_income,
            monthly_emi
        )

        if ratio == 0:
            return 0

        elif ratio <= 25:
            return 100

        elif ratio <= 35:
            return 90

        elif ratio <= 40:
            return 80

        elif ratio <= 50:
            return 60

        else:
            return 40

    # ==========================================
    # Amortization Schedule
    # ==========================================

    def amortization_schedule(
        self,
        principal,
        annual_rate,
        years
    ):

        emi = self.calculate_emi(
            principal,
            annual_rate,
            years
        )

        if emi == 0:
            return []

        monthly_rate = annual_rate / (12 * 100)
        months = years * 12

        balance = principal
        schedule = []

        for month in range(1, months + 1):

            if monthly_rate == 0:
                interest = 0
                principal_paid = emi

            else:
                interest = balance * monthly_rate
                principal_paid = emi - interest

            if principal_paid > balance:
                principal_paid = balance

            balance -= principal_paid

            schedule.append(
                {
                    "Month": month,
                    "EMI": round(emi, 2),
                    "Principal": round(principal_paid, 2),
                    "Interest": round(interest, 2),
                    "Remaining Balance": round(
                        max(balance, 0),
                        2
                    )
                }
            )

        return schedule
        # ==========================================
    # AI Loan Advisor
    # ==========================================

    def loan_advice(
        self,
        loan_amount,
        income,
        interest,
        years,
        emi,
        total_interest
    ):
        """
        Generate AI-powered loan advice using Gemini.
        """

        prompt = f"""
You are an experienced Financial Advisor.

Analyze the following loan details carefully.

Loan Details:
--------------
Loan Amount: ₹{loan_amount:,.2f}
Monthly Income: ₹{income:,.2f}
Interest Rate: {interest}%
Loan Tenure: {years} years
Monthly EMI: ₹{emi:,.2f}
Total Interest: ₹{total_interest:,.2f}
EMI Ratio: {self.emi_ratio(income, emi)}%
Eligibility: {self.loan_eligibility(income, emi)}
Health Score: {self.loan_health_score(income, emi)}/100

Provide the response in the following format:

## 📋 Overall Assessment

## ⚠️ Risk Level

## 👍 Advantages

## 👎 Disadvantages

## 💡 Suggestions

## ✅ Final Recommendation

Rules:
- Explain in simple English.
- Use bullet points.
- Keep the answer under 250 words.
- If EMI is more than 40% of income, warn the user.
- If EMI is less than 25% of income, mention that the loan is affordable.
- Suggest prepayment whenever beneficial.
- Do not answer unrelated questions.
"""

        try:

            response = model.generate_content(prompt)

            if response and hasattr(response, "text"):
                return response.text

                return "Unable to generate AI advice."

        except Exception as e:
            return f"❌ AI Error: {e}"
    