import streamlit as st

st.header("Evaluation")
st.write('''Abbiamo tre tipologie: supervised learning, unsupervised learning, e reinforcement learning''')
st.write('''L\'apprendimento supervisionato è l\'attività di apprendimento automatico di apprendere una funzione che associa un input a un output sulla base di coppie input-output di esempio. 
I dati forniti sono etichettati. Sia i problemi di classificazione che quelli di regressione sono problemi di apprendimento supervisionato.\n
Esempio: considera i seguenti dati relativi ai pazienti che entrano in una clinica. I dati consistono nel sesso e nell\' età dei pazienti e ogni paziente è etichettato come \'sano\' o \'malato\'.
\n
''')
st.code(f"""
Genere        Età        Etichetta\n
M             48         malato\n
M             67         malato\n
F             53         in salute\n
M             49         malato\n
F             32         in salute\n
M             34         in salute\n
M             21         in salute\n
""")

st.write('''il modello o l'algoritmo viene presentato con input di esempio e i relativi output desiderati, quindi trova modelli e connessioni tra l'input e l'output. L’obiettivo è apprendere 
una regola generale che associa gli input agli output. Il processo di addestramento continua finché il modello non raggiunge il livello di precisione desiderato sui dati di addestramento. Alcuni esempi di vita reale sono:\n
- Classificazione delle immagini: ti alleni con immagini/etichette. Quindi in futuro dai una nuova immagine aspettandoti che il computer riconosca il nuovo oggetto.\n
- Previsione/regressione del mercato: alleni il computer con dati di mercato storici e chiedi al computer di prevedere il nuovo prezzo in futuro.\n
''')
