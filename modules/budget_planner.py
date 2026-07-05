from modules.expense_manager import ExpenseManager


class BudgetPlanner:

    def __init__(self):
        self.expense_manager = ExpenseManager()

    # ==========================================
    # Remaining Budget
    # ==========================================
    def remaining_budget(self, user_id, monthly_budget):

        total_expense = self.expense_manager.get_total_expense(user_id)

        remaining = monthly_budget - total_expense

        return remaining

    # ==========================================
    # Budget Status
    # ==========================================
    def budget_status(self, user_id, monthly_budget):

        total_expense = self.expense_manager.get_total_expense(user_id)

        if total_expense > monthly_budget:
            return "Budget Exceeded"

        elif total_expense == monthly_budget:
            return "Budget Fully Utilized"

        else:
            return "Within Budget"

    # ==========================================
    # Expense Percentage
    # ==========================================
    def expense_percentage(self, user_id, monthly_budget):

        total = self.expense_manager.get_total_expense(user_id)

        if monthly_budget == 0:
            return 0

        return round((total / monthly_budget) * 100, 2)