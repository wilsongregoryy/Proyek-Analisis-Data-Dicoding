import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')



# Read data
product_count_df = pd.read_csv("product_count_data.csv")
customer_state_df = pd.read_csv("customer_state_data.csv")
seller_state_df = pd.read_csv("seller_state_data.csv")

st.header('Proyek Analisis Data: E-Commerce Public Dataset')


# Plot pertanyaan 1
st.subheader('Penjualan Kategori Produk')
fig, ax = plt.subplots(figsize=(16, 8))
colors_ = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3","#D3D3D3", "#D3D3D3"]
sns.barplot(
    x="counts", 
    y="products",
    data=product_count_df.sort_values(by="counts", ascending=False)[:10],
    palette=colors_,
    ax=ax
)
ax.set_title("10 Kategori Produk Teratas", loc="center", fontsize=15)
ax.set_ylabel(None)
ax.set_xlabel('Banyak Penjualan')
ax.tick_params(axis='y', labelsize=12)

st.pyplot(fig)


# Plot pertanyaan 2
st.subheader("5 Negara Bagian asal Pengguna/Customer Teratas")
 
fig, ax = plt.subplots(figsize=(16, 8))
 
colors_ = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    x="counts", 
    y="states",
    data=customer_state_df.sort_values(by="counts", ascending=False)[:5],
    palette=colors_,
    ax=ax
)
ax.set_title("5 Negara Bagian asal Pengguna/Customer Teratas", loc="center", fontsize=15)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=12)

st.pyplot(fig)


st.subheader("5 Negara Bagian asal Penjual/Seller Teratas")
fig, ax = plt.subplots(figsize=(16, 8))
colors_ = ["#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3", "#D3D3D3"]
sns.barplot(
    x="counts", 
    y="states",
    data=seller_state_df.sort_values(by="counts", ascending=False)[:5],
    palette=colors_,
    ax=ax
)
ax.set_title("5 Negara Bagian asal Penjual/Seller Teratas", loc="center", fontsize=15)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=12)
 
st.pyplot(fig)
