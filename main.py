import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")
dati_caricati = False

caricato = st.button('Home', key="primo")
if caricato:
         st.switch_page("pages/home.py")

    

           
