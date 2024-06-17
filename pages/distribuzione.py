import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import io
import streamlit.components.v1 as components
from IPython.core.pylabtools import figsize

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
    
  #df = st.session_state.df
  df = st.session_state.['df']
  st.write("Test")
  st.write(df)
  st.write("-------------------------------------------------------------------------")
  
  # -----------------------------------------distribuzione dei dati
  import numpy as np
  import matplotlib.pyplot as plt
  from scipy.stats import norm
  
  # Carica i dati dal file CSV
  #st.dataframe(df)  # Same as st.write(df)
  #data = st.dataframe(df)
  
  # Calcola la media e la deviazione standard dei dati
  #mean = np.mean(data)
  #mean = data.mean(axis = 1, skipna = True)
  uploaded_file = st.file_uploader("Scegli un file", key="pdf_uploader")
  if st.button("Submit & Process", type="primary", key="process_button") :
            with st.spinner("Elaborazione ..."):
                                        st.success("Caricamento effettuato !") 
                                        if uploaded_file is not None:                                           
                                           
                                            data = pd.read_csv(uploaded_file) #path folder of the data file
                                            st.write(data)
                                            tdata = pd.DataFrame(data)
                                          
                                          # media tutte le colonne escluso quelle non numeriche
                                            media = tdata.mean(axis = 0, skipna = False, numeric_only=True)
                                          
                                          # media di colonne selezionate
                                            #mean1 = tdata.iloc[:,0].mean() #calcola la media della prima colonna
                                            mean2 = tdata.iloc[:,3].mean() # calcola la media della seconda colonna
                                            st.write("Media della colonna 4")
                                            st.write(mean2)
                                            
                                          # deviazione standard 
              # In generale, una deviazione standard alta indica una maggiore variabilità dei dati, mentre una deviazione standard bassa indica una minore variabilità.
                                            std_dev = tdata.std(numeric_only=True)
                                            st.write("Deviazione standard su tutte le colonne")
                                            st.write(std_dev)
                                          
                                          # deviazione standard su singola colonna
                                            std_dev_col = tdata.iloc[:,3].std()
                                            #  df['age'].std()
                                            st.write("Deviazione standard su colonna 4")
                                            st.write(std_dev_col)

                                            # Generate values for the x-axis
                                            # Calcola la densità di probabilità (PDF) della distribuzione normale
                                            x = np.linspace(media - 3*std_dev, media + 3*std_dev, 1000)
                                            pdf = norm.pdf(x, media, std_dev)
                                            
                                            # Visualizza la PDF
                                            plt.plot(x, pdf)
                                            plt.title('Distribuzione Normale dei Dati')
                                            plt.xlabel('Valore')
                                            plt.ylabel('Probabilità')
                                            st.pyplot(plt.gcf())
                                            
                                            #------------------------------------------------------------------------                                        
                                            x = np.linspace(0, 10000, 500)
                                            arr = data['Type']
                                            fig, ax = plt.subplots()
                                            plt.title('Distribuzione Normale dei Dati colonna Type')
                                            ax.hist(arr, bins=20)                                        
                                            st.pyplot(fig)
                                            #------------------------------------------------------------------------ 
                                            figsize(7, 5)
                                            plt.hist(data['Type'], color='blue', edgecolor='black', bins=int(45/1))
                                            plt.xlabel('Quantità')
                                            plt.ylabel('Tipologia')
                                            plt.title('Housing prices frequencies')
                                            st.pyplot(plt.gcf())

  
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
