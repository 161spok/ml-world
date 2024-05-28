import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")
dati_caricati = False

st.button('Home', key="primo")
if st.button("Home", key="secondo"):
         st.switch_page("pages/home.py")

    

           
