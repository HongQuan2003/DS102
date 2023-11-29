import streamlit as st
import pandas as pd


st.title("Data Visualization")

st.header("upload data")

data_file = st.file_uploader("choose a csv file")

if data_file is not None:
    df = pd.read_csv(data_file)
  
    st.header("Show data")
    st.dataframe(df)
    
    st.header("Des")
    st.table(df.describe())
    
    st.header("Info")
    buffer = io.stringIO()
    df.info(buf=buffer)
    st.text(buffer.getvalue())

    st.header("Visualize each attribute")
    for col in list(df.columns):
    


