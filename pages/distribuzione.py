import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import io

st.subheader("Distribuzione dati")                                 


if 'dati' not in st.session_state:
  pass
else:  
  st.write(st.session_state.dati)
  df = st.session_state.df
  #st.write(df)
  st.dataframe(df)
  #  st.area_chart(df)
  #  st.bar_chart(df)
  #  st.line_chart(data=df)
  st.write(df.head())
  #------------------------
  buffer = io.StringIO()
  df.info(buf=buffer)
  s = buffer.getvalue()

  st.text(s)
