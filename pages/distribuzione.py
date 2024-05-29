import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

st.subheader("Distribuzione dati")
dati = st.text_area('DESCRIZIONE', 'Questo è il processo di raccolta di dati da varie fonti, come sensori, database o altri sistemi. I dati possono essere strutturati o non strutturati e possono presentarsi in vari formati come testo, immagini o audio.')
uploaded_file = st.file_uploader("Scegli un file", key="pdf_uploader")
                
if st.button("Submit & Process", type="primary", key="process_button") :
            with st.spinner("Elaborazione ..."):
                                        st.success("Caricamento effettuato !") 
                                        if uploaded_file is not None:
                                            dati_caricati = True
                                            data = pd.read_csv(uploaded_file) #path folder of the data file
                                            st.write(data)
                                            data.plot()
                                            #plt.boxplot(data)
                                            plt.show()
                                            #plt.hist(data)
                                            #plt.show()

'''
if 'dati' not in st.session_state:
  pass
else:  
  st.write(st.session_state.dati)
  data = st.session_state.df
  st.write(data)

  fig = plt.figure(figsize =(10, 7))
  plt.boxplot(data)
  plt.show()
  plt.hist(data)
  plt.show()
  #tips = sns.load_dataset('data')
  #tips.plot()
'''
