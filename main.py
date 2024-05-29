import streamlit as st
import pandas as pd
 
# Create a sample dataframe
data = pd.DataFrame({
  'Year': [2018, 2019, 2020, 2021],
  'Sales': [350, 480, 550, 680]
})
 
# Create a line chart
st.line_chart(data)

         

