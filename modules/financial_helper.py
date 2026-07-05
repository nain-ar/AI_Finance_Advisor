class FinancialHelper:

    @staticmethod
    def format_currency(amount):
        return f"₹{amount:,.2f}"

    @staticmethod
    def calculate_savings(income, expense):
        return income - expense

    @staticmethod
    def expense_ratio(expense, income):

        if income == 0:
            return 0

        return round((expense / income) * 100, 2)