import streamlit as st
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

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