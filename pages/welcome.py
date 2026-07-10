import streamlit as st


def show_welcome():

    st.markdown("""
<style>

/* ======================================
Main Background
====================================== */

.stApp{
    background: linear-gradient(135deg,#F8FAFC,#EEF4FF);
}

/* ======================================
Hero Section
====================================== */

.hero{
    background:linear-gradient(135deg,#1E40AF,#2563EB);
    border-radius:22px;
    padding:40px 50px;
    text-align:center;
    color:white;
    margin-bottom:30px;
    box-shadow:0 10px 30px rgba(37,99,235,.25);
}

.hero h1{
    color:white;
    font-size:52px;
    font-weight:800;
    margin:0;
}

.hero h3{
    color:#E0E7FF;
    font-size:22px;
    margin-top:10px;
}

.hero p{
    color:#F8FAFC;
    font-size:18px;
    max-width:850px;
    margin:20px auto 0;
    line-height:1.7;
}


/* ======================================
Feature Cards
====================================== */

.card{
    background:#FFFFFF;
    border-radius:18px;
    border:1px solid #E5E7EB;
    box-shadow:0 6px 18px rgba(0,0,0,.08);

    padding:25px 20px;

    min-height:170px;
    display:flex;
    flex-direction:column;
    justify-content:center;
    align-items:center;

    text-align:center;

    transition:0.3s;
}

.card:hover{
    transform:translateY(-5px);
    box-shadow:0 12px 25px rgba(37,99,235,.15);
}

.icon{
    font-size:42px;
    margin-bottom:12px;
}

.title{
    font-size:24px;
    font-weight:700;
    color:#1E3A8A;
    margin-bottom:10px;
}

.card p{
    font-size:16px;
    color:#64748B;
    margin:0;
    line-height:1.5;
}
/* ======================================
Buttons
====================================== */

.stButton>button{
    width:100%;
    height:55px;
    border-radius:14px;
    border:none;
    background:linear-gradient(90deg,#2563EB,#3B82F6);
    color:white;
    font-size:18px;
    font-weight:700;
    transition:all .3s;
}

.stButton>button:hover{
    transform:translateY(-2px);
    box-shadow:0 12px 25px rgba(37,99,235,.35);
}

/* ======================================
Divider
====================================== */

hr{
    border:1px solid #E2E8F0;
}

/* ======================================
Hide Streamlit Extras
====================================== */

#MainMenu{
    visibility:hidden;
}

header{
    visibility:hidden;
}

footer{
    visibility:hidden;
}

</style>
""", unsafe_allow_html=True)
    st.markdown("""
<div class="hero">

<h1> AI Finance Advisor</h1>

<h3>Smart • Secure • Personalized</h3>

<p>
Manage your finances with Artificial Intelligence.

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
            <div class="icon">💵</div>
            <div class="title">Budget Planner</div>
            <p>Plan monthly budgets</p>
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