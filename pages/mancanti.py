import streamlit as st
import pandas as pd

st.subheader("Rimozione dei dati mancanti")

if 'dati' not in st.session_state:
  pass
else:  
  st.write(st.session_state.dati)
  data = st.session_state.df

  # Check for missing rows
  missing_values = data.isna().sum()
  st.write("Missing Values:")
  st.write(missing_values)
  
