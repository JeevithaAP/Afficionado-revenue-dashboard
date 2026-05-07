import streamlit as st
import base64


# =====================================
# PAGE CONFIGURATION
# =====================================

st.set_page_config(
    page_title="Afficionado Coffee Roasters",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =====================================
# LOAD IMAGE FUNCTION
# =====================================

def get_base64(image_path):
    with open(image_path, "rb") as img:
        return base64.b64encode(img.read()).decode()


banner = get_base64("images/coffee_banner.jpg")


# =====================================
# CUSTOM CSS
# =====================================

st.markdown(f"""
<style>

/* Main App Background */
.stApp {{
    background: linear-gradient(to right, #140F0C, #2A1B14);
    color: #F5F5F5;
}}


/* Sidebar */
section[data-testid="stSidebar"] {{
    background-color: #120D0A;
    border-right: 1px solid #3E2C23;
}}


/* Sidebar Text */
section[data-testid="stSidebar"] * {{
    color: white !important;
}}


/* Hero Banner */
.hero-section {{
    background-image:
        linear-gradient(
            rgba(0,0,0,0.65),
            rgba(0,0,0,0.65)
        ),
        url("data:image/jpg;base64,{banner}");

    background-size: cover;
    background-position: center;
    padding: 90px 50px;
    border-radius: 25px;
    text-align: center;
    margin-bottom: 35px;
    box-shadow: 0px 6px 30px rgba(0,0,0,0.4);
}}


/* Main Title */
.hero-title {{
    font-size: 58px;
    font-weight: bold;
    color: #F8E7D2;
    margin-bottom: 15px;
}}


/* Subtitle */
.hero-subtitle {{
    font-size: 24px;
    color: #F3D7B6;
}}


/* Glass Cards */
.glass-card {{
    background: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0px 4px 25px rgba(0,0,0,0.25);
    margin-bottom: 25px;
}}


/* Section Titles */
.section-title {{
    font-size: 32px;
    font-weight: bold;
    color: #F8E7D2;
    margin-bottom: 20px;
}}


/* Module Cards */
.module-card {{
    background: rgba(255,255,255,0.04);
    padding: 22px;
    border-radius: 18px;
    margin-bottom: 18px;
    border-left: 5px solid #C08B5C;
    transition: 0.3s ease;
}}

.module-card:hover {{
    transform: translateY(-5px);
    background: rgba(255,255,255,0.08);
}}


/* Footer */
.footer {{
    text-align: center;
    color: #D7B899;
    margin-top: 40px;
    font-size: 15px;
}}

</style>
""", unsafe_allow_html=True)


# =====================================
# HERO SECTION
# =====================================

st.markdown(f"""
<div class="hero-section">

<div class="hero-title">
☕ Afficionado Coffee Roasters
</div>

<div class="hero-subtitle">
Product Optimization & Revenue Contribution Analysis
</div>

</div>
""", unsafe_allow_html=True)


# =====================================
# PROJECT OVERVIEW
# =====================================

st.markdown('<div class="glass-card">', unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
📌 Project Overview
</div>
""", unsafe_allow_html=True)

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


# =====================================
# DASHBOARD MODULES
# =====================================

st.markdown("""
<div class="section-title">
📊 Dashboard Modules
</div>
""", unsafe_allow_html=True)

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


# =====================================
# FOOTER
# =====================================

st.markdown("""
<div class="footer">
Developed using Streamlit | Data Analytics Project
</div>
""", unsafe_allow_html=True)
