import streamlit as st
import streamlit.components.v1 as components

st.header(":blue[4 Machine learning]")
st.subheader("4.1 Checklist")

with st.expander("**Checklist**"): 
     st.page_link("\ChecklistProgettoMachineLearningPython.pdf", label="pdf", icon="🏠")
     #components.iframe("https://www.diariodiunanalista.it/posts/analisi-esplorativa-dei-dati-con-python-e-pandas/", height = 500, scrolling = True)
