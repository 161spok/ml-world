import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.header(":blue[2 Data]")
             
st.subheader("Raccolta dati")
dati = st.text_area('DESCRIZIONE', 'Questo è il processo di raccolta di dati da varie fonti, come sensori, database o altri sistemi. I dati possono essere strutturati o non strutturati e possono presentarsi in vari formati come testo, immagini o audio.')
uploaded_file = st.file_uploader("Scegli un file", key="pdf_uploader")


#----------------------------------------------------------------------------------
import streamlit.components.v1 as components
from streamlit_modal import Modal

modal = Modal(
    "Demo Modal", 
    key="demo-modal",
    
    # Optional
    padding=20,    # default value
    max_width=744  # default value
)

open_modal = st.button("Open")
if open_modal:
    modal.open()

if modal.is_open():
    with modal.container():
        st.write("Text goes here")

        html_string = '''
        <h1>HTML string in RED</h1>

        <script language="javascript">
          document.querySelector("h1").style.color = "red";
        </script>
        '''
        components.html(html_string)

        st.write("Some fancy text")
        value = st.checkbox("Check me")
        st.write(f"Checkbox checked: {value}")
#---------------------------------------------------------------------------------

@st.experimental_dialog("Cache")
def mess(item):
    st.write(f"Cache empty !")
    
    if st.button("Ok"):        
        st.rerun()
#----------------------------------------------------------------------------------
@st.cache
def load_data(uploaded_file):
    st.cache_data.clear()
    #mess("A")
  
    st.cache_resource.clear()
    df=""
    df = pd.read_csv(uploaded_file) #path folder of the data file
    if 'dati' not in st.session_state:
                                                    st.session_state['dati'] = 'caricati'
                                                    st.session_state.df = df
                                                    #st.write(st.session_state.df.shape[0])
                                                    st.write(st.session_state['dati'])
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
                                            data = load_data(uploaded_file)
                                            #data = pd.read_csv(uploaded_file) #path folder of the data file
                                            st.write(data)
                                            
                                            #if 'dati' not in st.session_state:
                                            #        st.session_state['dati'] = 'caricati'
                                            #        st.session_state.df = data
                                            #        st.write(st.session_state.df.shape[0])

