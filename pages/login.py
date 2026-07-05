import streamlit as st
from modules.authentication import Authentication

st.set_page_config(
    page_title="Login",
    page_icon="🔐",
    layout="centered"
)

# If already logged in
if st.session_state.get("logged_in"):
    st.success(f"Welcome, {st.session_state['user_name']}")
    st.switch_page("pages/dashboard.py")
    st.stop()

auth = Authentication()

st.title("🔐 AI Finance Advisor")

tab1, tab2 = st.tabs(["Login", "Sign Up"])

# ==================================================
# LOGIN
# ==================================================

with tab1:

    st.subheader("Login")

    username = st.text_input(
        "Username",
        key="login_username"
    )

    password = st.text_input(
        "Password",
        type="password",
        key="login_password"
    )

    if st.button("Login", use_container_width=True):

        if not username.strip():
            st.error("Please enter your username.")

        elif not password:
            st.error("Please enter your password.")

        else:

            user = auth.login(
                username.strip(),
                password
            )

            if user:

                st.session_state["logged_in"] = True
                st.session_state["user_id"] = user[0]
                st.session_state["user_name"] = user[1]

                st.success(f"Welcome {user[1]}!")
                st.switch_page("pages/dashboard.py")

            else:
                st.error("Invalid username or password.")

# ==================================================
# SIGN UP
# ==================================================

with tab2:

    st.subheader("Create Account")

    username = st.text_input(
        "Username",
        key="signup_username"
    )

    password = st.text_input(
        "Password",
        type="password",
        key="signup_password"
    )

    confirm_password = st.text_input(
        "Confirm Password",
        type="password",
        key="signup_confirm"
    )

    if st.button("Create Account", use_container_width=True):

        if not username.strip():
            st.error("Username is required.")

        elif len(username.strip()) < 3:
            st.error("Username must be at least 3 characters.")

        elif len(username.strip()) > 20:
            st.error("Username cannot exceed 20 characters.")

        elif not username.replace("_", "").isalnum():
            st.error("Username can contain only letters, numbers and underscore (_).")

        elif not password:
            st.error("Password is required.")

        elif len(password) < 8:
            st.error("Password must be at least 8 characters.")

        elif password != confirm_password:
            st.error("Passwords do not match.")

        else:

            success = auth.register(
                username.strip(),
                password
            )

            if success:
                st.success("✅ Account created successfully!")
            else:
                st.error("Username already exists.")