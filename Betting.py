import streamlit as st
from datetime import date
from fargen_pg import fetch_data, init_connection
import yaml

# python -m streamlit run Betting.py

# # Load configuration file
# with open("config.yaml", "r") as file:
#     config = yaml.safe_load(file)

# # Build sidebar with custom order
# for page in config["pages"]:
#     if st.sidebar.button(page["name"]):
#         st.write(f"Loading {page['name']} page...")
#         # Use exec or custom logic to include corresponding page file dynamically

st.set_page_config(page_title="Degen Betting"
                    , layout="wide"
                    , page_icon=":slot_machine:"
                    , initial_sidebar_state="expanded")


# Title of the main dashboard
st.title(":slot_machine: Degen Dashboard")

  
# Initialize connection to the database
engine = init_connection()


# Example of creating filters on the sidebar
with st.sidebar:
    st.header("NBA Filters")
    
    # Date picker for selecting a date
    selected_date = st.date_input("Select a Date", value=date.today())


# Creating tabs for each sport
tabs = st.tabs(["Games :moneybag:", "Feature :lock:", "Education :books:", "Roadmap 🚗"])

# "Upcoming Games" tab
with tabs[0]:
    st.header("Upcoming Games")
    st.write("Here are the upcoming games for all sports.")
        #  Probably show yesterday's completed games and next week of games??
    st.write(f"Displaying games for:   {selected_date}")
    
    # Fetch data based on the selected date
    try:
        upcoming_games_df = fetch_data('SCHED', engine, filter_date=str(selected_date))
        st.dataframe(upcoming_games_df)
    except Exception as e:
        st.error(f"Error fetching data: {e}")

# "Feature" tab
with tabs[1]:
    st.header("Features")
    st.write("View the latest NBA games, odds, and betting information.")
    

# "Education" tab
with tabs[2]:
    st.header("Education")
    st.write("View the latest NFL games, odds, and betting information.")


# "Roadmap" tab
with tabs[3]:
    st.header("Roadmap")
    st.write("View the latest MLB games, odds, and betting information.")
 
