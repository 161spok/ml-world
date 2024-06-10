import streamlit as st
import pandas as pd

st.subheader("Rimozione dei duplicati")

if 'dati' not in st.session_state:
  pass
else:  
  st.write(st.session_state.dati)
  data = st.session_state.df

  st.page_link("https://www.geeksforgeeks.org/python-pandas-dataframe-drop_duplicates/", label="1 -Reference", icon="🏠")
  
  #data = pd.dataframe(tmpdati)

  # Check for duplicate rows
  duplicates = data.duplicated().sum()
  st.write("Number of duplicate rows:", duplicates)
                                      
  # Removing duplicate rows
  data = data.drop_duplicates(inplace=True)
  st.session_state.df = data # il nuovo dataset viene salvato in sessione                                          
  st.write(data.shape())
