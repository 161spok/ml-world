import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")
dati_caricati = False

#caricato = st.button('Home', key="primo")
#if caricato:
#         st.switch_page("pages/home.py")

from st_pages import Page, show_pages, add_page_title

# Optional -- adds the title and icon to the current page
add_page_title()
"Home", "1 Problem definition", "2 Data", "3 Analisi dei dati", "4 Interpretazione dei dati", '5 Archiviazione e gestione dei dati','6 Visualizzazione dei dati'
# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("main.py", "Main", "🏠"),
        Page("pages/home.py", "Home", ":books:"),
        Page("pages/problemdef.py", "1 Problem definition", ":department_store:"),
        Page("pages/data.py", "2 Data", ":globe_with_meridians:"),   
        Page("pages/data.py", "3 Analisi dei dati", ":globe_with_meridians:"),  
        Page("pages/data.py", "4 Interpretazione dei dati", ":globe_with_meridians:"),
        Page("pages/data.py", "5 Archiviazione e gestione dei dati", ":globe_with_meridians:"),
        Page("pages/data.py", "6 Visualizzazione dei dati", ":globe_with_meridians:"),
        
    ]
)    

           
