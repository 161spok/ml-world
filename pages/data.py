import streamlit as st
import pandas as pd

st.header(":blue[2 Data]")
             
st.subheader("1 Raccolta dati")
dati = st.text_area('DESCRIZIONE', 'questo è il processo di raccolta di dati da varie fonti, come sensori, database o altri sistemi. I dati possono essere strutturati o non strutturati e possono presentarsi in vari formati come testo, immagini o audio.')
uploaded_file = st.file_uploader("Scegli un file", key="pdf_uploader")
                
if st.button("Submit & Process", key="process_button") :
                                with st.spinner("Processing ..."):
                                        st.success("Done !") 
                                        if uploaded_file is not None:
                                            dati_caricati = True
                                            data = pd.read_csv(uploaded_file) #path folder of the data file
                                            st.write(data)

preelaborazione = st.button("2 Preelaborazione dati")

analisi =         st.button("3 Analisi dei dati")

interpretazione = st.button("4 Interpretazione dei dati")

archiviazione =   st.button("5 Archiviazione e gestione dei dati")

visualizzazione = st.button("6 Visualizzazione dei dati")                            
                            
if preelaborazione:
                st.subheader("2 Preelaborazione dati")
                predati = st.text_area('DESCRIZIONE', 'Questa fase prevede la pulizia, il filtraggio e la trasformazione dei dati per renderli idonei per ulteriori analisi. '
                'Ciò può includere la rimozione dei valori mancanti, il ridimensionamento o la normalizzazione dei dati o la loro conversione in un formato diverso.')
                st.text_area('Preparazione', 'I dati raccolti possono essere in una forma grezza che non può essere alimentata direttamente alla macchina. ' 
                'Quindi, questo è un processo di raccolta di set di dati da diverse fonti, l\'analisi di questi set di dati e ' 
                'quindi la costruzione di un nuovo set di dati per ulteriore elaborazione ed esplorazione. Questa preparazione ' 
                'può essere eseguita manualmente o dall\' approccio automatico. I dati possono anche essere preparati in forme ' 
                'numeriche che velocizzerebbero l\' apprendimento del modello. ' 
                'Esempio: Una immagine può essere convertita in una matrice di dimensioni NXN, il valore di ciascuna cella indicherà il pixel dell\' immagine.')

                col1, col2, col3, col4, col5, col6, col7, col8  = st.columns([1,1,1,1,1,1,1,1])
                with col1:
                    raccolta = st.button("1 Rimozione di osservazioni indesiderate")
                with col2:
                    preelaborazione = st.button("2 Correzione degli errori di struttura")
                with col3:
                    analisi = st.button("3 Gestione dei valori anomali indesiderati")
                with col4:
                    interpretazione = st.button("4 Gestione dei dati mancanti")
                with col5:
                    archiviazione = st.button("5 Trasformazione dei dati")
                with col6:
                    visualizzazione = st.button("6 Standardizzazione dei dati")
                with col7:
                    archiviazione = st.button("7 Formattazione dei dati")
                with col8:
                    visualizzazione = st.button("8 Codifica delle etichette")
