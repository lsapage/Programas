import pandas as pd
import streamlit as st

lista1 = ['Geeks', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks'] 
lista2 = [11, 22, 33, 44, 55, 66, 77]

base = pd.DataFrame(list(zip(lista1, lista2)), 
               columns =['Name', 'val'])


st.write("""
         
# Arquivo de teste

""")

st.dataframe(base)
