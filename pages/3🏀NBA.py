import streamlit as st
import pandas as pd
from datetime import date
from fargen_pg import fetch_data, init_connection

st.set_page_config(page_title="Degen Betting"
                    , layout="wide"
                    , page_icon=":slot_machine:"
                    , initial_sidebar_state="expanded")

# Page-specific configurations
st.title("NBA Games Dashboard")

# Example of creating filters on the sidebar
with st.sidebar:
    st.header("NBA Filters")
    
    # Date picker for selecting a date
    selected_date = st.date_input("Select a Date", value=date.today())
    
    # Dropdown for selecting a specific NBA team
    teams = ["All", "Lakers", "Warriors", "Bulls", "Nets", "Celtics"]  # Example team list
    selected_team = st.selectbox("Select Team", options=teams)
    
    # Buttons for additional filters (e.g., Conference or Division)
    st.write("Conference Filters")
    if st.button("Eastern Conference"):
        st.write("Displaying Eastern Conference games...")
    if st.button("Western Conference"):
        st.write("Displaying Western Conference games...")
    
    # Custom filter button for reset
    if st.button("Reset Filters"):
        st.write("Filters have been reset.")


# Initialize connection to the database
engine = init_connection()

# Creating tabs for each sport
tabs = st.tabs(["The Board :moneybag:", "Trends :bar_chart:", "System :lock:", "Performance :rocket:", "Education :books:"])

# "Upcoming Games" tab
with tabs[0]:
    st.header("Upcoming Games")
    st.write("Here are the upcoming games for all sports.")
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
    st.write(f"Displaying NBA games for: {selected_date}")

    # Fetch data based on the selected date
    try:
        nba_df = fetch_data('SCHED', engine, filter_date=str(selected_date))
        st.dataframe(nba_df)
    except Exception as e:
        st.error(f"Error fetching data: {e}")

# "NFL" tab
with tabs[2]:
    st.header("NFL Games")
    st.write("View the latest NFL games, odds, and betting information.")
    st.write(f"Displaying NFL games for: {selected_date}")

    # Fetch data based on the selected date
    try:
        nfl_df = fetch_data('SCHED', engine, filter_date=str(selected_date))
        st.dataframe(nfl_df)
    except Exception as e:
        st.error(f"Error fetching data: {e}")

# "MLB" tab
with tabs[3]:
    st.header("MLB Games")
    st.write("View the latest MLB games, odds, and betting information.")
    st.write(f"Displaying MLB games for: {selected_date}")

    # Fetch data based on the selected date
    try:
        mlb_df = fetch_data('SCHED', engine, filter_date=str(selected_date))
        st.dataframe(mlb_df)
    except Exception as e:
        st.error(f"Error fetching data: {e}")

# "NHL" tab
with tabs[4]:
    st.header("NHL Games")
    st.write("View the latest NHL games, odds, and betting information.")
    st.write(f"Displaying NHL games for: {selected_date}")

    # Fetch data based on the selected date
    try:
        nhl_df = fetch_data('SCHED', engine, filter_date=str(selected_date))
        st.dataframe(nhl_df)
    except Exception as e:
        st.error(f"Error fetching data: {e}")