import bcrypt
from database.database import FinanceDatabase


class Authentication:

    def __init__(self):
        self.db = FinanceDatabase()
        

    # =====================================
    # Register
    # =====================================

    def register(self, username, password):

        if self.db.username_exists(username):
            return False

        hashed_password = bcrypt.hashpw(
            password.encode(),
            bcrypt.gensalt()
        )

        return self.db.register_user(
            username,
            hashed_password.decode()
        )

    # =====================================
    # Login
    # =====================================

    def login(self, username, password):

        user = self.db.get_user(username)

        if user is None:
            return None

        # user = (id, username, password)
        stored_password = user[2]

        if bcrypt.checkpw(
            password.encode(),
            stored_password.encode()
        ):
            return user

        return None