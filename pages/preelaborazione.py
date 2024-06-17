import streamlit as st
import streamlit.components.v1 as components

st.header(":blue[2 Data]")
st.subheader("2.1 Preelaborazione dati")

predati = st.text_area('DESCRIZIONE', 'Questa fase prevede la pulizia, il filtraggio e la trasformazione dei dati per renderli idonei per ulteriori analisi. '
'Ciò può includere la rimozione dei valori mancanti, il ridimensionamento o la normalizzazione dei dati o la loro conversione in un formato diverso.')

with st.expander("**Preparazione**"): 
     st.write('''I dati raccolti possono essere in una forma grezza che non può essere alimentata direttamente alla macchina.  
     Quindi, questo è un processo di raccolta di set di dati da diverse fonti, l\'analisi di questi set di dati e  
     quindi la costruzione di un nuovo set di dati per ulteriore elaborazione ed esplorazione. Questa preparazione 
     può essere eseguita manualmente o dall\' approccio automatico. I dati possono anche essere preparati in forme numeriche che velocizzerebbero l\' apprendimento del modello.  
     La pulizia e la qualità dei dati sono estremamente importanti in qualsiasi progetto di analisi dei dati. 
     I set di dati del mondo reale spesso presentano problemi, come dati mancanti, inconsistenti o errati, che possono compromettere l’accuratezza delle analisi e, di conseguenza, 
     le decisioni aziendali risultanti. Questo progetto, quindi, mira a realizzare una pulizia completa dei nostri dati di marketing digitale.
     Il processo di pulizia coinvolgerà diverse fasi critiche, incluse l’identificazione di dati mancanti, la correzione o l’eliminazione di tali record, se appropriato. 
     Affronteremo anche gli outlier, assicurando che i dati estremi non distorcano le nostre analisi. Inoltre, affronteremo la sfida di gestire dati ambigui o mal etichettati, 
     come valori sconosciuti nella nostra fonte di traffico. Tali dati saranno esaminati e trattati in modo appropriato, sia completandoli con l’informazione corretta, se disponibile, 
     oppure categorizzandoli separatamente per un’analisi successiva.
     La pulizia di questi dati prepara il terreno per un’analisi più precisa ed efficace delle campagne di marketing digitale. Con dati puliti e di alta qualità, siamo in grado di 
     ottenere insight più affidabili e prendere decisioni più informate. Durante la registrazione delle lezioni, il ChatGPT ha presentato errori, i quali sono stati mantenuti nei video 
     affinché possiate imparare anche cosa può andare storto, come identificarlo e correggerlo.''')
     
     st.image('Immagine1.png', caption='Processo analisi esplorativa dei dati')



st.markdown("**La preelaborazione dei dati (DATA PREPROCESSING TECHNIQUES) prevede i seguenti passi:**")

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



st.write(''':green-background[Data cleaning], :blue-background[Data transformation],  :red-background[Feature engineering]''')
st.write('''Data cleaning - Handling missing values ''')
st.write('''Data cleaning - Removing outliers ''')
st.write('''Data cleaning - Correcting errors ''')

st.write('''Data transformation - Feature scaling ''')
st.write('''Data transformation - Encoding categorical variables ''')
st.write('''Data transformation - Data normalization ''')

st.write('''Feature engineering - Feature selection ''')
st.write('''Feature engineering - Feature extraction ''')
st.write('''Feature engineering - Dimensonality reduction ''')

st.write('''EXPLORATORY DATA ANALYSIS (EDA)''')
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
#st.markdown(custom_css, unsafe_allow_html=True)
#st.markdown('<div class="my-container">This is a custom-styled container</div>', unsafe_allow_html=True)



with st.expander("**Distribuzione dei dati**"):
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
          metti in gruppi separati per colore.
''')    
     st.page_link("pages/distribuzione.py", label="Vai", icon="🌎") 
     components.iframe("https://ccaudek.github.io/bookdown_psicometria/chapter-descript.html#forma-di-una-distribuzione", height = 500, scrolling = True)

with st.expander("**:green-background[Data cleaning] Rimozione dei duplicati**"):
    st.write('''
        Rimuovere i duplicati è un'abilità essenziale 
        per ottenere conteggi accurati perché spesso non si desidera contare la stessa cosa più volte. In Python, ciò potrebbe essere ottenuto 
        utilizzando il modulo Pandas , che ha un metodo noto come drop_duplicates.
    ''')
      
with st.expander("**:green-background[Data cleaning] Correzione degli errori di struttura**"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')                       
  
 # https://www.diariodiunanalista.it/posts/come-identificare-anomalie-nei-tuoi-dati/
with st.expander("**:green-background[Data cleaning] Gestione dei valori anomali**"):
    st.write('''
        Metodo della Deviazione Standard:
