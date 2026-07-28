import streamlit as st

"""
# This function is used to display the mechanincs and architecture of the
# Dashboard. An expander function is used to help minimize the information
# and let the user access it by their choice
"""

def display_about():
    
    with st.expander("📖 About This Project"):

        st.markdown("""
Overview
                    
This project automatically collects weather data every hour using
AWS Lambda and Amazon EventBridge.

The data is stored in Amazon S3, cataloged with AWS Glue,
queried using AWS Athena, and visualized with Streamlit.
                    
---
                    
Architecture

- Open-Meteo API
- AWS Lambda
- Amazon S3
- AWS Glue (Database and Crawler)
- Amazon Athena
- Streamlit Dashboard

Technologies
                    
- Python
- AWS Lambda
- AWS SAM
- Amazon EventBridge
- Amazon S3
- AWS Glue
- Amazon Athena
- Streamlit
- Plotly
- Pandas
- PyAthena
    """)