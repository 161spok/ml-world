import streamlit as st

st.header(":blue[2 Data]")
st.subheader("2.1 Preelaborazione dati")

predati = st.text_area('DESCRIZIONE', 'Questa fase prevede la pulizia, il filtraggio e la trasformazione dei dati per renderli idonei per ulteriori analisi. '
'Ciò può includere la rimozione dei valori mancanti, il ridimensionamento o la normalizzazione dei dati o la loro conversione in un formato diverso.')
st.text_area('Preparazione', 'I dati raccolti possono essere in una forma grezza che non può essere alimentata direttamente alla macchina. ' 
'Quindi, questo è un processo di raccolta di set di dati da diverse fonti, l\'analisi di questi set di dati e ' 
'quindi la costruzione di un nuovo set di dati per ulteriore elaborazione ed esplorazione. Questa preparazione ' 
'può essere eseguita manualmente o dall\' approccio automatico. I dati possono anche essere preparati in forme ' 
'numeriche che velocizzerebbero l\' apprendimento del modello. ' 
'Esempio: Una immagine può essere convertita in una matrice di dimensioni NXN, il valore di ciascuna cella indicherà il pixel dell\' immagine.')



#st.write("La preelaborazione dei dati prevede i seguenti passi:")
st.markdown("**La preelaborazione dei dati prevede i seguenti passi:**")

# -------------------------------------------- https://www.geeksforgeeks.org/ml-handling-imbalanced-data-with-smote-and-near-miss-algorithm-in-python/
#st.write("Distribuzione dati")  
with st.expander("Distribuzione dati"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')
    st.image("https://static.streamlit.io/examples/dice.jpg")
  
#st.write("Rimozione dei duplicati")                                 
with st.expander("Rimozione dei duplicati"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')
      
#st.write("Rimozione di osservazioni indesiderate")
with st.expander("Rimozione di osservazioni indesiderate"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')          
  
#st.write("Correzione degli errori di struttura")
with st.expander("Correzione degli errori di struttura"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')                       
  
#st.write("Gestione dei valori anomali")
with st.expander("Gestione dei valori anomali"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')  
  
#st.write("Gestione dei dati mancanti")
with st.expander("Gestione dei dati mancanti"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')                               
#st.write("Trasformazione dei dati")
with st.expander("Trasformazione dei dati"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')  
#st.write("Pulizia dei dati di testo")
with st.expander("Pulizia dei dati di testo"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')                                
#st.write("Standardizzazione dei dati - Feature Scaling")
with st.expander("Standardizzazione dei dati - Feature Scaling"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')                               
#st.write("Formattazione dei dati")
with st.expander("Formattazione dei dati"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')                                
#st.write("Codifica delle etichette")
with st.expander("Codifica delle etichette"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')  
#st.write("One-hot encoding")
with st.expander("One-hot encoding"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')  
#st.write("Gestione dei dati sbilanciati con SMOTE e l'algoritmo Near Miss")
with st.expander("Gestione dei dati sbilanciati con SMOTE e l'algoritmo Near Miss"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')  
#st.write("Trappola delle variabili fittizie nei modelli di regressione")
with st.expander("Trappola delle variabili fittizie nei modelli di regressione"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')  
         
#---------------# 

