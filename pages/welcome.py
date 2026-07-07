import streamlit as st


def show_welcome():

    st.markdown("""
    <style>

    .hero{
        background: linear-gradient(#4A4A4A);
        padding:45px;
        border-radius:25px;
        text-align:center;
        color:white;
        box-shadow:0 15px 35px rgba(0,0,0,.35);
        margin-bottom:35px;
    }

    .hero h1{
        font-size:55px;
        margin-bottom:10px;
        font-weight:800;
    }

    .hero h3{
        color:#CBCBCB;
        font-weight:400;
        margin-bottom:25px;
    }

    .card{
        background:#BAC095;
        border:1px solid #334155;
        border-radius:20px;
        padding:30px;
        text-align:center;
        color:black;
        height:170px;
    }

    .icon{
        font-size:42px;
        margin-bottom:15px;
    }

    .title{
        font-size:22px;
        font-weight:bold;
    }

    </style>
    """, unsafe_allow_html=True)

    # ---------------- Hero ---------------- #

    st.markdown("""
    <div class="hero">

    <h1> AI Finance Advisor</h1>

    <h3>Smart • Secure • Personalized</h3>

    <p style="font-size:20px;">
    Manage your finances with Artificial Intelligence.
    Budget smarter, track expenses, predict loans and receive AI-powered financial advice.
    </p>

    </div>
    """, unsafe_allow_html=True)

    # ---------------- Feature Cards ---------------- #

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="card">
        <div class="icon">🤖</div>
        <div class="title">AI Advisor</div>
        Smart financial guidance
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
       
        <div class="title">Budget Planner</div>
        Plan monthly budgets
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="card">
        <div class="icon">📊</div>
        <div class="title">Expense Tracker</div>
        Monitor daily spending
        </div>
        """, unsafe_allow_html=True)

    st.write("")

    col4, col5, col6 = st.columns(3)

    with col4:
        st.markdown("""
        <div class="card">
        <div class="icon">📈</div>
        <div class="title">Investment</div>
        Calculate returns
        </div>
        """, unsafe_allow_html=True)

    with col5:
        st.markdown("""
        <div class="card">
        <div class="icon">🧾</div>
        <div class="title">Receipt Scanner</div>
        Store receipts instantly
        </div>
        """, unsafe_allow_html=True)

    with col6:
        st.markdown("""
        <div class="card">
        <div class="icon">🏦</div>
        <div class="title">Loan Predictor</div>
        AI loan prediction
        </div>
        """, unsafe_allow_html=True)

    # ---------------- Buttons ---------------- #

    st.write("")
    st.write("")
    st.markdown("---")

    b1, b2 = st.columns(2)

    with b1:
        if st.button("🔐 Login", use_container_width=True, type="primary"):
            st.session_state.auth_mode = "login"
            st.session_state.page = "login"
            st.rerun()

    with b2:
        if st.button("📝 Create Account", use_container_width=True):
            st.session_state.auth_mode = "signup"
            st.session_state.page = "login"
            st.rerun()