import pandas as pd
import numpy as np


# =========================
# LOAD & CLEAN DATA
# =========================

def load_data():
    df = pd.read_csv("coffee_sales.csv")

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower()

    # Remove duplicates
    df = df.drop_duplicates()

    # Remove invalid quantity and price rows
    df = df[
        (df["transaction_qty"] > 0) &
        (df["unit_price"] > 0)
    ]

    # Convert transaction time
    df["transaction_time"] = pd.to_datetime(
        df["transaction_time"],
        format="%H:%M:%S",
        errors="coerce"
    )

    # Create hour column
    df["hour"] = df["transaction_time"].dt.hour

    # Create revenue column
    df["revenue"] = (
        df["transaction_qty"] *
        df["unit_price"]
    )

    return df


# =========================
# EXECUTIVE KPIs
# =========================

def get_total_revenue(df):
    return round(df["revenue"].sum(), 2)


def get_total_transactions(df):
    return df["transaction_id"].nunique()


def get_total_units_sold(df):
    return int(df["transaction_qty"].sum())


def get_average_order_value(df):
    return round(
        df["revenue"].sum() /
        df["transaction_id"].nunique(),
        2
    )


# =========================
# PRODUCT PERFORMANCE
# =========================

def top_selling_products(df, top_n=10):
    return (
        df.groupby("product_detail")["transaction_qty"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )


def least_selling_products(df, top_n=10):
    return (
        df.groupby("product_detail")["transaction_qty"]
        .sum()
        .sort_values(ascending=True)
        .head(top_n)
        .reset_index()
    )


def top_revenue_products(df, top_n=10):
    return (
        df.groupby("product_detail")["revenue"]
        .sum()
        .sort_values(ascending=False)
        .head(top_n)
        .reset_index()
    )


# =========================
# CATEGORY ANALYSIS
# =========================

def category_revenue(df):
    category_df = (
        df.groupby("product_category")["revenue"]
        .sum()
        .reset_index()
    )

    total_revenue = category_df["revenue"].sum()

    category_df["revenue_share_percent"] = (
        category_df["revenue"] / total_revenue
    ) * 100

    return category_df.sort_values(
        by="revenue",
        ascending=False
    )


def category_quantity(df):
    return (
        df.groupby("product_category")["transaction_qty"]
        .sum()
        .reset_index()
        .sort_values(
            by="transaction_qty",
            ascending=False
        )
    )


# =========================
# PRODUCT TYPE ANALYSIS
# =========================

def product_type_revenue(df):
    return (
        df.groupby(
            ["product_category", "product_type"]
        )["revenue"]
        .sum()
        .reset_index()
        .sort_values(
            by="revenue",
            ascending=False
        )
    )


# =========================
# REVENUE CONTRIBUTION
# =========================

def revenue_contribution_analysis(df):
    revenue_df = (
        df.groupby("product_detail")["revenue"]
        .sum()
        .reset_index()
    )

    total_revenue = revenue_df["revenue"].sum()

    revenue_df["revenue_contribution_percent"] = (
        revenue_df["revenue"] / total_revenue
    ) * 100

    revenue_df = revenue_df.sort_values(
        by="revenue",
        ascending=False
    )

    return revenue_df


# =========================
# PARETO ANALYSIS
# =========================

def pareto_analysis(df):
    pareto_df = (
        df.groupby("product_detail")["revenue"]
        .sum()
        .reset_index()
    )

    pareto_df = pareto_df.sort_values(
        by="revenue",
        ascending=False
    )

    pareto_df["cumulative_revenue"] = (
        pareto_df["revenue"].cumsum()
    )

    total_revenue = pareto_df["revenue"].sum()

    pareto_df["cumulative_percentage"] = (
        pareto_df["cumulative_revenue"] /
        total_revenue
    ) * 100

    return pareto_df


# =========================
# STORE LOCATION FILTER
# =========================

def get_store_locations(df):
    return sorted(
        df["store_location"]
        .dropna()
        .unique()
    )


# =========================
# FILTER DATA
# =========================

def filter_data(
    df,
    store_location=None,
    product_category=None
):

    if store_location:
        df = df[
            df["store_location"] == store_location
        ]

    if product_category:
        df = df[
            df["product_category"] == product_category
        ]

    return df
