import streamlit as st
import openpyxl as ox
import pandas as pd

df  = pd.read_excel("abc.xlsx",sheet_name=0)

st.dataframe(df)