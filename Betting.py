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
    st.write(":white_check_mark: The Board :moneybag: showing future games with odds.")
    st.write(":white_check_mark: Trends :bar_chart: showing trends of records, covers, odds")
    st.write(":white_check_mark: System :lock: shows bets that strategy and models are picking")
    st.write(":white_check_mark: Performance :rocket: shows your own picks, strategy, public records")
    st.write(":white_check_mark: Education :books: shows odds, strategy and relavant articles")    
    

# "Education" tab
with tabs[2]:
    st.header("Education")

    with st.expander("Odds Format - Decimal"):
        st.write("Betting Odds will be displayed as European/Decimal Odds. This graphic will give an example of how they compare to traditional Moneyline/US Odds.")
        st.image("https://www.soccerwidow.com/wp-content/uploads/2013/11/odds-conversion-table.jpg")

    with st.expander("Types of Bets"):
        st.write("Moneyline - ")
        st.write("Point Spread - ")
        st.write("Totals - ")
        st.write("Parlay - ")
        st.write("Futures - ")
        st.write("Props - ")

    with st.expander("Bankroll Management"):
        st.write("Spend it all, YOLO")
        st.write("Kelly Criterion")


# "Roadmap" tab
with tabs[3]:
    st.header("Roadmap")
    st.write(":construction: Weather Data")
    st.write(":construction: Public Betting Data")
    st.write(":construction: Coaching Tenure")
    st.write(":construction: Website Login")
    st.write(":construction: Bets Taken History")
    st.write(":construction: Twitter bot")
    st.write(":construction: News/Injury Updates")
 
