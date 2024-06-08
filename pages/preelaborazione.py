import streamlit as st
import streamlit.components.v1 as components

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
st.markdown(
    '''
    <style>
    .streamlit-expanderHeader {
        background-color: grey;
        color: black; # Adjust this for expander header color
    }
    .streamlit-expanderContent {
        background-color: grey;
        color: black; # Expander content color
    }
    </style>
    ''',
    unsafe_allow_html=True
) 

#components.iframe("https://ccaudek.github.io/bookdown_psicometria/chapter-descript.html#forma-di-una-distribuzione", height = 500, scrolling = True)

with st.expander("**Distribuzione dati**"): #https://ccaudek.github.io/bookdown_psicometria/chapter-descript.html#forma-di-una-distribuzione
    st.write('''
        Immagina che tu abbia una grande ciotola di caramelle di diversi colori e vuoi sapere quale colore c’è di più. Allora inizi a separare 
        le caramelle per colore: rosse, blu, verdi, ecc. Dopo averle separate, conti quante caramelle ci sono di ogni colore. Magari scopri che hai 
        molte caramelle rosse, alcune blu e poche verdi.

La “distribuzione dei dati” è un po’ come separare e contare le caramelle. In statistica, invece di caramelle, abbiamo numeri o informazioni che vogliamo 
organizzare. Ad esempio, se stiamo guardando i voti di una classe in matematica, potremmo vedere quanti studenti hanno preso un 6, un 7, un 8, ecc. Questo 
ci aiuta a capire rapidamente come sono distribuiti i voti: se molti studenti hanno voti alti, bassi o se sono distribuiti in modo uniforme.

A volte, quando mettiamo questi numeri in un grafico, possiamo vedere una forma speciale che assomiglia a una campana. Questa forma ci dice che la maggior 
parte dei dati si trova vicino al centro e meno dati si trovano ai lati, proprio come la maggior parte delle caramelle potrebbe essere rossa e solo alcune 
blu o verdi1.

Quindi, la distribuzione dei dati ci aiuta a vedere come sono organizzate le informazioni, proprio come quando organizzi le tue caramelle per colore per 
capire quale colore hai di più! È un modo per rendere le informazioni facili da capire, proprio come è più facile sapere quanti tipi di caramelle hai se le 
metti in gruppi separati per colore
    ''')
    components.iframe("https://paolapozzolo.it/distribuzione-normale/", height = 500, scrolling = True)

    st.page_link("https://ccaudek.github.io/bookdown_psicometria/chapter-descript.html#forma-di-una-distribuzione", label="Reference", icon="🏠")
  
                             
with st.expander("**Rimozione dei duplicati**"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')
      

with st.expander("**Rimozione di osservazioni indesiderate**"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')          
  

with st.expander("**Correzione degli errori di struttura**"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')                       
  
 # https://www.diariodiunanalista.it/posts/come-identificare-anomalie-nei-tuoi-dati/
with st.expander("**Gestione dei valori anomali**"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''') 
    st.page_link("https://www.diariodiunanalista.it/posts/come-identificare-anomalie-nei-tuoi-dati/", label="Reference", icon="🏠")
  

with st.expander("**Gestione dei dati mancanti**"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')                               

with st.expander("**Trasformazione dei dati**"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')  

with st.expander("**Pulizia dei dati di testo**"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')                                

with st.expander("**Standardizzazione dei dati - Feature Scaling**"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')                               

with st.expander("**Formattazione dei dati**"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')                                

with st.expander("**Codifica delle etichette**"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')  

with st.expander("**One-hot encoding**"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')  

with st.expander("**Gestione dei dati sbilanciati con SMOTE e l'algoritmo Near Miss**"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')  

with st.expander("**Trappola delle variabili fittizie nei modelli di regressione**"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')  
         


