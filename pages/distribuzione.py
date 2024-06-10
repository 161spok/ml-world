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
  with st.expander("**Distribuzione dati**"): #https://ccaudek.github.io/bookdown_psicometria/chapter-descript.html#forma-di-una-distribuzione
    st.write('''

    
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
    
  st.header("Conteggio ") 
  st.write(":blue[df[\"Failure Type\"].value_counts()]")
  conteggio = df["Failure Type"].value_counts()
  st.text(conteggio)
  
  st.header("Valori univoci ")
  st.write(":blue[df[\"Failure Type\"].sort_values().unique().tolist()]")#:blue[2 Data]
  #univoci = df["Failure Type"].unique()
  list_sub_category = df["Failure Type"].sort_values().unique().tolist()
  #st.text(list_sub_category)
  st.write(list_sub_category)
  
  st.header("Raggruppamento ")
  st.write(":blue[df.groupby(\"Failure Type\")[\"Type\"].count()]")
  gruppo = df.groupby("Failure Type")["Type"].count()
  #st.text(gruppo)
  st.write(gruppo)

  st.header("Raggruppamento con media valori")
  st.write(":blue[df.groupby('Failure Type').agg({'Air temperature [K]':'median', 'Process temperature [K]':'median'})]")
  gruppo2 = df.groupby('Failure Type').agg({"Air temperature [K]":"median", "Process temperature [K]":"median"})
  st.write(gruppo2)
