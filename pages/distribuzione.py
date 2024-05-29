import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

if 'dati' not in st.session_state:
  pass
else:  
  st.write(st.session_state.dati)
  data = st.session_state.df
  st.write(data)

  fig = plt.figure(figsize =(10, 7))
  plt.boxplot(data)
  plt.show()
  plt.hist(data)
  plt.show()
  #tips = sns.load_dataset('data')
  #tips.plot()
