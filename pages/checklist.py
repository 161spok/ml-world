import streamlit as st
import streamlit.components.v1 as components

# from streamlit_pdf_viewer import pdf_viewer
# è possibile utilizzare questo componente per gestire i file pdf
# https://github.com/lfoppiano/structure-vision/blob/main/streamlit_app.py

st.header(":blue[4 Machine learning]")
st.subheader("4.1 Checklist")

import PyPDF2
file = "ChecklistProgettoMachineLearningPython.pdf"
if file is not None:
    # Read the PDF file
    pdf_reader = PdfReader(file)
    # Extract the content
    content = ""
    for page in range(pdf_reader.getNumPages()):
        content += pdf_reader.getPage(page).extractText()
    # Display the content
    st.write(content)

#with st.expander("**Checklist**"): 
     #st.page_link("\ChecklistProgettoMachineLearningPython.pdf", label="pdf", icon="🏠")
     #components.iframe("https://www.diariodiunanalista.it/posts/analisi-esplorativa-dei-dati-con-python-e-pandas/", height = 500, scrolling = True)
