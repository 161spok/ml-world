import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

if 'dati' not in st.session_state:
  pass
else:  
  st.write(st.session_state.dati)
  data = st.session_state.df
  data.boxplot()
  data.hist()

  #tips = sns.load_dataset('data')
  #tips.plot()
