import streamlit as st

st.title("Metodologia da seguire")

st.markdown(''':blue-background[E' un processo iterativo] ''')
st.image('imag.png', caption='Processo')
st.write("1 - Quale problema stiamo tentando di risolvere ?")
st.write("2 - Quali dati abbiamo ?")
st.write("3 - Cosa definisce il successo ?")
st.write("4 - Quali caratteristiche dobbiamo modellare ?")
st.write("5 - Quale tipo di modello dovremmo utilizzare ?")
st.write("6 - Cosa abbiamo sperimentato / cosa altro dobbiamo fare ?")
st.write("----------------------------------------------------------------------------")


st.page_link("https://www.geeksforgeeks.org/machine-learning/?ref=shm", label="Vai a Corso Machine Learning", icon="🌎")


st.markdown(''':blue-background[I passi del processo sono quindi i seguenti:] ''')

st.write("1 - Problem definition")
st.write("2 - Data")
st.write("3 - Evaluation")
st.write("4 - Features")
st.write("5 - Modelling")
st.write("6 - Experiments")

# Custom CSS to inject
custom_css = """
<style>
.my-container {
 background-color: #AED6F1;
 padding: 10px;
 border-radius: 5px;
}
</style>
"""

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Use the custom class in a container
st.markdown('<div class="my-container">This is a custom-styled container</div>', unsafe_allow_html=True)

