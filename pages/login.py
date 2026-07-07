import streamlit as st
from modules.authentication import Authentication

auth = Authentication()


def show_login():

    # ===============================
    # Session State
    # ===============================

    st.session_state.setdefault("auth_mode", "login")

    # ===============================
    # CSS
    # ===============================

    st.markdown("""
    <style>

    <style>

.stApp{
    background: #A8DCAB;
}

/* Hide Streamlit Menu */
#MainMenu{
    visibility:hidden;
}

header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

/* Title */

.title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#1B4332;
}

/* Subtitle */

.subtitle{
    text-align:center;
    color:#4F6F52;
    margin-bottom:25px;
}

/* Cards */

div[data-testid="stMetric"]{
    background:#6D8I96;
    border-radius:18px;
    padding:18px;
    border:1px solid #D8EFD3;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
}

/* Buttons */

.stButton>button{
    width:100%;
    background:#BBBDBC;
    color:BLACK;
    border:none;
    border-radius:12px;
    font-weight:600;
    height:45px;
}

.stButton>button:hover{
    background:#388E3C;
}

/* Text Input */

.stTextInput input,
.stNumberInput input,
.stDateInput input,
textarea{
    border-radius:10px;
    border:1px solid #B7D9B5;
}

/* Select Box */

.stSelectbox div{
    border-radius:10px;
}

/* DataFrame */

[data-testid="stDataFrame"]{
    border-radius:15px;
    background:BLACK;
}


    header{
        visibility:hidden;
    }

    footer{
        visibility:hidden;
    }

    .block-container{
        padding-top:1rem;
        padding-bottom:1rem;
        max-width:1200px;
    }

    .left-box{

        padding:60px 40px;
        color:black;

    }

    .left-box h1{

        font-size:52px;
        color:#4EA8FF;
        margin-bottom:5px;

    }

    .left-box h2{

        color:BLACK;
        margin-bottom:35px;

    }

    .feature{

        font-size:21px;
        padding:12px 0;

    }

    div[data-testid="stForm"]{

        background:#111827;

        border:1px solid #334155;

        border-radius:20px;

        padding:35px;

        box-shadow:0 15px 35px rgba(0,0,0,.35);

    }

    .switch{

        text-align:center;

        color:#CBD5E1;

        padding-top:15px;

    }

    </style>
    """, unsafe_allow_html=True)

    # ===============================
    # Layout
    # ===============================

    left, right = st.columns([1.3,1])

    # ===============================
    # LEFT SIDE
    # ===============================

    with left:

        st.markdown("""

        <div class="left-box">

        <h1>💰 AI Finance Advisor</h1>

        <h2>Smart Finance Powered by AI</h2>

        <div class="feature">🤖 AI Financial Advisor</div>

        <div class="feature">💰 Budget Planner</div>

        <div class="feature">📊 Expense Manager</div>

        <div class="feature">📈 Investment Calculator</div>

        <div class="feature">🧾 Receipt Scanner</div>

        <div class="feature">🏦 Loan Predictor</div>

        <div class="feature">📑 Financial Reports</div>

        </div>

        """, unsafe_allow_html=True)

    # ===============================
    # RIGHT SIDE
    # ===============================

    with right:

        # ================= LOGIN =================

        if st.session_state.auth_mode == "login":

            with st.form("login_form"):

                st.subheader("🔐 Login")

                username = st.text_input(
                    "Username"
                )

                password = st.text_input(
                    "Password",
                    type="password"
                )
                login = st.form_submit_button(
    "Login",
    use_container_width=True
)

                if login:

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

                            st.session_state.logged_in = True
                            st.session_state.user_id = user[0]
                            st.session_state.username = user[1]
                            st.session_state.page = "dashboard"

                            st.success(f"Welcome {user[1]}!")

                            st.rerun()

                        else:

                            st.error("Invalid username or password.")

            st.markdown(
                "<div class='switch'>Don't have an account?</div>",
                unsafe_allow_html=True
            )

            if st.button(
                "📝 Create Account",
                use_container_width=True
            ):
                st.session_state.auth_mode = "signup"
                st.rerun()

        # ================= SIGNUP =================

        else:

            with st.form("signup_form"):

                st.subheader("📝 Create Account")

                new_username = st.text_input(
                    "Username"
                )

                new_password = st.text_input(
                    "Password",
                    type="password"
                )

                confirm_password = st.text_input(
                    "Confirm Password",
                    type="password"
                )

                created_date = st.date_input(
                    "Date"
                )

                signup = st.form_submit_button(
                    "Create Account",
                    use_container_width=True
                )

                if signup:

                    if not new_username.strip():

                        st.error("Username is required.")

                    elif len(new_username.strip()) < 3:

                        st.error("Username must contain at least 3 characters.")

                    elif len(new_username.strip()) > 20:

                        st.error("Username cannot exceed 20 characters.")

                    elif not new_username.replace("_", "").isalnum():

                        st.error(
                            "Username can contain only letters, numbers and underscore (_)."
                        )

                    elif not new_password:

                        st.error("Password is required.")

                    elif len(new_password) < 8:

                        st.error("Password must be at least 8 characters.")

                    elif new_password != confirm_password:

                        st.error("Passwords do not match.")

                    else:

                        success = auth.register(
                            new_username.strip(),
                            new_password,
                            str(created_date)
                        )

                        if success:

                            st.success("✅ Account created successfully!")

                            st.session_state.auth_mode = "login"

                            st.rerun()

                        else:

                            st.error("Username already exists.")

            st.markdown(
                "<div class='switch'>Already have an account?</div>",
                unsafe_allow_html=True
            )

            if st.button(
                "🔐 Login",
                use_container_width=True
            ):
                st.session_state.auth_mode = "login"
                st.rerun()