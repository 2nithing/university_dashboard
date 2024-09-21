import streamlit as st
import pandas as pd
import plotly.express as px
st.set_page_config(layout='wide')

st.header('World University Dashboard')

df = pd.read_csv('mentornow/timesData.csv')

with st.expander("Show data"):
    st.write(df)

sd = st.sidebar
options = sd.multiselect('Select y axis',['teaching','research','citations'])
selected_year = sd.select_slider('Select Year',options=range(2011,2017))

col1,col2 = st.columns(2)

fig1 = px.line(df[df['year']==selected_year].iloc[:100], x='world_rank', y=options)
col1.plotly_chart(fig1)

fig2 = px.bar(df[df['year']==selected_year].iloc[:3],x='university_name',y=options,barmode='group')
col2.plotly_chart(fig2)

sd.subheader('Hi')