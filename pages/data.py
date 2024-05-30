import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.header(":blue[2 Data]")
             
st.subheader("Raccolta dati")
dati = st.text_area('DESCRIZIONE', 'Questo è il processo di raccolta di dati da varie fonti, come sensori, database o altri sistemi. I dati possono essere strutturati o non strutturati e possono presentarsi in vari formati come testo, immagini o audio.')
uploaded_file = st.file_uploader("Scegli un file", key="pdf_uploader")

@st.cache
def load_data(uploaded_file):
    data = pd.read_csv(uploaded_file) #path folder of the data file
    return df

#d1 = load_data(DATA_URL_1)
# Actually executes the function, since this is the first time it was
# encountered.

#d2 = load_data(DATA_URL_1)
# Does not execute the function. Instead, returns its previously computed
# value. This means that now the data in d1 is the same as in d2.

#d3 = load_data(DATA_URL_2)
# This is a different URL, so the function executes.

if st.button("Submit & Process", type="primary", key="process_button") :
            with st.spinner("Elaborazione ..."):
                                        st.success("Caricamento effettuato !") 
                                        if uploaded_file is not None:                                           
                                            dati_caricati = True
                                            df = load_data(uploaded_file)
                                            #data = pd.read_csv(uploaded_file) #path folder of the data file
                                            st.write(data)
                                            if 'dati' not in st.session_state:
                                                    st.session_state['dati'] = 'caricati'
                                                    st.session_state.df = data
                                                    st.write(st.session_state.df.shape[0])

