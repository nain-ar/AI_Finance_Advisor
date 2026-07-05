# from database.database import FinanceDatabase


# class ExpenseManager:
#     """
#     Business logic for managing expenses.
#     """

#     def __init__(self):
#         self.db = FinanceDatabase()

#     # ==============================
#     # Add Expense
#     # ==============================
#     def add_expense(self, user_id, category, amount, description, expense_date):
#         try:
#             self.db.add_expense(
#                 user_id,
#                 category,
#                 amount,
#                 description,
#                 expense_date
#             )
#             return True

#         except Exception as e:
#             return False, str(e)

#     # ==============================
#     # Get All Expenses
#     # ==============================

#     # ==============================
# # Get All Expenses
# # ==============================
#     def get_all_expenses(self, user_id):
#         return self.db.get_all_expenses(user_id)
#     # ==============================
# # Get Single Expense
# # ==============================
#     def get_expense(self, expense_id):
#         return self.db.get_expense(expense_id)



#     # ==============================
#     # Delete Expense
#     # ==============================
#     def delete_expense(self, expense_id):
#         try:
#             self.db.delete_expense(expense_id)
#             return True

#         except Exception as e:
#             return False, str(e)

#     # ==============================
#     # Update Expense
#     # ==============================
#     def update_expense(
#         self,
#         expense_id,
#         category,
#         amount,
#         description,
#         expense_date
#     ):
#         try:
#             self.db.update_expense(
#                 expense_id,
#                 category,
#                 amount,
#                 description,
#                 expense_date
#             )

#             return True

#         except Exception as e:
#             return False, str(e)

#     # ==============================
#     # Total Expense
#     # ==============================
#     def get_total_expense(self, user_id):
#         return self.db.get_total_expense(user_id)

#     # ==============================
#     # Category Summary
#     # ==============================
#     def category_summary(self, user_id):
#         return self.db.category_summary(user_id)
from database.database import FinanceDatabase


class ExpenseManager:
    """
    Business logic for managing expenses.
    """

    def __init__(self):
        self.db = FinanceDatabase()

    # ==========================================
    # Add Expense
    # ==========================================
    def add_expense(
        self,
        user_id,
        category,
        amount,
        description,
        expense_date
    ):
        try:
            self.db.add_expense(
                user_id,
                category,
                amount,
                description,
                expense_date
            )
            return True, "Expense added successfully."

        except Exception as e:
            return False, str(e)

    # ==========================================
    # Get All Expenses
    # ==========================================
    def get_all_expenses(self, user_id):
        return self.db.get_all_expenses(user_id)

    # ==========================================
    # Get Single Expense
    # ==========================================
    def get_expense(self, expense_id):
        return self.db.get_expense(expense_id)

    # ==========================================
    # Update Expense
    # ==========================================
    def update_expense(
        self,
        expense_id,
        category,
        amount,
        description,
        expense_date
    ):
        try:
            self.db.update_expense(
                expense_id,
                category,
                amount,
                description,
                expense_date
            )

            return True, "Expense updated successfully."

        except Exception as e:
            return False, str(e)

    # ==========================================
    # Delete Expense
    # ==========================================
    def delete_expense(self, expense_id):
        try:
            self.db.delete_expense(expense_id)
            return True, "Expense deleted successfully."

        except Exception as e:
            return False, str(e)

    # ==========================================
    # Total Expense
    # ==========================================
    def get_total_expense(self, user_id):
        return self.db.get_total_expense(user_id)

    # ==========================================
    # Category Summary
    # ==========================================
    def category_summary(self, user_id):
        return self.db.category_summary(user_id)