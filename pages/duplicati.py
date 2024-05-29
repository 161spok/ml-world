import streamlit as st
import pandas as pd

st.subheader("Rimozione dei duplicati")

if 'dati' not in st.session_state:
  pass
else:  
  st.write(st.session_state.dati)
  tmpdati = st.session_state.dati
  data = pd.dataframe(tmpdati)

  # Check for duplicate rows
  duplicates = data.duplicated().sum()
  st.write("Number of duplicate rows:", duplicates)
                                      
  # Removing duplicate rows
  data.drop_duplicates(inplace=True)
                                            
