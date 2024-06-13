import streamlit as st
import streamlit.components.v1 as components
import base64

# from streamlit_pdf_viewer import pdf_viewer
# è possibile utilizzare questo componente per gestire i file pdf
# https://github.com/lfoppiano/structure-vision/blob/main/streamlit_app.py

st.header(":blue[4 Machine learning]")
st.subheader("4.1 Checklist")


"""
import PyPDF2

file_path = "ChecklistProgettoMachineLearningPython.pdf"
if file_path is not None:
    # Read the PDF file
    pdf_reader = PdfReader(file_path)
    # Extract the content
    content = ""
    for page in range(pdf_reader.getNumPages()):
        content += pdf_reader.getPage(page).extractText()
    # Display the content
    st.write(content)
""" 
"""
pdf_file = "ChecklistProgettoMachineLearningPython.pdf"
base64_pdf = base64.b64encode(pdf_file.read()).decode('utf-8')
pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">' 
st.markdown(pdf_display, unsafe_allow_html=True)
"""

import base64
from pathlib import Path

pdf_path = Path("ChecklistProgettoMachineLearningPython.pdf")

base64_pdf = base64.b64encode(pdf_path.read_bytes()).decode("utf-8")
pdf_display = f"""
    <iframe src="data:application/pdf;base64,{base64_pdf}" width="800px" height="2100px" type="application/pdf"></iframe>
"""
st.markdown(pdf_display, unsafe_allow_html=True)
#with st.expander("**Checklist**"): 
     #st.page_link("\ChecklistProgettoMachineLearningPython.pdf", label="pdf", icon="🏠")
     #components.iframe("https://www.diariodiunanalista.it/posts/analisi-esplorativa-dei-dati-con-python-e-pandas/", height = 500, scrolling = True)
