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

with st.expander("**Esempio 1**"): 
     st.page_link("https://www.diariodiunanalista.it/posts/analisi-esplorativa-dei-dati-con-python-e-pandas/", label="1 -Reference", icon="🏠")
     components.iframe("https://www.diariodiunanalista.it/posts/analisi-esplorativa-dei-dati-con-python-e-pandas/", height = 500, scrolling = True)
     
with st.expander("**Esempio 2**"): 
#https://it.linkedin.com/pulse/guida-completa-alla-pulizia-dei-dati-csv-leonardo-anello-btj2f
    st.write('''
    Il dataset presenta i seguenti problemi:

- Righe duplicate
- ID duplicati
- Valori mancanti
- Valori anomali (Outliers)

:green[**CODICE**]\n
import pandas as pd\n


file_path = 'data.csv'\n
data = pd.read_csv(file_path)\n

:green[Ottenimento delle dimensioni del dataset]\n
dimensioni = data.shape\n

:green[Visualizzazione delle prime righe del dataset per comprendere la struttura dei dati]\n
prime_righe = data.head()\n

dimensioni\n
(1004, 12) \n

:green[Traduzione delle etichette del dataset originale in italiano]\n
:green[Traduzione delle etichette del dataset originale in italiano con underscore case]\n

traduzioni_originali = {\n
    'ID da Campanha': 'id_della_campagna',\n
    'Nome da Campanha': 'nome_della_campagna',\n
    'Data de Início': 'data_di_inizio',\n
    'Data de Término': 'data_di_fine',\n
    'Orçamento da Campanha (R$)': 'budget_della_campagna_r',\n
    'Canal': 'canale',\n
    'Impressões': 'impressioni',\n
    'Cliques': 'click',\n
    'Conversões': 'conversioni',\n
    'Pageviews': 'visualizzazioni_pagina',\n
    'Fonte do Tráfego': 'fonte_del_traffico',\n
    'Bounce Rate': 'tasso_di_rimbalzo'\n
}\n

:green[Applicazione delle traduzioni con underscore case al dataset originale]\n
data2 = data.rename(columns=traduzioni_originali)\n        

:green[Dettaglio dei Dati]\n
describe = data2.describe(include='all')\n
describe\n        

**id_della_campagna**: ID numerico delle campagne, varia da 1 a 1000.\n
**nome_della_campagna**: Nomi unici delle campagne, con 999 valori unici e una massima frequenza di 2 per “Balanced asymmetric architecture”.\n
**data_di_inizio e data_di_fine**: Date di inizio e fine delle campagne. Presentano diverse date uniche.\n
**budget_della_campagna_r**: Budget delle campagne in Reais brasiliani, con un valore medio di circa 25.043, una deviazione standard di 14.187 e valori che variano da circa 1.042 a 49.982.\n
**canale**: Canale di marketing utilizzato, con 5 categorie uniche. “Email” è il più frequente.\n
**impressioni**: Numero di impressioni, con una media di circa 62.384, una deviazione standard molto elevata (293.482) e un range che va da 1.001 a 1.975.723.\n
**click**: Numero di click, con una media di 554 e un range da 101 a 998.\n
**conversioni**: Numero di conversioni, con una media di 103 e un range da 10 a 200.\n
**visualizzazioni_pagina**: Numero di visualizzazioni pagina, con una media di circa 5.419 e un range da 1.009 a 9.996.\n
**fonte_del_traffico**: Fonte del traffico, con 5 categorie uniche e “Direto” come la più frequente.\n
**tasso_di_rimbalzo**: Tasso di rimbalzo, con una media di 0.516 e un range da 0 a 1.\n

:green[Record Duplicati]\n

:green[Utilizzo di duplicated() per trovare i record duplicati]\n
keep=False :green[segnala tutte le occorrenze dei record duplicati]\n
duplicati = data2[data2.duplicated(keep=False)]\n

duplicati \n       


Mantenere righe duplicate in un dataset può avere diversi impatti negativi sull’analisi dei dati:

1. Distorsione delle Statistiche: Le righe duplicate possono distorcere statistiche importanti come la media, la mediana, e la deviazione standard. Questo può portare a conclusioni errate riguardo alle tendenze, ai modelli e alle caratteristiche generali del dataset.

2. Affidabilità Compromessa: La presenza di duplicati mette in dubbio l’affidabilità dei dati. Analisi come correlazioni, regressioni, e altre inferenze statistiche possono essere influenzate negativamente, portando a risultati non accurati.

3. Efficienza Ridotta: I record duplicati aumentano inutilmente la dimensione del dataset, portando a un utilizzo inefficiente della memoria e a tempi di elaborazione più lunghi, specialmente in grandi set di dati.

4. Decisioni Inaccurate: In ambito aziendale e decisionale, i dati duplicati possono portare a prendere decisioni basate su informazioni errate, influenzando negativamente le strategie e i risultati aziendali.

5. Complicazioni nella Modellazione dei Dati: Nel machine learning e in altre forme di modellazione dei dati, i duplicati possono portare a un addestramento scorretto dei modelli, causando overfitting o bias nei risultati.

Per questi motivi, è cruciale identificare e rimuovere i record duplicati prima di procedere con ulteriori analisi.

:green[Rimozione delle duplicate]\n
:green[Rimozione delle righe duplicate mantenendo la prima occorrenza]\n

clean_data = data2.drop_duplicates()\n

clean_data.shape\n
(1001, 12)\n

data2.shape\n
(1004, 12)\n        

Le righe duplicate sono state rimosse dal dataset data2. Dopo la rimozione, il dataset contiene ora 1001 righe e 12 colonne, rispetto alle 1004 righe originali. Questo indica che 3 righe duplicate sono state rimosse.\n

:green[ID duplicato]\n
:green[Per identificare l’ID duplicato nel dataset, puoi utilizzare il seguente codice:]\n

Identificazione degli ID duplicati nel dataset "cap3"\n
ids_duplicati = clean_data[clean_data['id_della_campagna'].duplicated(keep=False)]\n

Visualizzazione dei record con gli ID duplicati\n
print(ids_duplicati)\n        

Questo codice assegnerà alla riga 518 un nuovo ID, che sarà il valore massimo corrente degli ID incrementato di 1, assicurando che sia unico all’interno del dataset.\n

:green[Calcolo del valore massimo di ID nel dataset e aggiunta di 1]\n
nuovo_id = clean_data['id_della_campagna'].max() + 1\n

Modifica dell'ID della riga 518\n
clean_data.loc[clean_data.index == 518, 'id_della_campagna'] = nuovo_id\n

Verifica se la modifica è stata applicata correttamente\n
modifica_applicata = clean_data.loc[clean_data.index == 518]\n
print(modifica_applicata)\n

Abbiamo affrontato il problema di un ID duplicato nel nostro dataset modificando l’ID di un record specifico (riga 518) per garantirne l’unicità. Questo è stato realizzato incrementando di 1 l’ID (1000) massimo esistente nel dataset e assegnando questo nuovo valore (1001) all’ID della riga 518.\n
Pertanto, la duplicazione dei valori nella colonna ID rappresenta un problema. Per altre colonne con valori duplicati, è essenziale comprendere il contesto aziendale e procedere con un’analisi specifica per ogni caso.\n

:green[Valori Mancanti]\n
Finora, abbiamo risolto con successo due problemi chiave nel nostro dataset: la presenza di righe duplicate e di ID duplicati. Il prossimo passo sarà affrontare il problema dei valori mancanti. È fondamentale riconoscere che i valori mancanti possono avere un impatto significativo sulla qualità e l’accuratezza delle nostre analisi.\n

:green[Verifica dei valori mancanti in "clean_data"]\n
valori_mancanti = clean_data.isnull().sum()\n
print(valori_mancanti) \n

Ci sono 55 valori mancanti nella colonna budget_della_campagna_r. Tutte le altre colonne del dataset non presentano valori mancanti.\n
Adesso vedremo il percentuale dei valori mancanti nella colonna ‘budget_della_campagna_r’, che è un passaggio cruciale per decidere come gestire questi valori mancanti.\n

Numero totale di righe in 'budget_della_campagna_r'\n
totale_righe = clean_data.shape[0]\n

Numero di valori mancanti in 'budget_della_campagna_r'\n
valori_mancanti_budget = clean_data['budget_della_campagna_r'].isnull().sum()\n

Calcolo del percentuale di valori mancanti\n
percentuale_mancanti = (valori_mancanti_budget / totale_righe) * 100\n
print(percentuale_mancanti)\n

5.49%  \n

:green[Statistiche della colonna]\n
:green[Statistiche della colonna 'budget_della_campagna_r']\n
media = clean_data['budget_della_campagna_r'].mean()\n
mediana = clean_data['budget_della_campagna_r'].median()\n
massimo = clean_data['budget_della_campagna_r'].max()\n
minimo = clean_data['budget_della_campagna_r'].min()\n

print("Media:", media)\n
print("Mediana:", mediana)\n
print("Massimo:", massimo)\n
print("Minimo:", minimo)\n

Media: 25062.07\n
Mediana: 24697.08\n
Massimo: 49982.02\n
Minimo: 1042.12  \n

I dati nella colonna ‘budget_della_campagna_r’ non mostrano significative discrepanze. La media e la mediana sono molto vicine tra loro, il che suggerisce una distribuzione relativamente uniforme dei valori. Pertanto, possiamo procedere con un certo grado di sicurezza nell’utilizzare la media o la mediana per interpolare i valori mancanti.\n

:green[Strategie Efficaci per la Gestione dei Valori Mancanti]\n
:green[Per trattare i valori mancanti nella colonna ‘budget_della_campagna_r’ del dataset “clean_data”, ci sono diverse opzioni:]\n

- Interpolazione con la Media o la Mediana: Se la distribuzione dei dati è relativamente uniforme, potresti usare la media o la mediana per riempire i valori mancanti. Questo è un approccio comune quando i dati non mostrano estreme variazioni o outlier significativi.\n
- Interpolazione Lineare: Se ci sono tendenze o modelli nei dati, l’interpolazione lineare può essere utilizzata per stimare i valori mancanti basandosi sui valori adiacenti.\n
- Eliminazione delle Righe: Se i valori mancanti non sono molti e se la rimozione di queste righe non influisce significativamente sulle analisi, potresti considerare di eliminare le righe con valori mancanti.\n
- Modello di Imputazione: Per dataset più complessi, potresti utilizzare modelli statistici o di machine learning per prevedere e imputare i valori mancanti, soprattutto se la quantità di dati mancanti è rilevante.\n

La scelta del metodo dipenderà dalla quantità di valori mancanti, dalla distribuzione dei dati esistenti e dall’impatto dell’imputazione sulle analisi successive.\n

:green[Calcolo della mediana]\n
mediana_budget = clean_data['budget_della_campagna_r'].median()\n

:green[Preenchimento dei valori mancanti con la mediana]\n
clean_data['budget_della_campagna_r'].fillna(mediana_budget, inplace=True)

:green[Verifica se tutti i valori mancanti sono stati riempiti]\n
valori_mancanti_dopo = clean_data['budget_della_campagna_r'].isnull().sum()
valori_mancanti_dopo

0         

:green[Percorso Essenziale per l’Elaborazione e l’Analisi dei Dati]\n
Il processo che abbiamo seguito è fondamentale nel campo dell’analisi dei dati. Iniziamo caricando i dati e fornendo un riassunto iniziale.\n

Il primo passo è verificare la presenza di duplicati per evitare sorprese durante l’analisi. Controlliamo anche la fonte dei dati, se necessario, e esaminiamo ciascuna colonna per assicurarci che non contenga duplicati inappropriati.\n

Successivamente, ci concentriamo sui dati mancanti, calcolando il loro percentuale per valutare l’impatto delle nostre decisioni. Se una colonna presenta un’elevata quantità di dati mancanti, può essere più opportuno eliminarla poiché potrebbe non essere viabile per l’analisi. Altrimenti, applichiamo metodi statistici adatti per gestire questi valori mancanti.\n

Il passo successivo è risolvere il problema delle informazioni mancanti o errate, che può essere più complesso. Un approccio utile è controllare la presenza di caratteri insoliti o problemi specifici in ogni variabile, ad esempio verificando i valori unici in ciascuna di esse. Questo approccio sistematico garantisce che i dati siano accurati e pronti per analisi più dettagliate.\n

:green[Analisi dei Valori Unici]\n
Stiamo conducendo questa analisi per comprendere meglio la varietà e l’unicità dei dati in ciascuna colonna.\n

valori_unici = clean_data.nunique()\n
print(valori_unici) \n

Questo ci aiuterà a identificare colonne con una grande diversità di valori, colonne con potenziali valori ripetitivi o limitati, e a rilevare eventuali anomalie o inconsistenze nei dati.\n

Per visualizzare ogni valore unico per ogni colonna del dataset “clean_data”, puoi utilizzare il seguente codice Python nel tuo ambiente locale:\n

Visualizzazione dei valori unici per ogni colonna in "clean_data"\n
for colonna in clean_data.columns:\n
    print(f"Valori unici nella colonna '{colonna}': {clean_data[colonna].unique()}\n")\n
    
Questo codice stamperà l’elenco di tutti i valori unici per ciascuna colonna nel dataset “clean_data”. È un modo efficace per esplorare in dettaglio i diversi tipi di dati presenti in ogni colonna, aiutandoti a capire meglio la composizione del tuo dataset.\n

:green[Identificazione degli Outliers]\n
Ora passeremo alla fase di rilevamento degli outliers nel nostro dataset. Gli outliers sono valori estremamente alti o bassi che si discostano significativamente dalla maggior parte degli altri dati.\n

Identificarli è cruciale, poiché possono influenzare negativamente le analisi statistiche e i modelli predittivi. Utilizzeremo metodi statistici per esaminare le diverse colonne del dataset alla ricerca di questi valori anomali, garantendo così che le nostre analisi siano il più accurate e affidabili possibile.\n

Selezione delle colonne numeriche\n
colonne_numeriche = clean_data.select_dtypes(include=['float64', 'int64'])\n

Calcolo dell'IQR (Intervallo Interquartile) per identificare gli outliers\n
Q1 = colonne_numeriche.quantile(0.25)\n
Q3 = colonne_numeriche.quantile(0.75)\n
IQR = Q3 - Q1\n

Definizione dei limiti per considerare un valore come outlier\n
limite_inferiore = Q1 - 1.5 * IQR\n
limite_superiore = Q3 + 1.5 * IQR\n

Identificazione degli outliers\n
outliers = (colonne_numeriche < limite_inferiore) | (colonne_numeriche > limite_superiore)\n

outliers.sum()\n

Abbiamo eseguito un’analisi per identificare gli outliers nelle colonne numeriche del dataset. Utilizzando il metodo dell’Intervallo Interquartile (IQR), abbiamo definito limiti inferiore e superiore per ciascuna colonna numerica.\n

Gli outliers sono stati individuati come valori che si trovano al di fuori di questi limiti. Dai risultati, abbiamo scoperto che la colonna Impressioni contiene 38 outliers, mentre nelle altre colonne numeriche non sono stati rilevati outliers. Questo passaggio è fondamentale per garantire la correttezza delle nostre analisi, poiché gli outliers possono influenzare significativamente i risultati statistici e i modelli predittivi.\n

:green[Calcolo di media, mediana, valore massimo e minimo per la colonna "Impressões" in "clean_data"]\n

media = clean_data['impressioni'].mean()\n
mediana = clean_data['impressioni'].median()\n
max = clean_data['impressioni'].max()\n
min = clean_data['impressioni'].min()\n

(media, mediana, max, min)\n
# (62555.754245754244, 5667.0, 1975723, 1001)   \n

Ecco le statistiche per la colonna Impressioni nel dataset:\n


Media delle Impressioni: 62.384,08\n
Mediana delle Impressioni: 5.668,5\n
Valore Massimo delle Impressioni: 1.975.723\n
Valore Minimo delle Impressioni: 1.001\n

:green[La Scelta tra Rimozione e Imputazione di Outliers nel Dataset]\n
Il valore massimo nella colonna Impressioni è chiaramente un outlier, in quanto si discosta significativamente dal modello generale dei dati. La media risulta essere elevata a causa dell’impatto degli outliers, mentre la mediana, essendo il valore centrale in un insieme di dati ordinato, non è influenzata in egual misura. Queste osservazioni dimostrano come l’utilizzo della media possa essere ingannevole in presenza di outliers.\n

Se la media è distorta dagli outliers, sostituire i valori mancanti con questa media distorta potrebbe causare problemi nel dataset. In questo caso, i valori sono estremamente diversi, rendendo la rimozione degli outliers una scelta più prudente. Qualsiasi altro metodo di imputazione potrebbe rappresentare un rischio per l’integrità dell’analisi.\n

Considerando che il numero di record da rimuovere è minimo, procederemo con la rimozione dei 38 outliers identificati, preservando così la qualità e l’affidabilità del nostro dataset per le analisi successive.\n

:green[Rimozione dei record con valori outlier nella colonna Impressioni nel dataset "clean_data"]\n

:green[Identificazione degli outliers]\n
outliers_impressioni = (clean_data['impressioni'] < limite_inferiore['impressioni']) | (clean_data['impressioni'] > limite_superiore['impressioni'])\n

:green[Rimozione degli outliers]\n
clean_data_senza_outliers = clean_data[~outliers_impressioni]\n

clean_data_senza_outliers.shape, clean_data.shape\n      

:green[Salvataggio della Versione Finale del Dataset Dopo la Pulizia]\n
Abbiamo completato il processo di pulizia del dataset “clean_data”, rimuovendo sia le righe duplicate sia gli outliers nella colonna Impressioni.\n

La versione finale del dataset, ora denominata “clean_data_senza_outliers”, è stata salvata in formato CSV.\n

Questa versione pulita del dataset è pronta per essere utilizzata in analisi successive, garantendo una maggiore affidabilità e precisione dei risultati.\n


:green[Salvataggio della versione finale del dataset in formato CSV]\n
output_file_path = 'clean_data_versione_finale.csv'\n
clean_data_senza_outliers.to_csv(output_file_path, index=False)\n

output_file_path 

:green[Conclusione]\n
Abbiamo intrapreso un percorso metodico e dettagliato per organizzare e pulire il nostro dataset “clean_data”, un processo fondamentale per garantire che le analisi condotte siano accurate e affidabili. Inizialmente, abbiamo caricato i dati e creato un riassunto per ottenere una visione generale del contenuto e delle caratteristiche del dataset. Questo passaggio iniziale ci ha permesso di identificare immediatamente le aree che necessitavano di attenzione.\n
Il primo problema affrontato è stato la presenza di righe duplicate. La rimozione di queste righe è stata cruciale per evitare distorsioni nelle analisi e per garantire l’unicità dei dati. Successivamente, ci siamo concentrati sugli ID duplicati, un aspetto fondamentale per mantenere l’integrità dei dati. Abbiamo risolto questo problema modificando l’ID di un record specifico, garantendo così che tutti gli ID nel dataset fossero unici.\n

In seguito, abbiamo affrontato il problema dei valori mancanti, valutando il loro impatto e decidendo le strategie più adatte per gestirli. In particolare, abbiamo optato per l’imputazione dei valori mancanti nella colonna “budget_della_campagna_r” utilizzando la mediana, una scelta dettata dalla necessità di evitare distorsioni causate da valori estremi.\n

Infine, abbiamo identificato e rimosso gli outliers nella colonna “Impressões” (Impressioni), un passo decisivo per evitare che valori estremamente elevati influenzassero negativamente le analisi successive. Dopo aver completato queste fasi di pulizia, abbiamo salvato la versione finale del dataset in formato CSV, rendendola pronta per un’analisi più approfondita.\n

Attraverso questo processo, non solo abbiamo migliorato la qualità del dataset, ma abbiamo anche applicato principi fondamentali dell’analisi dei dati, dimostrando come un’attenta pulizia e preparazione dei dati siano essenziali per qualsiasi tipo di analisi dati. Questa esperienza serve come esempio didattico dell’importanza di esaminare, pulire e preparare i dati prima di procedere con analisi complesse, assicurando così che le conclusioni tratte siano basate su informazioni precise e affidabili.
    
    ''')

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

    st.page_link("https://ccaudek.github.io/bookdown_psicometria/chapter-descript.html#forma-di-una-distribuzione", label="1 - Reference", icon="🏠")
    st.page_link("https://www.geeksforgeeks.org/python-normal-distribution-in-statistics/", label="2 - Reference", icon="🏠")
    st.page_link("https://smartstrategy.eu/research/come-calcolare-media-e-deviazione-standard-con-python-per-principianti/", label="Media e deviazione standard", icon="🏠")
     
    st.page_link("https://community.sisense.com/t5/knowledge/test-for-normal-distribution-of-data-with-python/ta-p/9434", label="Test con Pandas", icon="🏠")
                             
