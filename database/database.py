import sqlite3
print("FinanceDatabase loaded from:", __file__)


class FinanceDatabase:

    def __init__(self):
        self.connection = sqlite3.connect(
            "database/finance.db",
            check_same_thread=False
        )
        self.cursor = self.connection.cursor()
    

    # Create tables automatically
        self.create_users_table()
        self.create_expense_table()
    # ==========================================
# Create Users Table
# ==========================================
    def create_users_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            created_date TEXT NOT NULL
        )
        """)
        self.connection.commit()
    # ==========================================
    # Create Expenses Table
    # ==========================================
    def create_expense_table(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS expenses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            category TEXT,
            amount REAL,
            description TEXT,
            expense_date TEXT,
            FOREIGN KEY(user_id) REFERENCES users(id)
        )
        """)
        self.connection.commit()

    # ==========================================
    # Register User
    # ==========================================
    def register_user(self, username, password, created_date):
        try:

            self.cursor.execute("""
            INSERT INTO users(username, password, created_date)
            VALUES (?, ?, ?)
            """, (
                username,
                password,
                created_date
            ))

            self.connection.commit()

            return True

        except sqlite3.IntegrityError:
            return False

    # ==========================================
    # Get User
    # ==========================================
    def get_user(self, username):
        self.cursor.execute("""
        SELECT * FROM users
        WHERE username = ?
        """, (username,))

        return self.cursor.fetchone()

    # ==========================================
    # Get User By ID
    # ==========================================
    def get_user_by_id(self, user_id):
        self.cursor.execute("""
        SELECT * FROM users
        WHERE id = ?
        """, (user_id,))

        return self.cursor.fetchone()

    # ==========================================
    # Check Email Exists
    # ==========================================
    def username_exists(self, username):
        self.cursor.execute("""
        SELECT id FROM users
        WHERE username = ?
        """, (username,))

        return self.cursor.fetchone() is not None
    
    def add_expense(self, user_id, category, amount, description, expense_date):
        self.cursor.execute("""
        INSERT INTO expenses(user_id, category, amount, description, expense_date)
        VALUES (?, ?, ?, ?, ?)
        """, (user_id, category, amount, description, expense_date))

        self.connection.commit()

    def get_all_expenses(self, user_id):
        self.cursor.execute("""
        SELECT *
        FROM expenses
        WHERE user_id=?
        ORDER BY expense_date DESC
        """, (user_id,))

        return self.cursor.fetchall()
    def delete_expense(self, expense_id):
        self.cursor.execute("""
        DELETE FROM expenses
        WHERE id=?
        """, (expense_id,))

        self.connection.commit()


    def update_expense(
    self,
    expense_id,
    category,
    amount,
    description,
    expense_date
    ):
        try:

            query = """
            UPDATE expenses
            SET
                category=?,
                amount=?,
                description=?,
                expense_date=?
            WHERE id=?
            """

            self.connection.execute(
                query,
                (
                    category,
                    amount,
                    description,
                    expense_date,
                    expense_id
                )
            )

            self.connection.commit()

            return True

        except Exception as e:
            return False, str(e)

        self.connection.commit()
    def get_expense(self, expense_id):
        self.cursor.execute("""
        SELECT *
        FROM expenses
        WHERE id=?
        """, (expense_id,))

        return self.cursor.fetchone()
    def get_total_expense(self, user_id):
        self.cursor.execute("""
        SELECT SUM(amount)
        FROM expenses
        WHERE user_id=?
        """, (user_id,))

        total = self.cursor.fetchone()[0]

        return total if total else 0
    def category_summary(self, user_id):
        self.cursor.execute("""
        SELECT category,
            SUM(amount)
        FROM expenses
        WHERE user_id=?
        GROUP BY category
        """, (user_id,))

        return self.cursor.fetchall()      

    # ==========================================
    # Close Database
    # ==========================================
    def close_connection(self):
        self.connection.close()