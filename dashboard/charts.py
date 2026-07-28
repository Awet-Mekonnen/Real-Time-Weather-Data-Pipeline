import streamlit as st
import plotly.express as px

"""
# This function is used to display the charts on the dashboard
# the y coordinate is the timestamp for every chart while the x coordinates
# are temperature, humidity, and wind_speed for their charts respectively
"""
def display_charts(df):

    temp_fig = px.line(
        df,
        x = "timestamp",
        y = "temperature",
        title = "Tempreature Over Time",
        markers = True
    )

    st.plotly_chart(temp_fig, use_container_width = True)

    hum_fig = px.line(
        df,
        x = "timestamp",
        y = "humidity",
        title = "Humidity Over Time",
        markers = True
    )

    st.plotly_chart(hum_fig, use_container_width = True)

    wind_fig = px.line(
        df,
        x = "timestamp",
        y = "wind_speed",
        title = "Wind Speed Over Time",
        markers = True
    )

    st.plotly_chart(wind_fig, use_container_width = True)