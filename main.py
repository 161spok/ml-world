import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")
dati_caricati = False


def on_change(key):
    selection = st.session_state[key]
    st.write(f"Selection changed to {selection}")
    

def sidebar_menu():
    with st.sidebar:
        selected5 = option_menu(None, ["Home", "1 Problem definition", "2 Data", "3 Analisi dei dati", "4 Interpretazione dei dati", '5 Archiviazione e gestione dei dati','6 Visualizzazione dei dati'],
                        icons=['house', 'cloud-upload', 'cloud-upload', "building-fill", "list-task", 'gear'],
                        orientation="vertical")
    return selected5

selezionato = sidebar_menu()

match selezionato:
        case "Home":
            st.page_link("pages/home.py", label="Home")
            
        case "1 Problem definition":
            st.page_link("pages/problemdef.py", label="Problem definition")
            

        case "2 Data":
            
            
