import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import io
import streamlit.components.v1 as components

st.subheader("Distribuzione dati")                                 

if 'dati' not in st.session_state:
  st.write("Session vuota")
else:  
  st.write(st.session_state.dati)
  with st.expander("**Distribuzione dati**"): #https://ccaudek.github.io/bookdown_psicometria/chapter-descript.html#forma-di-una-distribuzione
    st.write('''
            ''')
    components.iframe("https://paolapozzolo.it/distribuzione-normale/", height = 500, scrolling = True)

    st.page_link("https://ccaudek.github.io/bookdown_psicometria/chapter-descript.html#forma-di-una-distribuzione", label="1 - Reference", icon="🏠")
    st.page_link("https://www.geeksforgeeks.org/python-normal-distribution-in-statistics/", label="2 - Reference", icon="🏠")
    st.page_link("https://smartstrategy.eu/research/come-calcolare-media-e-deviazione-standard-con-python-per-principianti/", label="Media e deviazione standard (esempio con caricamento di un csv)", icon="🏠")
     
    st.page_link("https://community.sisense.com/t5/knowledge/test-for-normal-distribution-of-data-with-python/ta-p/9434", label="Test con Pandas", icon="🏠")
    
  df = st.session_state.df
  st.write("Test")
  st.write(df)
  st.write("-------------------------------------------------------------------------")
  #st.dataframe(df)
  #st.area_chart(df)
  #st.bar_chart(df)
  #st.line_chart(data=df)
  
  # -----------------------------------------distribuzione dei dati
  import numpy as np
  import matplotlib.pyplot as plt
  from scipy.stats import norm
  
  # Carica i dati dal file CSV
  #data = np.genfromtxt('dati.csv', delimiter=',')
  data = st.dataframe(df)
  # Calcola la media e la deviazione standard dei dati
  mean = np.mean(data)
  std_dev = np.std(data)
  
  # Calcola la densità di probabilità (PDF) della distribuzione normale
  x = np.linspace(mean - 3*std_dev, mean + 3*std_dev, 1000)
  pdf = norm.pdf(x, mean, std_dev)
  
  # Visualizza la PDF
  plt.plot(x, pdf)
  plt.title('Distribuzione Normale dei Dati')
  plt.xlabel('Valore')
  plt.ylabel('Probabilità')
  plt.show()
  #------------------------------------------------------------------------
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
  colonna = st.text_input("Su quale colonna occorre effettuare il conteggio ?")
  
  st.write(":blue[df['colonna'].value_counts()]")
  
                                                  #conteggio = df["Failure Type"].value_counts()
  if colonna:
    conteggio = df[colonna].value_counts()
    st.text(conteggio)
  
  st.header("Valori univoci ")
  univoco = st.text_input("Su quale colonna occorre estrarre il valore univoco ?")
  st.write(":blue[df['colonna'].sort_values().unique().tolist()]")#:blue[2 Data]
  if univoco:
                                                #univoci = df["Failure Type"].unique()
                                                #list_sub_category = df["Failure Type"].sort_values().unique().tolist()
    list_sub_category = df[univoco].sort_values().unique().tolist()
                                                #st.text(list_sub_category)
    st.write(list_sub_category)
  
  st.header("Raggruppamento ")
  raggruppamento = st.text_input("Su quale colonna occorre effettuare in raggruppamento ?")
  st.write(":blue[df.groupby('colonna')[\"Type\"].count()]")
  if raggruppamento:
    gruppo = df.groupby(raggruppamento)["Type"].count()
                                                #gruppo = df.groupby("Failure Type")["Type"].count()
                                                #st.text(gruppo)
    st.write(gruppo)

  st.header("Raggruppamento con media valori")
  raggruppamedia = st.text_input("Su quale colonna occorre effettuare in raggruppamento con media valori ?")
  if raggruppamedia:
    
    st.write(":blue[df.groupby('colonna').agg({'Air temperature [K]':'median', 'Process temperature [K]':'median'})]")
  
    gruppo2 = df.groupby('Failure Type').agg({"Air temperature [K]":"median", "Process temperature [K]":"median"})
    st.write(gruppo2)
