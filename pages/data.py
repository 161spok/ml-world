import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.header(":blue[2 Data]")
             
st.subheader("Raccolta dati")
dati = st.text_area('DESCRIZIONE', 'questo è il processo di raccolta di dati da varie fonti, come sensori, database o altri sistemi. I dati possono essere strutturati o non strutturati e possono presentarsi in vari formati come testo, immagini o audio.')
uploaded_file = st.file_uploader("Scegli un file", key="pdf_uploader")
                
if st.button("Submit & Process", key="process_button") :
            with st.spinner("Processing ..."):
                                        st.success("Done !") 
                                        if uploaded_file is not None:
                                            dati_caricati = True
                                            data = pd.read_csv(uploaded_file) #path folder of the data file
                                            st.write(data)
with st.container(border=True):
  col1, col2, col3, col4, col5 = st.columns(5)
  with col1:
    preelaborazione = st.button("Preelaborazione dati")
  with col2:
    analisi =         st.button("Analisi dei dati")
  with col3:
    interpretazione = st.button("Interpretazione dei dati")
  with col4:
    archiviazione =   st.button("Archiviazione e gestione dei dati")
  with col5:
    visualizzazione = st.button("Visualizzazione dei dati")                            
                            
if preelaborazione:
                st.subheader("Preelaborazione dati")
                predati = st.text_area('DESCRIZIONE', 'Questa fase prevede la pulizia, il filtraggio e la trasformazione dei dati per renderli idonei per ulteriori analisi. '
                'Ciò può includere la rimozione dei valori mancanti, il ridimensionamento o la normalizzazione dei dati o la loro conversione in un formato diverso.')
                st.text_area('Preparazione', 'I dati raccolti possono essere in una forma grezza che non può essere alimentata direttamente alla macchina. ' 
                'Quindi, questo è un processo di raccolta di set di dati da diverse fonti, l\'analisi di questi set di dati e ' 
                'quindi la costruzione di un nuovo set di dati per ulteriore elaborazione ed esplorazione. Questa preparazione ' 
                'può essere eseguita manualmente o dall\' approccio automatico. I dati possono anche essere preparati in forme ' 
                'numeriche che velocizzerebbero l\' apprendimento del modello. ' 
                'Esempio: Una immagine può essere convertita in una matrice di dimensioni NXN, il valore di ciascuna cella indicherà il pixel dell\' immagine.')
#---------------#                
                with st.container(border=True):
                              col1, col2, col3, col4, col5, col6, col7, col8  = st.columns([1,1,1,1,1,1,1,1])
                              with col1:
                                  duplicati = st.button("Rimozione dei duplicati")                                 
                              with col2:
                                  rimozione = st.button("Rimozione di osservazioni indesiderate")
                              with col3:
                                  correzione = st.button("Correzione degli errori di struttura")
                              with col4:
                                  anomali = st.button("Gestione dei valori anomali indesiderati")
                              with col5:
                                  mancanti = st.button("Gestione dei dati mancanti")
                              with col6:
                                  archiviazione = st.button("Trasformazione dei dati")
                              with col7:
                                  standardizzazione = st.button("Standardizzazione dei dati")
                              with col8:
                                  formattazione = st.button("Formattazione dei dati")
                              with col9:
                                  codifica = st.button("Codifica delle etichette")
#---------------#                              
                # Check for duplicate rows
                duplicates = data.duplicated().sum()
                st.write("Number of duplicate rows:", duplicates)
                                  
                # Removing duplicate rows
                data.drop_duplicates(inplace=True)
                st.write(data)
