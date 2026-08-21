import streamlit as st
"""
# This function is used to display the metrics of the data collected from
# the database. The data collected are temperature, humidity, and wind speed.
"""
def display_metrics(df):

    # This is used to get the latest value in the table 
    latest = df.iloc[-1]

    st.header("Current Weather")
    
    temp = latest['temperature']
    # These columns are declared to display the values on the dashboard
    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Temperature",
        f"{temp:.2f} °F"
    )

    c2.metric(
        "Humidity",
        f"{latest['humidity']:.2f}%"
    )

    c3.metric(
        "Wind Speed",
        f"{latest['wind_speed']:.2f} km/h"
    )

    st.header("Statisitcs")

    display_stats(c1, "Temperature", df["temperature"], "°F")
    display_stats(c2, "Humidity", df["humidity"], "%")
    display_stats(c3, "Wind Speed", df["wind_speed"], "mph")


"""
# This function is used to calculate the average, maximum, and minimum
# of the values collected from the database and display on the dashboard.
"""
def display_stats(col, title, data, unit):

    avg = data.mean()
    maximum = data.max()
    minimum = data.min()

# This if statement is used when the title is Temperature in order to convert the data
# from celcius to Farenhite

    with col:
        st.subheader(title)

        st.write(f"**Average:** {avg:.1f} {unit}")
        st.write(f"**Maximum:** {maximum:.1f} {unit}")
        st.write(f"**Minimum:** {minimum:.1f} {unit}")
