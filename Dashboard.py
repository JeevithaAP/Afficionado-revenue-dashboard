
import streamlit as st


# =========================
# PAGE CONFIGURATION
# =========================

st.set_page_config(
    page_title="Afficionado Coffee Roasters",
    page_icon="☕",
    layout="wide"
)


# =========================
# CUSTOM STYLING
# =========================

st.markdown("""
<style>

.main {
    background-color: #F8F5F2;
}

h1, h2, h3 {
    color: #3E2723;
    font-family: 'Arial';
}

.stMetric {
    background-color: white;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0px 2px 8px rgba(0,0,0,0.08);
}

.sidebar .sidebar-content {
    background-color: #EFE7DD;
}

</style>
""", unsafe_allow_html=True)


# =========================
# HEADER SECTION
# =========================

st.title("☕ Afficionado Coffee Roasters")
st.subheader(
    "Product Optimization & Revenue Contribution Analysis"
)

st.markdown("---")


# =========================
# PROJECT DESCRIPTION
# =========================

st.markdown("""
### 📌 Project Overview

This analytics dashboard helps Afficionado Coffee Roasters identify:

- Best-selling and least-selling products
- Revenue-driving categories and products
- Product popularity vs profitability
- Revenue concentration patterns
- Menu optimization opportunities

The dashboard supports data-driven business decisions
for improving operational efficiency and maximizing profitability.
""")


# =========================
# DASHBOARD NAVIGATION
# =========================

st.markdown("---")

st.markdown("""
## 📊 Dashboard Modules

Use the sidebar to navigate through the analytics dashboards:

### 1️⃣ Executive Overview
Business KPIs and overall performance summary

### 2️⃣ Product Performance
Top-selling and least-selling product analysis

### 3️⃣ Revenue Contribution
Revenue share and profitability insights

### 4️⃣ Category Analysis
Category-level revenue and sales distribution

### 5️⃣ Pareto Analysis
80/20 revenue concentration and menu optimization
""")


# =========================
# FOOTER
# =========================

st.markdown("---")

st.caption(
    "Developed using Streamlit | Data Analytics Project"
)
