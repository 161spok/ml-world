import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import io

st.page_link("https://www.geeksforgeeks.org/data-cleansing-introduction/?ref=lbp", label="Data cleansing", icon="🌎")

st.write("Rimozione di osservazioni indesiderate")
st.write("Correzione degli errori di struttura")
st.write("Correzione dei duplicati")
st.write("Gestione dei valori anomali")
st.write("Gestione dei dati mancanti")                 # round((df1.isnull().sum()/df1.shape[0])*100,2)
st.write("Trasformazione dei dati")
st.write("Formattazione dei dati - ridimensionamento(ridimensionamento min e max e standardizzazione) e normalizzazione")
