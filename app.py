import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Data Storytelling App", layout="wide")

url = "https://raw.githubusercontent.com/leonism/sample-superstore/master/data/superstore.csv"
df = pd.read_csv(url)

df.dropna(subset=["Customer ID"], inplace=True)
df.drop_duplicates(inplace=True)

df["Order Date"] = pd.to_datetime(df["Order Date"])

st.title("Data Storytelling App - Superstore Sales Insights")

st.header("Dataset Introduction")

st.write("Dataset Shape")
st.write(df.shape)

st.write("Columns")
st.write(df.columns)

st.write("First 5 Rows")
st.dataframe(df.head())

st.write("Last 5 Rows")
st.dataframe(df.tail())

st.write("Missing Values")
st.dataframe(df.isnull().sum())

st.write("Statistical Summary")
st.dataframe(df.describe())

st.header("Exploratory Data Analysis")

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
total_customers = df["Customer ID"].nunique()

c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Sales", f"₹{total_sales:,.0f}")
c2.metric("Total Profit", f"₹{total_profit:,.0f}")
c3.metric("Total Orders", total_orders)
c4.metric("Total Customers", total_customers)

region_sales = df.groupby("Region")["Sales"].sum().reset_index()

fig1 = px.bar(
region_sales,
x="Region",
y="Sales",
title="Sales by Region"
)

st.plotly_chart(fig1, use_container_width=True)

category_profit = df.groupby("Category")["Profit"].sum().reset_index()

fig2 = px.bar(
category_profit,
x="Category",
y="Profit",
title="Profit by Category"
)

st.plotly_chart(fig2, use_container_width=True)

df["Year"] = df["Order Date"].dt.year

year_sales = df.groupby("Year")["Sales"].sum().reset_index()

fig3 = px.line(
year_sales,
x="Year",
y="Sales",
markers=True,
title="Year-wise Sales Trend"
)

st.plotly_chart(fig3, use_container_width=True)

segment_sales = df.groupby("Segment")["Sales"].sum().reset_index()

fig4 = px.pie(
segment_sales,
names="Segment",
values="Sales",
title="Sales by Customer Segment"
)

st.plotly_chart(fig4, use_container_width=True)

top_products = (
df.groupby("Product Name")["Sales"]
.sum()
.sort_values(ascending=False)
.head(10)
.reset_index()
)

fig5 = px.bar(
top_products,
x="Sales",
y="Product Name",
orientation="h",
title="Top 10 Products by Sales"
)

st.plotly_chart(fig5, use_container_width=True)

st.header("Insights and Findings")

st.success("West region generated the highest sales.")
st.success("Technology category contributed significantly to profit.")
st.success("Sales increased steadily over the years.")
st.success("Consumer segment contributed the largest share of sales.")
st.success("Top-selling products generated a major portion of revenue.")

st.header("Conclusion and Recommendations")

st.write("""

1. Focus marketing efforts on high-performing regions.

2. Maintain inventory for top-selling products.

3. Promote profitable categories.

4. Improve performance in low-sales regions.

5. Use customer segmentation for targeted marketing campaigns.
   """)
