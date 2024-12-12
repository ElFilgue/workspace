from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import streamlit as st

st.title("Coffee Machine App")
st.write("Enjoy your coffee today!.")

col1, col2 = st.columns([1, 1])
with col1:
    option = st.selectbox("Enter Choice, (expresso, latte, cappuccino):", value='expresso')
with col2:
    lon = st.text_input("Enter Money:", value='0', format="%.2f", step=0.02)

fetch_button = st.button("Make Coffee")
