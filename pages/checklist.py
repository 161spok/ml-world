import streamlit as st
import streamlit.components.v1 as components
import base64
from streamlit_pdf_viewer import pdf_viewer

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


def ViewPDF(wch_fl):
    with open(wch_fl,"rb") as pdf_file:
        base64_pdf = base64.b64encode(pdf_file.read()).decode('utf-8')
        pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="1000" height="500" type="application/pdf">' 
        st.markdown(pdf_display, unsafe_allow_html=True)

#ViewPDF("./ChecklistProgettoMachineLearningPython.pdf") 
#ViewPDF("ChecklistProgettoMachineLearningPython.pdf") 
#-----------------------------------------------------------------------------------
vuoto = 0
st.session_state['binary'] = vuoto
uploaded_file = st.file_uploader("Upload a file",
                                 type=("pdf"),
                                 #on_change=new_file,
                                 help="The full-text is extracted using Grobid. ")
if uploaded_file:
    if not st.session_state['binary']:
        with (st.spinner('Reading file, calling Grobid...')):
            binary = uploaded_file.getvalue()            
            st.session_state['binary'] = binary
            
            pdf_viewer(
                            input=st.session_state['binary'],
                            width=width,
                            height=height,
                            annotations=annotations,
                            pages_vertical_spacing=pages_vertical_spacing,
                            annotation_outline_size=annotation_thickness,
                            pages_to_render=st.session_state['page_selection'],
                        )
#with st.expander("**Checklist**"): 
     #st.page_link("\ChecklistProgettoMachineLearningPython.pdf", label="pdf", icon="🏠")
     #components.iframe("https://www.diariodiunanalista.it/posts/analisi-esplorativa-dei-dati-con-python-e-pandas/", height = 500, scrolling = True)
