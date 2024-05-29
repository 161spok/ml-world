import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.header(":blue[2 Data]")
             
st.subheader("Raccolta dati")
dati = st.text_area('DESCRIZIONE', 'questo è il processo di raccolta di dati da varie fonti, come sensori, database o altri sistemi. I dati possono essere strutturati o non strutturati e possono presentarsi in vari formati come testo, immagini o audio.')
uploaded_file = st.file_uploader("Scegli un file", key="pdf_uploader")
                
if st.button("Submit & Process", type="primary", key="process_button") :
            with st.spinner("Elaborazione ..."):
                                        st.success("Caricamento effettuato !") 
                                        if uploaded_file is not None:
                                            dati_caricati = True
                                            data = pd.read_csv(uploaded_file) #path folder of the data file
                                            st.write(data)
def click_button():
    st.write("preelaborazione")

# in container
with st.container(border=True):
      col1, col2, col3, col4, col5 = st.columns(5)
      with col1:
        #preelaborazione = st.button("Preelaborazione dati")
        st.page_link("pages/preelaborazione.py", label="Page 1", icon="1️⃣")
        #st.button("Preelaborazione dati", on_click=click_button)
      with col2:
        analisi =         st.button("Analisi dei dati")
      with col3:
        interpretazione = st.button("Interpretazione dei dati")
      with col4:
        archiviazione =   st.button("Archiviazione e gestione dei dati")
      with col5:
        visualizzazione = st.button("Visualizzazione dei dati")       



# out container