Questo metodo identifica i valori anomali basandosi sulla deviazione standard dei dati.
Calcola la media e la deviazione standard per ciascuna variabile.
Considera come valori anomali quelli che si discostano da questa media di più di una certa soglia (ad esempio, 2 o 3 volte la deviazione standard).
''')
    st.code(f"""
    Esempio in Python
    
    import numpy as np\n
    threshold = 2  :green[# Soglia per considerare un valore come anomalo]\n
    mean, std = np.mean(dataset), np.std(dataset)\n
    outliers = dataset[(dataset - mean) > threshold * std]\n
    \n
    """)
    st.write('''
    Metodo dell’Intervallo Interquartile (IQR):\n
    L’IQR è la differenza tra il terzo quartile (75%) e il primo quartile (25%).\n
    I valori al di fuori di questo intervallo sono considerati anomali.\n
    \n
    ''')
    
    st.code(f"""
    Esempio in Python
    
    Q1 = dataset.quantile(0.25)\n
    Q3 = dataset.quantile(0.75)\n
    IQR = Q3 - Q1\n
    outliers = dataset[(dataset < (Q1 - 1.5 * IQR)) | (dataset > (Q3 + 1.5 * IQR))]\n
    \n
    """)

    st.write('''
    Rilevamento automatico dei valori anomali:\n
    Utilizza modelli di machine learning specifici per identificare valori anomali.\n
    Ad esempio, puoi utilizzare Isolation Forest o One-Class SVM.\n
    \n
    ''')
    
    st.code(f"""
    Esempio in Python
    
    from sklearn.ensemble import IsolationForest\n
    model = IsolationForest(contamination=0.05)  # Contaminazione = percentuale di valori anomali\n
    model.fit(dataset)\n
    outliers = model.predict(dataset) == -1\n
    """)
    
    st.write('''
    Ricorda che la scelta del metodo dipende dal contesto e dalla natura dei dati. Inoltre, è importante esaminare attentamente i valori identificati come anomali per evitare di rimuovere informazioni preziose.
        ''') 
    
    st.page_link("https://www.diariodiunanalista.it/posts/come-identificare-anomalie-nei-tuoi-dati/", label="Reference", icon="🏠")
    st.page_link("https://www.intelligenzaartificialeitalia.net/post/come-rimuovere-e-gestire-i-valori-anomali-con-python-nel-machine-learning", label="Reference", icon="🏠")

with st.expander("**:green-background[Data cleaning] Gestione dei dati mancanti**"):
    st.write('''
        I valori mancanti sono un problema comune nell'apprendimento automatico. Ciò si verifica quando una particolare variabile non dispone di punti dati, risultando in informazioni incomplete e potenzialmente danneggiando l'accuratezza e l'affidabilità dei modelli. È essenziale affrontare i valori mancanti in modo efficiente per garantire risultati forti e imparziali nei tuoi progetti di machine learning. In questo articolo vedremo come gestire i valori mancanti nei set di dati in Machine Learning .
        Cos'è un valore mancante?
        I valori mancanti sono punti dati assenti per una variabile specifica in un set di dati. Possono essere rappresentati in vari modi, ad esempio celle vuote, valori nulli o simboli speciali come "NA" o "sconosciuto". Questi punti dati mancanti rappresentano una sfida significativa nell’analisi dei dati e possono portare a risultati imprecisi o distorti.
    ''')                               
    st.page_link("https://www.geeksforgeeks.org/ml-handling-missing-values/?ref=header_search", label="Reference", icon="🏠")
    
with st.expander("**:blue-background[Data transformation] Operare su variabili categoriche**"):
    st.write('''
        All'interno di un dataset strutturato puoi trovare due tipologie di dati

        **Variabili quantitative continue:** numeri che indicano una quantità\n
        **Variabili qualiative ordinate (ordinali):** numeri o stringhe che rappresentano delle classi che possono essere ordinate\n
        **Variabili qualitative sconnesse (nominali):** numeri e stringhe rappresentanti classi che non hanno un ordine\n
        
        Le variabili qualitative possono essere rappresentate anche da stringhe, in questo caso bisogna codificarle all'interno di numeri per poterle usare come input per un algoritmo di machine learning. 
        In inglese le variabili qualitative sono conosciute come categorical variables (ordinal e nominal).
    ''') 
    st.image('tipologia_variabili.PNG', caption='')
    st.page_link("https://github.com/ProfAI/ml00/blob/master/2%20-%20Datasets%20e%20data%20preprocessing/Operare%20su%20variabili%20categoriche.ipynb", label="Variabili categoriche", icon="🏠")
    
with st.expander("**:blue-background[Data transformation]**"):
    st.write('''
        Il processo di trasformazione dei dati prevede la conversione, la pulizia e la strutturazione dei dati in un formato utilizzabile che viene utilizzato per analizzare per supportare i processi decisionali. Include la modifica del formato, dell'organizzazione o dei valori dei dati per prepararli all'utilizzo da parte di un'applicazione o all'analisi. Questo processo cruciale viene intrapreso dalle organizzazioni che cercano di sfruttare i propri dati per fornire approfondimenti aziendali tempestivi, garantendo che le informazioni siano accessibili, coerenti, sicure ed eventualmente riconosciute dagli utenti aziendali target.
        Le trasformazioni possono essere suddivise in due categorie: trasformazioni semplici e trasformazioni dati complesse.
        Le trasformazioni semplici dei dati includono procedure semplici che includono la pulizia dei dati, la standardizzazione, l'aggregazione e il filtraggio. Queste trasformazioni vengono spesso eseguite utilizzando semplici metodi di manipolazione dei dati e vengono spesso utilizzate per preparare i dati per l'analisi o il reporting.
        Le trasformazioni complesse dei dati includono processi più avanzati come l'integrazione, la migrazione, la replica e l'arricchimento dei dati. Queste trasformazioni spesso richiedono metodi complessi di manipolazione dei dati come la modellazione, la mappatura e la convalida dei dati e sono comunemente utilizzati per preparare i dati per applicazioni di analisi avanzata, machine learning o data warehousing.
    ''')  

with st.expander("**:green-background[Data cleaning] Pulizia dei dati di testo**"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')                                

with st.expander("**:blue-background[Data transformation] Formattazione dei dati**"):
    st.write('''
        La formattazione dei dati implica la conversione dei dati in un formato o struttura standard che può essere facilmente elaborata dagli algoritmi o dai modelli 
        utilizzati per l'analisi. Qui discuteremo le tecniche di formattazione dei dati comunemente utilizzate, ad esempio ridimensionamento e normalizzazione.
        Ridimensionamento
        Il ridimensionamento implica la trasformazione dei valori delle funzionalità in un intervallo specifico. Mantiene la forma della distribuzione originale pur modificando la scala.
        Particolarmente utile quando le caratteristiche hanno scale diverse e alcuni algoritmi sono sensibili alla grandezza delle caratteristiche.
        I metodi di ridimensionamento comuni includono il ridimensionamento Min-Max e la standardizzazione (ridimensionamento del punteggio Z).
        Ridimensionamento Min-Max
        Il ridimensionamento Min-Max ridimensiona i valori in un intervallo specificato, in genere tra 0 e 1. Preserva la distribuzione originale e garantisce che il valore minimo sia mappato su 0 e il valore massimo sia mappato su 1.
    ''') 

with st.expander("**:blue-background[Data transformation] Standardizzazione dei dati - Feature Scaling**"):
     st.write('''
        Nel Machine Learning, un modello sarà buono (o altrettanto cattivo) quanto i dati con cui lo addestri. L'entità delle diverse funzionalità influisce sui diversi modelli di machine learning per vari motivi.

        Ad esempio, considera un set di dati contenente due caratteristiche, età e reddito. Qui l’età varia da 0 a 100, mentre il reddito varia da 0 a un importo enorme, per lo più superiore a 100. Il reddito è circa 1.000 volte maggiore dell’età. Quindi, queste due funzionalità rientrano in intervalli molto diversi. Quando eseguiamo ulteriori analisi, come ad esempio la regressione lineare multivariata, il reddito attribuito influenzerà intrinsecamente maggiormente il risultato a causa del suo valore maggiore. Ma questo non significa necessariamente che sia più importante come predittore. Pertanto, la portata di tutti gli elementi dovrebbe essere ridimensionata in modo che ogni elemento contribuisca in modo approssimativamente proporzionale alla distanza finale.
        
    ''')
     st.page_link("https://towardsdatascience.com/normalization-vs-standardization-cb8fe15082eb", label="Reference", icon="🏠")                              
     st.page_link("https://github.com/ProfAI/ml00/blob/master/2%20-%20Datasets%20e%20data%20preprocessing/Portare%20i%20dati%20sulla%20stessa%20scala.ipynb", label="Reference", icon="🏠") 

with st.expander("**:blue-background[Data transformation] Codifica delle etichette**"):
     st.write('''
        La codifica delle etichette è una tecnica utilizzata per convertire le colonne categoriche in colonne numeriche in modo che possano essere adattate da modelli di apprendimento automatico che accettano solo dati numerici. Si tratta di un importante passaggio di pre-elaborazione in un progetto di machine learning.
    ''')  
     st.page_link("https://www.geeksforgeeks.org/ml-label-encoding-of-datasets-in-python/", label="Reference", icon="🏠")

with st.expander("**:blue-background[Data transformation] One-hot encoding**"):
     st.write('''
        Una codifica a caldo è una tecnica che utilizziamo per rappresentare le variabili categoriali come valori numerici in un modello di machine learning.
    ''')       
     st.page_link("https://www.geeksforgeeks.org/ml-one-hot-encoding/?ref=header_search", label="Reference", icon="🏠")

with st.expander("**Gestione dei dati sbilanciati con SMOTE e l'algoritmo Near Miss**"):
     st.write('''
        La Synthetic Minority Over-sampling TEchnique, o SMOTE in breve, è una tecnica di preelaborazione utilizzata per affrontare uno squilibrio di classi in un set di dati.
    ''') 
     st.page_link("https://medium.com/@corymaklin/synthetic-minority-over-sampling-technique-smote-7d419696b88c", label="Reference", icon="🏠")
     

with st.expander("**Trappola delle variabili fittizie nei modelli di regressione**"):
    st.write('''
        Prima di conoscere la trappola delle variabili fittizie, capiamo innanzitutto cos'è in realtà la variabile fittizia. 

        Variabile fittizia nei modelli di regressione: 
        nelle statistiche, soprattutto nei modelli di regressione, abbiamo a che fare con vari tipi di dati. I dati possono essere quantitativi (numerici) o qualitativi (categoriali). I dati numerici possono essere facilmente gestiti nei modelli di regressione ma non possiamo utilizzare direttamente i dati categorici, devono essere trasformati in qualche modo. 
        
        Per trasformare gli attributi categoriali in attributi numerici, possiamo utilizzare la procedura di codifica delle etichette (la codifica delle etichette assegna un intero univoco a ciascuna categoria di dati). Ma questa procedura non è l'unica adatta, quindi, una codifica a caldo viene utilizzata nei modelli di regressione successivi alla codifica dell'etichetta. Ciò ci consente di creare nuovi attributi in base al numero di classi presenti nell'attributo categoriale, ovvero se ci sono n numero di categorie nell'attributo categoriale, verranno creati n nuovi attributi. Questi attributi creati sono chiamati variabili fittizie . Pertanto, le variabili dummy sono variabili “proxy” per i dati categorici nei modelli di regressione. 
        Queste variabili fittizie verranno create con codifica one-hot e ciascun attributo avrà un valore pari a 0 o 1, che rappresenta la presenza o l'assenza di tale attributo. 
        
        Trappola delle variabili fittizie: 
        la trappola delle variabili fittizie è uno scenario in cui sono presenti attributi altamente correlati (multicollineari) e una variabile predice il valore delle altre. Quando utilizziamo la codifica one-hot per gestire i dati categorici, è possibile prevedere una variabile fittizia (attributo) con l'aiuto di altre variabili fittizie. Pertanto, una variabile fittizia è altamente correlata con altre variabili fittizie. L'utilizzo di tutte le variabili dummy per i modelli di regressione porta a una trappola delle variabili dummy . Pertanto, i modelli di regressione dovrebbero essere progettati per escludere una variabile fittizia. 
        
        Ad esempio – 
        Consideriamo il caso del genere avente due valori maschile (0 o 1) e femminile (1 o 0). Includere entrambe le variabili fittizie può causare ridondanza perché se una persona non è maschio in tal caso quella persona è una donna, quindi non è necessario utilizzare entrambe le variabili nei modelli di regressione. Questo ci proteggerà dalla trappola delle variabili fittizie.
    ''')  

with st.expander("**Corso**"): 
     st.page_link("https://github.com/ProfAI/ml00/blob/master/README.md", label="Corso", icon="🏠")
     

with st.expander("**Esempio 1**"): 
     st.page_link("https://www.diariodiunanalista.it/posts/analisi-esplorativa-dei-dati-con-python-e-pandas/", label="1 -Reference", icon="🏠")
     #st.page_link("pages/esempiouno.py", label="Vai a Esempio 2", icon="🌎") 
     components.iframe("https://www.diariodiunanalista.it/posts/analisi-esplorativa-dei-dati-con-python-e-pandas/", height = 500, scrolling = True)
     
 


