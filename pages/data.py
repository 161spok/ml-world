import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.header(":blue[2 Data]")
             
st.subheader("Raccolta dati")
dati = st.text_area('DESCRIZIONE', 'Questo è il processo di raccolta di dati da varie fonti, come sensori, database o altri sistemi. I dati possono essere strutturati o non strutturati e possono presentarsi in vari formati come testo, immagini o audio.')
uploaded_file = st.file_uploader("Scegli un file", key="pdf_uploader")

@st.cache
def get_data_deputies():
  # Fetch data from URL here, and then clean it up.
     return pd.read_csv(os.path.join(os.getcwd(),'df_dep.csv'))

#d1 = fetch_and_clean_data(DATA_URL_1)
# Actually executes the function, since this is the first time it was
# encountered.

#d2 = fetch_and_clean_data(DATA_URL_1)
# Does not execute the function. Instead, returns its previously computed
# value. This means that now the data in d1 is the same as in d2.

#d3 = fetch_and_clean_data(DATA_URL_2)
# This is a different URL, so the function executes.

if st.button("Submit & Process", type="primary", key="process_button") :
            with st.spinner("Elaborazione ..."):
                                        st.success("Caricamento effettuato !") 
                                        if uploaded_file is not None:
                                            #del st.session_state['dati']
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
     


