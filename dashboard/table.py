import streamlit as st
"""
# This funciton is used to display the table collecting the values of the
# variables collected from the queries and display them on the dashboard
# as well as allow the user to download a csv file consisting of those values.
"""
def display_table(df):

    st.subheader("Latest Records")
    display_df = df.drop(columns = ["latitude", "longitude"])
    st.dataframe(display_df, use_container_width = True)

    csv = df.to_csv(index = False)

    st.download_button(
        "Download CSV",
        csv,
        "weather_data.csv",
        "text/csv"
    )