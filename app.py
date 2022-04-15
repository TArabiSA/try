import streamlit as st
st.set_page_config(page_title="Taba Pares House", page_icon=":chart_with_upwards_trend:", layout= "wide")
from multiapp import MultiApp
from apps import week, month, quarter, year





app = MultiApp()
st.markdown("""
# Taba Pares House Sale's Forecasting using LSTM
[Fabook page](https://www.facebook.com/TABAPARESHOUSE).
""")

# Add all your application here
app.add_app("WEEK", week.app)
app.add_app("MONTH", month.app)
app.add_app("QUARTER", quarter.app)
app.add_app("YEAR", year.app)
# The main app
app.run()
