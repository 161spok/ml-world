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

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("main.py", "Main", "🏠"),
        Page("pages/home.py", "home", ":books:"),
        Page("pages/data.py", "data", ":books:"),   
        Page("pages/problemdef.py", "definizione", ":books:"),     
    ]
)    

           
