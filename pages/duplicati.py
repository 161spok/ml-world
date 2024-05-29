import streamlit as st

st.subheader("Rimozione dei duplicati")

uploaded_file = st.file_uploader("Scegli un file", key="pdf_uploader")
                
if st.button("Submit & Process", type="primary", key="process_button") :
            with st.spinner("Elaborazione ..."):
                                        st.success("Caricamento effettuato !") 
                                        if uploaded_file is not None:
                                            dati_caricati = True
                                            data = pd.read_csv(uploaded_file) #path folder of the data file
                                            st.write(data)
                                            # Check for duplicate rows
                                            duplicates = data.duplicated().sum()
                                            st.write("Number of duplicate rows:", duplicates)
                                      
                                            # Removing duplicate rows
                                            data.drop_duplicates(inplace=True)
                                            st.write(data)
