from modules.expense_manager import ExpenseManager
import streamlit as st

class Dashboard:

    def __init__(self):
        self.expense_manager = ExpenseManager()

    # =====================================
    # Total Expense
    # =====================================
    def total_expense(self, user_id):
        return self.expense_manager.get_total_expense(user_id)

    # =====================================
    # Category Summary
    # =====================================
    def category_summary(self, user_id):
        return self.expense_manager.category_summary(user_id)

    # =====================================
    # All Expenses
    # =====================================
    def all_expenses(self, user_id):
        return self.expense_manager.get_all_expenses(user_id)