import stramlit as st

#https://it.linkedin.com/pulse/guida-completa-alla-pulizia-dei-dati-csv-leonardo-anello-btj2f
    st.write('''
    Il dataset presenta i seguenti problemi:

        - Righe duplicate
        - ID duplicati
        - Valori mancanti
        - Valori anomali (Outliers)
        
        :green[**CODICE**]
        ''')

    st.code(f"""
        import pandas as pd
        
        # Caricamento del file dati
        file_path = 'data.csv'
        data = pd.read_csv(file_path)
        
        # Ottenimento delle dimensioni del dataset
        dimensioni = data.shape
        
        # Visualizzazione delle prime righe del dataset per comprendere la struttura dei dati
        prime_righe = data.head()
        dimensioni
        (1004, 12) 
        """)
    
    st.write('''   
    :green[**Traduzione delle etichette del dataset originale in italiano con underscore case**]\n
    ''')

    st.write('''
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
    }
    ''')
    
    st.code(f"""
    # Applicazione delle traduzioni con underscore case al dataset originale
    data2 = data.rename(columns=traduzioni_originali)       
    
    # Dettaglio dei Dati
    describe = data2.describe(include='all')
    describe
    """)
    
    st.code(f"""
    id_della_campagna: ID numerico delle campagne, varia da 1 a 1000.\n
    nome_della_campagna: Nomi unici delle campagne, con 999 valori unici e una massima frequenza di 2 per “Balanced asymmetric architecture”.\n
    data_di_inizio e data_di_fine: Date di inizio e fine delle campagne. Presentano diverse date uniche.\n
    budget_della_campagna_r: Budget delle campagne in Reais brasiliani, con un valore medio di circa 25.043, una deviazione standard di 14.187 e valori che variano da circa 1.042 a 49.982.\n
    canale: Canale di marketing utilizzato, con 5 categorie uniche. “Email” è il più frequente.\n
    impressioni: Numero di impressioni, con una media di circa 62.384, una deviazione standard molto elevata (293.482) e un range che va da 1.001 a 1.975.723.\n
    click: Numero di click, con una media di 554 e un range da 101 a 998.\n
    conversioni: Numero di conversioni, con una media di 103 e un range da 10 a 200.\n
    visualizzazioni_pagina: Numero di visualizzazioni pagina, con una media di circa 5.419 e un range da 1.009 a 9.996.\n
    fonte_del_traffico: Fonte del traffico, con 5 categorie uniche e “Direto” come la più frequente.\n
    tasso_di_rimbalzo: Tasso di rimbalzo, con una media di 0.516 e un range da 0 a 1.\n
     """)
    
    st.code(f"""
    # Record Duplicati
    
    # Utilizzo di duplicated() per trovare i record duplicati
    keep=False #segnala tutte le occorrenze dei record duplicati
    duplicati = data2[data2.duplicated(keep=False)]
    duplicati
    """)

    st.write('''
    Mantenere righe duplicate in un dataset può avere diversi impatti negativi sull’analisi dei dati:
    
    1. Distorsione delle Statistiche: Le righe duplicate possono distorcere statistiche importanti come la media, la mediana, e la deviazione standard. Questo può portare a conclusioni errate riguardo alle tendenze, ai modelli e alle caratteristiche generali del dataset.
    
    2. Affidabilità Compromessa: La presenza di duplicati mette in dubbio l’affidabilità dei dati. Analisi come correlazioni, regressioni, e altre inferenze statistiche possono essere influenzate negativamente, portando a risultati non accurati.
    
    3. Efficienza Ridotta: I record duplicati aumentano inutilmente la dimensione del dataset, portando a un utilizzo inefficiente della memoria e a tempi di elaborazione più lunghi, specialmente in grandi set di dati.
    
    4. Decisioni Inaccurate: In ambito aziendale e decisionale, i dati duplicati possono portare a prendere decisioni basate su informazioni errate, influenzando negativamente le strategie e i risultati aziendali.
    
    5. Complicazioni nella Modellazione dei Dati: Nel machine learning e in altre forme di modellazione dei dati, i duplicati possono portare a un addestramento scorretto dei modelli, causando overfitting o bias nei risultati.
    
    Per questi motivi, è cruciale identificare e rimuovere i record duplicati prima di procedere con ulteriori analisi.
    
    :green[**Rimozione delle righe duplicate**]\n
    :green[Rimozione delle righe duplicate mantenendo la prima occorrenza]\n
    ''')

    st.code(f"""
    clean_data = data2.drop_duplicates()
    
    clean_data.shape
    (1001, 12)
    
    data2.shape
    (1004, 12)       
    """)
    
    st.write('''
    Le righe duplicate sono state rimosse dal dataset data2. Dopo la rimozione, il dataset contiene ora 1001 righe e 12 colonne, rispetto alle 1004 righe originali. Questo indica che 3 righe duplicate sono state rimosse.\n
    
    :green[**ID duplicato**]\n
    :green[Per identificare l’ID duplicato nel dataset, puoi utilizzare il seguente codice:]\n
    ''')

    st.code(f"""
    # Identificazione degli ID duplicati nel dataset "cap3"
    ids_duplicati = clean_data[clean_data['id_della_campagna'].duplicated(keep=False)]
    
    # Visualizzazione dei record con gli ID duplicati
    print(ids_duplicati)      
    """)

    st.write('''
    Questo codice assegnerà alla riga 518 un nuovo ID, che sarà il valore massimo corrente degli ID incrementato di 1, assicurando che sia unico all’interno del dataset.\n
    ''')

    st.code(f"""
    # Calcolo del valore massimo di ID nel dataset e aggiunta di 1
    nuovo_id = clean_data['id_della_campagna'].max() + 1
    
    # Modifica dell'ID della riga 518
    clean_data.loc[clean_data.index == 518, 'id_della_campagna'] = nuovo_id
    
    # Verifica se la modifica è stata applicata correttamente
    modifica_applicata = clean_data.loc[clean_data.index == 518]
    print(modifica_applicata)
    """)
    
    st.write('''
    Abbiamo affrontato il problema di un ID duplicato nel nostro dataset modificando l’ID di un record specifico (riga 518) per garantirne l’unicità. Questo è stato realizzato incrementando di 1 l’ID (1000) massimo esistente nel dataset e assegnando questo nuovo valore (1001) all’ID della riga 518.\n
    Pertanto, la duplicazione dei valori nella colonna ID rappresenta un problema. Per altre colonne con valori duplicati, è essenziale comprendere il contesto aziendale e procedere con un’analisi specifica per ogni caso.\n
    
    :green[**Valori Mancanti**]\n
    Finora, abbiamo risolto con successo due problemi chiave nel nostro dataset: la presenza di righe duplicate e di ID duplicati. Il prossimo passo sarà affrontare il problema dei valori mancanti. È fondamentale riconoscere che i valori mancanti possono avere un impatto significativo sulla qualità e l’accuratezza delle nostre analisi.\n
    ''')

    st.code(f"""
    # Verifica dei valori mancanti in "clean_data"
    valori_mancanti = clean_data.isnull().sum()
    print(valori_mancanti) 
    """)

    st.write('''
    Ci sono 55 valori mancanti nella colonna budget_della_campagna_r. Tutte le altre colonne del dataset non presentano valori mancanti.\n
    Adesso vedremo la percentuale dei valori mancanti nella colonna ‘budget_della_campagna_r’, che è un passaggio cruciale per decidere come gestire questi valori mancanti.\n
    ''')

    st.code(f"""
    # Numero totale di righe in 'budget_della_campagna_r'
    totale_righe = clean_data.shape[0]
    
    # Numero di valori mancanti in 'budget_della_campagna_r'
    valori_mancanti_budget = clean_data['budget_della_campagna_r'].isnull().sum()
    
    # Calcolo del percentuale di valori mancanti
    percentuale_mancanti = (valori_mancanti_budget / totale_righe) * 100
    print(percentuale_mancanti)
    
    5.49%  
    """)

    st.code(f"""
    #Statistiche della colonna
    #Statistiche della colonna 'budget_della_campagna_r'
    media = clean_data['budget_della_campagna_r'].mean()
    mediana = clean_data['budget_della_campagna_r'].median()
    massimo = clean_data['budget_della_campagna_r'].max()
    minimo = clean_data['budget_della_campagna_r'].min()
    
    print("Media:", media)
    print("Mediana:", mediana)
    print("Massimo:", massimo)
    print("Minimo:", minimo)
    
    Media: 25062.07
    Mediana: 24697.08
    Massimo: 49982.02
    Minimo: 1042.12  
    """)

    st.write('''
    I dati nella colonna ‘budget_della_campagna_r’ non mostrano significative discrepanze. La media e la mediana sono molto vicine tra loro, il che suggerisce una distribuzione relativamente uniforme dei valori. Pertanto, possiamo procedere con un certo grado di sicurezza nell’utilizzare la media o la mediana per interpolare i valori mancanti.\n
    
    :green[**Strategie Efficaci per la Gestione dei Valori Mancanti**]\n
    :green[Per trattare i valori mancanti nella colonna ‘budget_della_campagna_r’ del dataset “clean_data”, ci sono diverse opzioni:]\n
    
    - Interpolazione con la Media o la Mediana: Se la distribuzione dei dati è relativamente uniforme, potresti usare la media o la mediana per riempire i valori mancanti. Questo è un approccio comune quando i dati non mostrano estreme variazioni o outlier significativi.\n
    - Interpolazione Lineare: Se ci sono tendenze o modelli nei dati, l’interpolazione lineare può essere utilizzata per stimare i valori mancanti basandosi sui valori adiacenti.\n
    - Eliminazione delle Righe: Se i valori mancanti non sono molti e se la rimozione di queste righe non influisce significativamente sulle analisi, potresti considerare di eliminare le righe con valori mancanti.\n
    - Modello di Imputazione: Per dataset più complessi, potresti utilizzare modelli statistici o di machine learning per prevedere e imputare i valori mancanti, soprattutto se la quantità di dati mancanti è rilevante.\n
    
    :red[**La scelta del metodo dipenderà dalla quantità di valori mancanti, dalla distribuzione dei dati esistenti e dall’impatto dell’imputazione sulle analisi successive.**]\n
    ''')

    st.code(f"""
    #Calcolo della mediana
    mediana_budget = clean_data['budget_della_campagna_r'].median()
    
    #Preenchimento dei valori mancanti con la mediana
    clean_data['budget_della_campagna_r'].fillna(mediana_budget, inplace=True)
    
    #Verifica se tutti i valori mancanti sono stati riempiti
    valori_mancanti_dopo = clean_data['budget_della_campagna_r'].isnull().sum()
    valori_mancanti_dopo
    
    0         
    """)

    st.write('''
    :green[**Percorso Essenziale per l’Elaborazione e l’Analisi dei Dati**]\n
    Il processo che abbiamo seguito è fondamentale nel campo dell’analisi dei dati. Iniziamo caricando i dati e fornendo un riassunto iniziale.\n
    
    Il primo passo è verificare la presenza di duplicati per evitare sorprese durante l’analisi. Controlliamo anche la fonte dei dati, se necessario, e esaminiamo ciascuna colonna per assicurarci che non contenga duplicati inappropriati.\n
    
    Successivamente, ci concentriamo sui dati mancanti, calcolando il loro percentuale per valutare l’impatto delle nostre decisioni. Se una colonna presenta un’elevata quantità di dati mancanti, può essere più opportuno eliminarla poiché potrebbe non essere viabile per l’analisi. Altrimenti, applichiamo metodi statistici adatti per gestire questi valori mancanti.\n
    
    Il passo successivo è risolvere il problema delle informazioni mancanti o errate, che può essere più complesso. Un approccio utile è controllare la presenza di caratteri insoliti o problemi specifici in ogni variabile, ad esempio verificando i valori unici in ciascuna di esse. Questo approccio sistematico garantisce che i dati siano accurati e pronti per analisi più dettagliate.\n
    ''')
    
    st.code(f"""
    #Analisi dei Valori Unici
    #Stiamo conducendo questa analisi per comprendere meglio la varietà e l’unicità dei dati in ciascuna colonna.\n
    
    valori_unici = clean_data.nunique()
    print(valori_unici) 
    """)

    st.write('''
    Questo ci aiuterà a identificare colonne con una grande diversità di valori, colonne con potenziali valori ripetitivi o limitati, e a rilevare eventuali anomalie o inconsistenze nei dati.\n
    
    Per visualizzare ogni valore unico per ogni colonna del dataset “clean_data”, puoi utilizzare il seguente codice Python nel tuo ambiente locale:\n
    ''')
       
    st.info("""Visualizzazione dei valori unici per ogni colonna in clean_data\n
    for colonna in clean_data.columns:\n
        print(f"Valori unici nella colonna '{colonna}': {clean_data[colonna].unique()}""",icon="ℹ️")
    
    st.write('''
    Questo codice stamperà l’elenco di tutti i valori unici per ciascuna colonna nel dataset “clean_data”. È un modo efficace per esplorare in dettaglio i diversi tipi di dati presenti in ogni colonna, aiutandoti a capire meglio la composizione del tuo dataset.\n
    
    :green[**Identificazione degli Outliers**]\n
    Ora passeremo alla fase di rilevamento degli outliers nel nostro dataset. Gli outliers sono valori estremamente alti o bassi che si discostano significativamente dalla maggior parte degli altri dati.\n
    
    Identificarli è cruciale, poiché possono influenzare negativamente le analisi statistiche e i modelli predittivi. Utilizzeremo metodi statistici per esaminare le diverse colonne del dataset alla ricerca di questi valori anomali, garantendo così che le nostre analisi siano il più accurate e affidabili possibile.\n
    ''')

    st.code(f"""
    Selezione delle colonne numeriche
    colonne_numeriche = clean_data.select_dtypes(include=['float64', 'int64'])
    
    Calcolo dell'IQR (Intervallo Interquartile) per identificare gli outliers
    Q1 = colonne_numeriche.quantile(0.25)
    Q3 = colonne_numeriche.quantile(0.75)
    IQR = Q3 - Q1
    
    Definizione dei limiti per considerare un valore come outlier
    limite_inferiore = Q1 - 1.5 * IQR
    limite_superiore = Q3 + 1.5 * IQR
    
    Identificazione degli outliers
    outliers = (colonne_numeriche < limite_inferiore) | (colonne_numeriche > limite_superiore)
    
    outliers.sum()
    """)
    
    st.write('''
    Abbiamo eseguito un’analisi per identificare gli outliers nelle colonne numeriche del dataset. Utilizzando il metodo dell’Intervallo Interquartile (IQR), abbiamo definito limiti inferiore e superiore per ciascuna colonna numerica.\n
    
    Gli outliers sono stati individuati come valori che si trovano al di fuori di questi limiti. Dai risultati, abbiamo scoperto che la colonna Impressioni contiene 38 outliers, mentre nelle altre colonne numeriche non sono stati rilevati outliers. Questo passaggio è fondamentale per garantire la correttezza delle nostre analisi, poiché gli outliers possono influenzare significativamente i risultati statistici e i modelli predittivi.\n
    ''')

    st.code(f"""
    :green[Calcolo di media, mediana, valore massimo e minimo per la colonna "Impressões" in "clean_data"]
    
    media = clean_data['impressioni'].mean()
    mediana = clean_data['impressioni'].median()
    max = clean_data['impressioni'].max()
    min = clean_data['impressioni'].min()
    
    (media, mediana, max, min)
    (62555.754245754244, 5667.0, 1975723, 1001)   
    
    Ecco le statistiche per la colonna Impressioni nel dataset:
    
    
    Media delle Impressioni: 62.384,08
    Mediana delle Impressioni: 5.668,5
    Valore Massimo delle Impressioni: 1.975.723
    Valore Minimo delle Impressioni: 1.001
    """)

    st.write('''
    :green[**La Scelta tra Rimozione e Imputazione di Outliers nel Dataset**]\n
    Il valore massimo nella colonna Impressioni è chiaramente un outlier, in quanto si discosta significativamente dal modello generale dei dati. La media risulta essere elevata a causa dell’impatto degli outliers, mentre la mediana, essendo il valore centrale in un insieme di dati ordinato, non è influenzata in egual misura. Queste osservazioni dimostrano come l’utilizzo della media possa essere ingannevole in presenza di outliers.\n
    
    Se la media è distorta dagli outliers, sostituire i valori mancanti con questa media distorta potrebbe causare problemi nel dataset. In questo caso, i valori sono estremamente diversi, rendendo la rimozione degli outliers una scelta più prudente. Qualsiasi altro metodo di imputazione potrebbe rappresentare un rischio per l’integrità dell’analisi.\n
    
    Considerando che il numero di record da rimuovere è minimo, procederemo con la rimozione dei 38 outliers identificati, preservando così la qualità e l’affidabilità del nostro dataset per le analisi successive.\n
    ''')

    st.code(f"""
    # Rimozione dei record con valori outlier nella colonna Impressioni nel dataset "clean_data"
    
    # Identificazione degli outliers
    outliers_impressioni = (clean_data['impressioni'] < limite_inferiore['impressioni']) | (clean_data['impressioni'] > limite_superiore['impressioni'])
    
    # Rimozione degli outliers
    clean_data_senza_outliers = clean_data[~outliers_impressioni]
    
    clean_data_senza_outliers.shape, clean_data.shape     
    """)
    
    st.write('''
    :green[**Salvataggio della Versione Finale del Dataset Dopo la Pulizia**]
    
    Abbiamo completato il processo di pulizia del dataset “clean_data”, rimuovendo sia le righe duplicate sia gli outliers nella colonna Impressioni.\n
    La versione finale del dataset, ora denominata “clean_data_senza_outliers”, è stata salvata in formato CSV.\n
    Questa versione pulita del dataset è pronta per essere utilizzata in analisi successive, garantendo una maggiore affidabilità e precisione dei risultati.\n
    ''')

    st.code(f"""
    # Salvataggio della versione finale del dataset in formato CSV
    output_file_path = 'clean_data_versione_finale.csv'
    clean_data_senza_outliers.to_csv(output_file_path, index=False)
    
    output_file_path 
    """)
    st.write('''
    :green[**Conclusione**]\n
    Abbiamo intrapreso un percorso metodico e dettagliato per organizzare e pulire il nostro dataset “clean_data”, un processo fondamentale per garantire che le analisi condotte siano accurate e affidabili. Inizialmente, abbiamo caricato i dati e creato un riassunto per ottenere una visione generale del contenuto e delle caratteristiche del dataset. Questo passaggio iniziale ci ha permesso di identificare immediatamente le aree che necessitavano di attenzione.\n
    Il primo problema affrontato è stato la presenza di righe duplicate. La rimozione di queste righe è stata cruciale per evitare distorsioni nelle analisi e per garantire l’unicità dei dati. Successivamente, ci siamo concentrati sugli ID duplicati, un aspetto fondamentale per mantenere l’integrità dei dati. Abbiamo risolto questo problema modificando l’ID di un record specifico, garantendo così che tutti gli ID nel dataset fossero unici.\n
    In seguito, abbiamo affrontato il problema dei valori mancanti, valutando il loro impatto e decidendo le strategie più adatte per gestirli. In particolare, abbiamo optato per l’imputazione dei valori mancanti nella colonna “budget_della_campagna_r” utilizzando la mediana, una scelta dettata dalla necessità di evitare distorsioni causate da valori estremi.\n
    Infine, abbiamo identificato e rimosso gli outliers nella colonna “Impressões” (Impressioni), un passo decisivo per evitare che valori estremamente elevati influenzassero negativamente le analisi successive. Dopo aver completato queste fasi di pulizia, abbiamo salvato la versione finale del dataset in formato CSV, rendendola pronta per un’analisi più approfondita.\n
    Attraverso questo processo, non solo abbiamo migliorato la qualità del dataset, ma abbiamo anche applicato principi fondamentali dell’analisi dei dati, dimostrando come un’attenta pulizia e preparazione dei dati siano essenziali per qualsiasi tipo di analisi dati. Questa esperienza serve come esempio didattico dell’importanza di esaminare, pulire e preparare i dati prima di procedere con analisi complesse, assicurando così che le conclusioni tratte siano basate su informazioni precise e affidabili.
        
        ''')
