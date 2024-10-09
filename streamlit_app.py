import streamlit as st
import pandas as pd
from datetime import date
import psycopg2
from sqlalchemy import create_engine

# python -m streamlit run streamlit_app.py

st.set_page_config(page_title="Degen Betting"
                    , layout="wide"
                    , page_icon=":man_with_probing_cane:"
                    , initial_sidebar_state="expanded")

# Database connection configuration (replace with your credentials)
DB_HOST = "localhost"
DB_PORT = "15432"
DB_NAME = "SPORT"
DB_USER = "postgres"
DB_PASS = "Th3iri$h"

# Function to connect to PostgreSQL database
@st.cache_resource
def init_connection():
    return create_engine(f'postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

# Function to fetch data from a specified table
# def fetch_data(table_name, engine):
#     query = f'SELECT * FROM "SPORT"."ALL"."{table_name}" LIMIT 500'
#     return pd.read_sql(query, con=engine)
def fetch_data(table_name, engine, filter_date=None):
    if filter_date:
        query = f'''SELECT * FROM "SPORT"."ALL"."{table_name}" WHERE "GAME_DT" = '{filter_date}' '''
    else:
        query = f'SELECT * FROM "SPORT"."ALL"."{table_name}"'
    return pd.read_sql(query, con=engine)

# Title of the main dashboard
st.title(":man_with_probing_cane: Degen Dashboard")


# Initialize connection to the database
engine = init_connection()

# Creating tabs for each sport
tabs = st.tabs(["The Board :moneybag:", "NBA", "NFL", "MLB", "NHL"])

# "Upcoming Games" tab
with tabs[0]:
    st.header("Upcoming Games")
    st.write("Here are the upcoming games for all sports.")

    # Date picker filter for upcoming games
    selected_date = st.date_input("Select a Date", value=date.today())
    st.write(f"Displaying games for: {selected_date}")
    
    # Fetch data based on the selected date
    try:
        upcoming_games_df = fetch_data('SCHED', engine, filter_date=str(selected_date))
        st.dataframe(upcoming_games_df)
    except Exception as e:
        st.error(f"Error fetching data: {e}")

# "NBA" tab
with tabs[1]:
    st.header("NBA Games")
    st.write("View the latest NBA games, odds, and betting information.")
    
    # Date picker for filtering NBA games
    selected_nba_date = st.date_input("Select a Date for NBA Games", value=date.today(), key='nba_date')
    st.write(f"Displaying NBA games for: {selected_nba_date}")

    # Fetch data based on the selected date
    try:
        nba_df = fetch_data('nba_games', engine, filter_date=str(selected_nba_date))
        st.dataframe(nba_df)
    except Exception as e:
        st.error(f"Error fetching data: {e}")

# "NFL" tab
with tabs[2]:
    st.header("NFL Games")
    st.write("View the latest NFL games, odds, and betting information.")
    
    # Date picker for filtering NFL games
    selected_nfl_date = st.date_input("Select a Date for NFL Games", value=date.today(), key='nfl_date')
    st.write(f"Displaying NFL games for: {selected_nfl_date}")

    # Fetch data based on the selected date
    try:
        nfl_df = fetch_data('nfl_games', engine, filter_date=str(selected_nfl_date))
        st.dataframe(nfl_df)
    except Exception as e:
        st.error(f"Error fetching data: {e}")

# "MLB" tab
with tabs[3]:
    st.header("MLB Games")
    st.write("View the latest MLB games, odds, and betting information.")
    
    # Date picker for filtering MLB games
    selected_mlb_date = st.date_input("Select a Date for MLB Games", value=date.today(), key='mlb_date')
    st.write(f"Displaying MLB games for: {selected_mlb_date}")

    # Fetch data based on the selected date
    try:
        mlb_df = fetch_data('mlb_games', engine, filter_date=str(selected_mlb_date))
        st.dataframe(mlb_df)
    except Exception as e:
        st.error(f"Error fetching data: {e}")

# "NHL" tab
with tabs[4]:
    st.header("NHL Games")
    st.write("View the latest NHL games, odds, and betting information.")
    
    # Date picker for filtering NHL games
    selected_nhl_date = st.date_input("Select a Date for NHL Games", value=date.today(), key='nhl_date')
    st.write(f"Displaying NHL games for: {selected_nhl_date}")

    # Fetch data based on the selected date
    try:
        nhl_df = fetch_data('nhl_games', engine, filter_date=str(selected_nhl_date))
        st.dataframe(nhl_df)
    except Exception as e:
        st.error(f"Error fetching data: {e}")