import stramlit as st

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
                              col1, col2, col3, col4, col5, col6, col7, col8, col9  = st.columns([1,1,1,1,1,1,1,1,1])
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

