import pandas as pd
import streamlit as st

base = pd.read_csv('Base_Claro_teste.csv',sep=';',nrows=10)


st.write("""
         
# Arquivo de teste

""")

st.dataframe(base)