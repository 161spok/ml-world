import streamlit as st

st.write("Duplicati")

# Check for duplicate rows
duplicates = data.duplicated().sum()
st.write("Number of duplicate rows:", duplicates)
                                      
# Removing duplicate rows
data.drop_duplicates(inplace=True)
st.write(data)
