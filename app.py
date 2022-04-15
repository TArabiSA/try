import streamlit as st
st.set_page_config(page_title="Taba Pares House", page_icon=":chart_with_upwards_trend:", layout= "wide")

# Custom imports 
from multipage import MultiPage
from apps import week,month,quarter,year



# Create an instance of the app 
app = MultiPage()
st.markdown("""
# Taba Pares House Sale's Forecasting using LSTM
[Fabook page](https://www.facebook.com/TABAPARESHOUSE).
""")

Navigation_name = st.selectbox("Select Prediction", ("WEEK", "MONTH", "QUARTER", "YEAR"))


# Title of the main page
st.title("Data :page_facing_up: ")

# Add all your applications (pages) here
app.add_page("WEEK",week.app)
app.add_page("MONTH",month.app)
app.add_page("QUARTER",quarter.app)
app.add_page("YEAR",year.app)

# The main app
app.run()
