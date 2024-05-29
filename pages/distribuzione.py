import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

st.subheader("Distribuzione dati")                                 


if 'dati' not in st.session_state:
  pass
else:  
  st.write(st.session_state.dati)
  data = st.session_state.df
  st.write(data)
  st.area_chart(data)
  
  

