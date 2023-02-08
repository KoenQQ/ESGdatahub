
import streamlit as st
import pandas as pd


# dashboard that allows filtering from ESG dataset on Heroku database

st.title('ESG data')
st.subheader('data from a wide variety of countries & companies that you can scroll through')

df = pd.DataFrame({
  'first column': [1, 2, 3, 4],
  'second column': [10, 20, 30, 40]
})

df

