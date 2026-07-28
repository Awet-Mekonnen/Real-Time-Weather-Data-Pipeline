import streamlit as st
"""
# This function is used to collect the latitude and longitude
# and display it on the dashboard.
"""
def display_map(df):
    
    st.subheader("Collection Location")

    st.map(
        df[["latitude", "longitude"]]
    )

    st.markdown(
        f"### Location: **Las Vegas, Nevada, USA**"
    )