import streamlit as st

st.subheader("Data - Preelaborazione dati")

predati = st.text_area('DESCRIZIONE', 'Questa fase prevede la pulizia, il filtraggio e la trasformazione dei dati per renderli idonei per ulteriori analisi. '
'Ciò può includere la rimozione dei valori mancanti, il ridimensionamento o la normalizzazione dei dati o la loro conversione in un formato diverso.')
st.text_area('Preparazione', 'I dati raccolti possono essere in una forma grezza che non può essere alimentata direttamente alla macchina. ' 
'Quindi, questo è un processo di raccolta di set di dati da diverse fonti, l\'analisi di questi set di dati e ' 
'quindi la costruzione di un nuovo set di dati per ulteriore elaborazione ed esplorazione. Questa preparazione ' 
'può essere eseguita manualmente o dall\' approccio automatico. I dati possono anche essere preparati in forme ' 
'numeriche che velocizzerebbero l\' apprendimento del modello. ' 
'Esempio: Una immagine può essere convertita in una matrice di dimensioni NXN, il valore di ciascuna cella indicherà il pixel dell\' immagine.')



st.write("La preelaborazione dei dati prevede i seguenti passi:")              

st.write("Rimozione dei duplicati")                                 
                             
st.write("Rimozione di osservazioni indesiderate")
                             
st.write("Correzione degli errori di struttura")
                             
st.write("Gestione dei valori anomali indesiderati")
                             
st.write("Gestione dei dati mancanti")
                             
st.write("Trasformazione dei dati")

st.write("Pulizia dei dati di testo")
                              
st.write("Standardizzazione dei dati")
                             
st.write("Formattazione dei dati")
                              
st.write("Codifica delle etichette")
#---------------# 

