import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

st.title('This is my first streamlit app test')

#we use triple  quotes when the string has more than a line
st.markdown("""
This is my first streamlit's app
* **Name:** Jorge Caceres
* **Interests:** I want to learn about data science.
""")

#this will create the sidebar of the website
st.sidebar.header('User input features')

#we will display the years with this
#to generate the years we use range which includes the first parameter but exludes the second one.
selected_year = st.sidebar.selectbox('Year', list(reversed(range(1990, 2022))))


def load_data(year):
    url = "https://www.basketball-reference.com/leagues/NBA_"+ str(year)+ "_per_game.html"
    html = pd.read_html(url, header = 0)
    df = html[0]
    raw = df.drop(df[df.Age == 'Age'].index)
    raw = raw.fillna(0)
    player_stats = raw.drop(['Rk'], axis = 1)
    return player_stats

playerstats = load_data(selected_year)

#Sidebar - Team selection
sorted_unique_team = sorted(playerstats.Tm.unique())
# The third parameter will be the default value of the multiselect field.
selected_team = st.sidebar.multiselect("NBA's TEAMS", sorted_unique_team, sorted_unique_team)

#Sidebar - Players' age
sorted_unique_age = sorted(playerstats.Age.unique())
selected_age = st.sidebar.multiselect("AGE", sorted_unique_age, sorted_unique_age)

#Sidebar - Player's positions
unique_pos = ['C', 'PF', 'SF', 'PG', 'SG']
selected_pos = st.sidebar.multiselect('POSITION', unique_pos, unique_pos)

#Data filtering
df_selected_team = playerstats[(playerstats.Tm.isin(selected_team)) & (playerstats.Pos.isin(selected_pos)) & (playerstats.Age.isin(selected_age))]

st.header('Player Stats')
st.write('Data dimension: '+ str(df_selected_team.shape[0]) + ' rows and '+ str(df_selected_team.shape[1]) + ' columns')
st.dataframe(df_selected_team)