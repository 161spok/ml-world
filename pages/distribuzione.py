import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import io

st.subheader("Distribuzione dati")                                 

if 'dati' not in st.session_state:
  st.write("Session vuota")
else:  
  st.write(st.session_state.dati)
  df = st.session_state.df
  #st.write(df)
  st.dataframe(df)
  #  st.area_chart(df)
  #  st.bar_chart(df)
  #  st.line_chart(data=df)

  col1, col2 = st.columns(2)
  with col1:
    st.header("Head")
    st.write(df.head())
  
  with col2:
    st.header("Info")
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    st.text(s)
    
st.header("Conteggio") 
conteggio = df["Failure Type"].value_counts()
st.text(conteggio)

st.header("Valori univoci")
#univoci = df["Failure Type"].unique()
list_sub_category = df["Failure Type"].sort_values().unique().tolist()
st.text(list_sub_category)

