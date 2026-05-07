
import streamlit as st
import plotly.express as px
from data_processing import *


# =========================
# PAGE CONFIGURATION
# =========================

st.set_page_config(
    page_title="Executive Overview",
    page_icon="📊",
    layout="wide"
)


# =========================
# LOAD DATA
# =========================

df = load_data()


# =========================
# SIDEBAR FILTERS
# =========================

st.sidebar.header("🔍 Filter Dashboard")

store_locations = get_store_locations(df)

selected_store = st.sidebar.selectbox(
    "Select Store Location",
    ["All Stores"] + store_locations
)

if selected_store != "All Stores":
    df = filter_data(
        df,
        store_location=selected_store
    )


# =========================
# PAGE TITLE
# =========================

st.title("📊 Executive Overview")
st.markdown(
    "Business performance summary and high-level insights"
)

st.markdown("---")


# =========================
# KPI SECTION
# =========================

total_revenue = get_total_revenue(df)
total_transactions = get_total_transactions(df)
total_units = get_total_units_sold(df)
average_order = get_average_order_value(df)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "💰 Total Revenue",
        f"${total_revenue:,.2f}"
    )

with col2:
    st.metric(
        "🧾 Total Transactions",
        f"{total_transactions:,}"
    )

with col3:
    st.metric(
        "📦 Units Sold",
        f"{total_units:,}"
    )

with col4:
    st.metric(
        "🛒 Average Order Value",
        f"${average_order:,.2f}"
    )


st.markdown("---")


# =========================
# CATEGORY REVENUE CHART
# =========================

category_df = category_revenue(df)

fig_category = px.pie(
    category_df,
    names="product_category",
    values="revenue",
    hole=0.5,
    title="Revenue Distribution by Category"
)

fig_category.update_layout(
    title_x=0.25,
    template="plotly_white"
)


# =========================
# TOP REVENUE PRODUCTS
# =========================

top_products = top_revenue_products(df)

fig_products = px.bar(
    top_products,
    x="revenue",
    y="product_detail",
    orientation="h",
    title="Top Revenue Generating Products",
    text_auto=".2s"
)

fig_products.update_layout(
    yaxis=dict(categoryorder="total ascending"),
    template="plotly_white",
    title_x=0.2
)


# =========================
# DISPLAY CHARTS
# =========================

col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(
        fig_category,
        use_container_width=True
    )

with col2:
    st.plotly_chart(
        fig_products,
        use_container_width=True
    )


# =========================
# HOURLY SALES ANALYSIS
# =========================

hourly_sales = (
    df.groupby("hour")["revenue"]
    .sum()
    .reset_index()
)

fig_hourly = px.line(
    hourly_sales,
    x="hour",
    y="revenue",
    markers=True,
    title="Hourly Revenue Trend"
)

fig_hourly.update_layout(
    template="plotly_white",
    title_x=0.35
)

st.plotly_chart(
    fig_hourly,
    use_container_width=True
)


# =========================
# INSIGHTS SECTION
# =========================

st.markdown("---")

st.subheader("📌 Key Business Insights")

top_category = (
    category_df.iloc[0]["product_category"]
)

top_product = (
    top_products.iloc[0]["product_detail"]
)

st.success(
    f"""
    • Highest Revenue Category: {top_category}

    • Top Revenue Product: {top_product}

    • Peak business hours can be identified
      from the hourly revenue trend chart.

    • Revenue concentration insights help
      identify hero products driving profitability.
    """
)
