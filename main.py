import streamlit as st
import pandas as pd
#from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import seaborn as sns


st.subheader("Distribuzione dati")
df = pd.read_csv('data.csv')
df.plot()
plt.show()


