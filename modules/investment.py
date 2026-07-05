class Investment:

    def __init__(self):
        pass

    # ==========================================
    # Simple Interest
    # ==========================================
    def simple_interest(self, principal, rate, time):

        interest = (principal * rate * time) / 100
        total_amount = principal + interest

        return {
            "interest": round(interest, 2),
            "total_amount": round(total_amount, 2)
        }

    # ==========================================
    # Compound Interest
    # ==========================================
    def compound_interest(self, principal, rate, time):

        amount = principal * ((1 + (rate / 100)) ** time)
        interest = amount - principal

        return {
            "interest": round(interest, 2),
            "total_amount": round(amount, 2)
        }

    # ==========================================
    # SIP Calculator
    # ==========================================
    def sip_calculator(self, monthly_investment, annual_rate, years):

        monthly_rate = annual_rate / 12 / 100
        months = years * 12

        maturity = monthly_investment * (
            (((1 + monthly_rate) ** months) - 1)
            / monthly_rate
        ) * (1 + monthly_rate)

        invested = monthly_investment * months

        return {
            "invested_amount": round(invested, 2),
            "estimated_returns": round(maturity - invested, 2),
            "maturity_value": round(maturity, 2)
        }

    # ==========================================
    # Investment Suggestion
    # ==========================================
    def investment_suggestion(self, risk_level):

        risk_level = risk_level.lower()

        if risk_level == "low":
            return [
                "Fixed Deposit",
                "PPF",
                "Government Bonds"
            ]

        elif risk_level == "medium":
            return [
                "Balanced Mutual Funds",
                "Index Funds",
                "Gold ETF"
            ]

        elif risk_level == "high":
            return [
                "Equity Mutual Funds",
                "Stocks",
                "Sector Funds"
            ]

        return ["Please select a valid risk level."]