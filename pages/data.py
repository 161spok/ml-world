import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.header(":blue[2 Data]")
             
st.subheader("Raccolta dati")
dati = st.text_area('DESCRIZIONE', 'Questo è il processo di raccolta di dati da varie fonti, come sensori, database o altri sistemi. I dati possono essere strutturati o non strutturati e possono presentarsi in vari formati come testo, immagini o audio.')
uploaded_file = st.file_uploader("Scegli un file", key="pdf_uploader")
                
if st.button("Submit & Process", type="primary", key="process_button") :
            with st.spinner("Elaborazione ..."):
                                        st.success("Caricamento effettuato !") 
                                        if uploaded_file is not None:
                                            del st.session_state['dati']
                                            dati_caricati = True
                                            data = pd.read_csv(uploaded_file) #path folder of the data file
                                            st.write(data)
                                            if 'dati' not in st.session_state:
                                                    st.session_state['dati'] = 'caricati'
                                                    st.session_state.df = data
                                                    st.write(st.session_state.df.shape[0])
def click_button():
    st.switch_page("pages/preelaborazione.py")

#st.button("Preelaborazione dati", on_click=click_button)
     


