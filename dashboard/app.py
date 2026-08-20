import streamlit as st
import pandas as pd

from utils import run_query
from queries import get_query
from about import display_about
from metrics import display_metrics
from charts import display_charts
from table import display_table
from map import display_map

# Display the title of the Dashboard at the top
st.set_page_config(
    page_title= "Weather Data Pipeline",
    page_icon = "🌤",
    layout = "wide"
)

st.title("🌤 Weather Data Pipeline Dashboard")

# This function displays the mechanics and architecture used to make the dashboard
display_about()

# This is a selection box to help the user interact with the dashboard
# letting them format the data
time_filter = st.selectbox(
    "Select Time Range",
    ["Last 24 Hours", "Last 7 Days", "Last 30 Days", "All Data"]
)

query = get_query(time_filter)

# Exception handling used to check for any errors when running the dashboard
# And display the appropriate error message
try:
    df = run_query(query)

    df["timestamp"] = pd.to_datetime(df["timestamp"], format = "mixed", utc = "true")
    df = df.sort_values("timestamp")

    display_map(df)
    display_metrics(df)
    display_charts(df)
    display_table(df)

except Exception as e:
    st.error("Unable to load data.")
    st.exception(e)