with st.expander("**Rimozione dei duplicati**"):
    st.write('''
        Rimuovere i duplicati è un'abilità essenziale 
        per ottenere conteggi accurati perché spesso non si desidera contare la stessa cosa più volte. In Python, ciò potrebbe essere ottenuto 
        utilizzando il modulo Pandas , che ha un metodo noto come drop_duplicates.
    ''')
      
    st.page_link("https://www.geeksforgeeks.org/python-pandas-dataframe-drop_duplicates/", label="1 -Reference", icon="🏠")
              
  
with st.expander("**Correzione degli errori di struttura**"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')                       
  
 # https://www.diariodiunanalista.it/posts/come-identificare-anomalie-nei-tuoi-dati/
with st.expander("**Gestione dei valori anomali**"):
    st.write('''
        Metodo della Deviazione Standard:
Questo metodo identifica i valori anomali basandosi sulla deviazione standard dei dati.
Calcola la media e la deviazione standard per ciascuna variabile.
Considera come valori anomali quelli che si discostano da questa media di più di una certa soglia (ad esempio, 2 o 3 volte la deviazione standard).

:green[Esempio in Python:]\n
\n
import numpy as np\n
threshold = 2  :green[# Soglia per considerare un valore come anomalo]\n
mean, std = np.mean(dataset), np.std(dataset)\n
outliers = dataset[(dataset - mean) > threshold * std]\n
\n
Metodo dell’Intervallo Interquartile (IQR):\n
L’IQR è la differenza tra il terzo quartile (75%) e il primo quartile (25%).\n
I valori al di fuori di questo intervallo sono considerati anomali.\n
\n
:green[Esempio in Python:]\n
\n
Q1 = dataset.quantile(0.25)\n
Q3 = dataset.quantile(0.75)\n
IQR = Q3 - Q1\n
outliers = dataset[(dataset < (Q1 - 1.5 * IQR)) | (dataset > (Q3 + 1.5 * IQR))]\n
\n
Rilevamento automatico dei valori anomali:\n
Utilizza modelli di machine learning specifici per identificare valori anomali.\n
Ad esempio, puoi utilizzare Isolation Forest o One-Class SVM.\n
\n
:green[Esempio in Python:]\n
\n
from sklearn.ensemble import IsolationForest\n
model = IsolationForest(contamination=0.05)  # Contaminazione = percentuale di valori anomali\n
model.fit(dataset)\n
outliers = model.predict(dataset) == -1\n

Ricorda che la scelta del metodo dipende dal contesto e dalla natura dei dati. Inoltre, è importante esaminare attentamente i valori identificati come anomali per evitare di rimuovere informazioni preziose.
    ''') 
    st.page_link("https://www.diariodiunanalista.it/posts/come-identificare-anomalie-nei-tuoi-dati/", label="Reference", icon="🏠")
    st.page_link("https://www.intelligenzaartificialeitalia.net/post/come-rimuovere-e-gestire-i-valori-anomali-con-python-nel-machine-learning", label="Reference", icon="🏠")

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
        Nel Machine Learning, un modello sarà buono (o altrettanto cattivo) quanto i dati con cui lo addestri. L'entità delle diverse funzionalità influisce sui diversi modelli di machine learning per vari motivi.

Ad esempio, considera un set di dati contenente due caratteristiche, età e reddito. Qui l’età varia da 0 a 100, mentre il reddito varia da 0 a un importo enorme, per lo più superiore a 100. Il reddito è circa 1.000 volte maggiore dell’età. Quindi, queste due funzionalità rientrano in intervalli molto diversi. Quando eseguiamo ulteriori analisi, come ad esempio la regressione lineare multivariata, il reddito attribuito influenzerà intrinsecamente maggiormente il risultato a causa del suo valore maggiore. Ma questo non significa necessariamente che sia più importante come predittore. Pertanto, la portata di tutti gli elementi dovrebbe essere ridimensionata in modo che ogni elemento contribuisca in modo approssimativamente proporzionale alla distanza finale.
        
    ''')
     st.page_link("https://towardsdatascience.com/normalization-vs-standardization-cb8fe15082eb", label="Reference", icon="🏠")

with st.expander("**Formattazione dei dati**"):
    st.write('''
        
    ''')                                

with st.expander("**Codifica delle etichette**"):
     st.write('''
        La codifica delle etichette è una tecnica utilizzata per convertire le colonne categoriche in colonne numeriche in modo che possano essere adattate da modelli di apprendimento automatico che accettano solo dati numerici. Si tratta di un importante passaggio di pre-elaborazione in un progetto di machine learning.
    ''')  
     st.page_link("https://www.geeksforgeeks.org/ml-label-encoding-of-datasets-in-python/", label="Reference", icon="🏠")

with st.expander("**One-hot encoding**"):
     st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')       
     st.page_link("https://www.geeksforgeeks.org/ml-one-hot-encoding/?ref=header_search", label="Reference", icon="🏠")

with st.expander("**Gestione dei dati sbilanciati con SMOTE e l'algoritmo Near Miss**"):
     st.write('''
        La Synthetic Minority Over-sampling TEchnique, o SMOTE in breve, è una tecnica di preelaborazione utilizzata per affrontare uno squilibrio di classi in un set di dati.
    ''') 
     st.page_link("https://medium.com/@corymaklin/synthetic-minority-over-sampling-technique-smote-7d419696b88c", label="Reference", icon="🏠")
     

with st.expander("**Trappola delle variabili fittizie nei modelli di regressione**"):
    st.write('''
        The chart above shows some numbers I picked for you.
        I rolled actual dice for these, so they're *guaranteed* to
        be random.
    ''')  
         


