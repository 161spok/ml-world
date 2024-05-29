import streamlit as st
import pandas as pd
#from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import seaborn as sns
import sys

st.subheader("Distribuzione dati")
df = pd.read_csv('data.csv')
df.plot()
plt.show()
#Two  lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()

