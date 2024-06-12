import streamlit as st

st.header("Evaluation")
st.write('''Abbiamo tre tipologie: supervised learning, unsupervised learning, e reinforcement learning''')
st.write('''L\'apprendimento supervisionato è l\'attività di apprendimento automatico di apprendere una funzione che associa un input a un output sulla base di coppie input-output di esempio. 
I dati forniti sono etichettati. Sia i problemi di classificazione che quelli di regressione sono problemi di apprendimento supervisionato.\n
Esempio: considera i seguenti dati relativi ai pazienti che entrano in una clinica. I dati consistono nel sesso e nell\' età dei pazienti e ogni paziente è etichettato come \'sano\' o \'malato\'.
\n
''')
st.code(f"""
Genere        Età        Etichetta
M             48         malato
M             67         malato
F             53         in salute
M             49         malato
F             32         in salute
M             34         in salute
M             21         in salute
""")

st.write('''il modello o l'algoritmo viene presentato con input di esempio e i relativi output desiderati, quindi trova modelli e connessioni tra l'input e l'output. L’obiettivo è apprendere 
una regola generale che associa gli input agli output. Il processo di addestramento continua finché il modello non raggiunge il livello di precisione desiderato sui dati di addestramento. Alcuni esempi di vita reale sono:\n
- Classificazione delle immagini: ti alleni con immagini/etichette. Quindi in futuro dai una nuova immagine aspettandoti che il computer riconosca il nuovo oggetto.\n
- Previsione/regressione del mercato: alleni il computer con dati di mercato storici e chiedi al computer di prevedere il nuovo prezzo in futuro.\n
- Modelli generativi: dopo che un modello ha acquisito la distribuzione di probabilità dei dati di input, sarà in grado di generare più dati. Questo può essere molto utile per rendere il tuo classificatore più robusto.\n
''')
st.write('''L'apprendimento non supervisionato è un tipo di algoritmo di apprendimento automatico utilizzato per trarre inferenze da set di dati costituiti da dati di input senza risposte etichettate. 
Negli algoritmi di apprendimento non supervisionato, la classificazione o categorizzazione non è inclusa nelle osservazioni. \n
Esempio: considerare i seguenti dati relativi ai pazienti che entrano in una clinica. I dati sono costituiti dal sesso e dall’età dei pazienti. \n
''')

st.code(f"""
Genere         Età
M              48
M              67
F              53
M              49
F              34
M              21
""")

st.write('''In quanto tipo di apprendimento, assomiglia ai metodi utilizzati dagli esseri umani per capire che determinati oggetti o eventi appartengono alla stessa classe, ad esempio osservando \n
il grado di somiglianza tra gli oggetti. Alcuni sistemi di raccomandazione che trovi sul web sotto forma di marketing automation si basano su questo tipo di apprendimento. ''')

Apprendimento per rinforzo : un programma per computer interagisce con un ambiente dinamico in cui deve eseguire un determinato obiettivo (come guidare un veicolo o giocare contro un avversario). Al programma viene fornito un feedback in termini di ricompense e punizioni mentre naviga nello spazio problematico.


