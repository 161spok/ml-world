import streamlit as st
import pandas as pd

#from streamlit_option_menu import option_menu

#st.set_page_config(layout="wide")

from st_pages import Page, Section, show_pages, add_page_title

# Optional -- adds the title and icon to the current page
add_page_title()

@st.experimental_dialog("Cache")
def mess(item):
    st.cache_data.clear()
    #st.cache_resource.clear()
    st.write(f"Cache empty !")
    
    #if st.button("Ok"):        
        #st.rerun()


mess("A")

if 'dati' not in st.session_state:   
    #st.write("Sessione vuota")
    st.session_state['dati'] = 'caricati'
    #st.session_state.df = df

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("main.py", "Main", "🏠"),
        Page("pages/home.py",            "Home", ":books:"),
        Page("pages/problemdef.py",      "[1] Problem definition", ":department_store:"),
        #Section(name="SEZIONE  Data", icon=":globe_with_meridians:"),
        # Pages after a section will be indented
        Page("pages/data.py", "[2] Data", icon=":globe_with_meridians:"),
        Page("pages/preelaborazione.py", "[2.1] Preelaborazione", icon=":globe_with_meridians:"),
        # Unless you explicitly say in_section=False
        Page("pages/datacleaning.py",      "[2.1.0] Data cleaning ", icon=":chart_with_upwards_trend:"),
        Page("pages/distribuzione.py",     "[2.1.0.1] Distribuzione dei dati", icon=":chart_with_upwards_trend:"),
        Page("pages/categoriche.py",       "[2.1.0.2] Verifica di colonne categoriche e numeriche", icon=":chart_with_upwards_trend:"),
        Page("pages/duplicati.py",         "[2.1.0.3] Rimozione dei duplicati", icon=":chart_with_downwards_trend:"),
        Page("pages/indesiderate.py",      "[2.1.0.4] Correzione degli errori di struttura", icon=":memo:"),
        Page("pages/anomali.py",           "[2.1.0.5] Gestione dei valori anomali", icon=":signal_strength:"),
        Page("pages/mancanti.py",          "[2.1.0.6] Gestione dei mancanti", icon=":signal_strength:"),
        Page("pages/trasformazione.py",    "[2.1.0.7] Trasformazione dei dati", icon=":signal_strength:"),
        Page("pages/puliziadatitesto.py",  "[2.1.0.8] Pulizia dei dati di testo", icon=":signal_strength:"),
        Page("pages/standardizzazione.py", "[2.1.0.9] Standardizzazione dei dati - feature scaling", icon=":signal_strength:"),
        Page("pages/codificaetichette.py", "[2.1.0.10] Codifica delle etichette", icon=":signal_strength:"),
        Page("pages/onehot.py",            "[2.1.0.11] One-hot encoding", icon=":signal_strength:"),
        Page("pages/datisbilanciati.py",   "[2.1.0.12] Gestione dei dati sbilanciati", icon=":signal_strength:"),
        Page("pages/trappola.py",          "[2.1.0.13] Trappola delle variabili fittizie nei modelli di regressione", icon=":signal_strength:"),
        
        Page("pages/analisi.py",         "[2.2] Analisi dei dati", ":arrows_counterclockwise:", in_section=False),  
        Page("pages/interpretazione.py", "[2.3] Interpretazione dei dati", ":desktop_computer:", in_section=False),
        Page("pages/archiviazione.py",   "[2.4] Archiviazione e gestione dei dati", ":oil_drum:", in_section=False),
        Page("pages/visualizzazione.py", "[2.5] Visualizzazione dei dati", ":red_envelope:", in_section=False),
        Page("pages/evaluation.py",      "[3] Evaluation", ":hourglass_flowing_sand:", in_section=False),
        Page("pages/appo.py",            "[x] Counter", ":hourglass_flowing_sand:", in_section=False),
    ]
)    
file = st.sidebar.file_uploader('Upload',type=["pdf","txt"])         

