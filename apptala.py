import streamlit as st

st.title("محاسبه قیمت")

prices = []

for i in range(3):
    x = st.number_input(f"قیمت {i+1}", min_value=0, step=1)
    prices.append(x)

if st.button("محاسبه"):

    bishtarin = max(prices)
    kamtarin = min(prices)
    miangin = sum(prices) / len(prices)

    st.write("کمترین:", kamtarin)
    st.write("بیشترین:", bishtarin)
    st.write("میانگین:", miangin)
