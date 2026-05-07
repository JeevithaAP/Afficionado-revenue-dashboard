import streamlit as st


# ======================================
# PAGE CONFIGURATION
# ======================================

st.set_page_config(
    page_title="Afficionado Coffee Roasters",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ======================================
# CUSTOM CSS STYLING
# ======================================

st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(to right, #1B120D, #2B1D17);
    color: #F5F5F5;
}


/* Sidebar Styling */
section[data-testid="stSidebar"] {
    background-color: #140F0C;
    border-right: 1px solid #3E2C23;
}


/* Sidebar Text */
section[data-testid="stSidebar"] * {
    color: #F5F5F5 !important;
}


/* Main Title */
.main-title {
    font-size: 52px;
    font-weight: bold;
    color: #F8E7D2;
    text-align: center;
    margin-bottom: 10px;
}


/* Subtitle */
.sub-title {
    font-size: 24px;
    color: #D7B899;
    text-align: center;
    margin-bottom: 40px;
}


/* Glass Card Effect */
.glass-card {
    background: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.1);
    box-shadow: 0px 4px 30px rgba(0,0,0,0.3);
    margin-bottom: 25px;
}


/* Dashboard Section Heading */
.section-title {
    font-size: 30px;
    color: #F8E7D2;
    margin-bottom: 15px;
    font-weight: bold;
}


/* Module Cards */
.module-card {
    background-color: rgba(255,255,255,0.04);
    padding: 18px;
    border-radius: 15px;
    margin-bottom: 15px;
    border-left: 5px solid #C08B5C;
    transition: 0.3s ease;
}

.module-card:hover {
    transform: scale(1.02);
    background-color: rgba(255,255,255,0.08);
}


/* Footer */
.footer {
    text-align: center;
    color: #C7B299;
    margin-top: 40px;
    font-size: 15px;
}

</style>
""", unsafe_allow_html=True)


# ======================================
# HEADER SECTION
# ======================================

st.markdown(
    """
    <div class="main-title">
        ☕ Afficionado Coffee Roasters
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="sub-title">
        Product Optimization & Revenue Contribution Analysis
    </div>
    """,
    unsafe_allow_html=True
)


# ======================================
# PROJECT OVERVIEW
# ======================================

st.markdown('<div class="glass-card">', unsafe_allow_html=True)

st.markdown(
    """
    <div class="section-title">
        📌 Project Overview
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown("""
This analytics dashboard helps Afficionado Coffee Roasters identify:

- Best-selling and least-selling products
- Revenue-driving categories and products
- Product popularity vs profitability
- Revenue concentration patterns
- Menu optimization opportunities

The dashboard supports data-driven business decisions
for improving operational efficiency and maximizing profitability.
""")

st.markdown('</div>', unsafe_allow_html=True)


# ======================================
# DASHBOARD MODULES
# ======================================

st.markdown(
    """
    <div class="section-title">
        📊 Dashboard Modules
    </div>
    """,
    unsafe_allow_html=True
)

modules = [
    ("📈 Executive Overview",
     "Business KPIs and overall performance summary"),

    ("🛍️ Product Performance",
     "Top-selling and least-selling product analysis"),

    ("💰 Revenue Contribution",
     "Revenue share and profitability insights"),

    ("📦 Category Analysis",
     "Category-level revenue and sales distribution"),

    ("🎯 Pareto Analysis",
     "80/20 revenue concentration and menu optimization")
]

for title, desc in modules:
    st.markdown(
        f"""
        <div class="module-card">
            <h3>{title}</h3>
            <p>{desc}</p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ======================================
# FOOTER
# ======================================

st.markdown(
    """
    <div class="footer">
        Developed using Streamlit | Data Analytics Project
    </div>
    """,
    unsafe_allow_html=True
)
