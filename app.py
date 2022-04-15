import streamlit as st
st.set_page_config(page_title="Taba Pares House", page_icon=":chart_with_upwards_trend:", layout= "wide")
from multiapp import MultiApp
import apps as week
import apps as month 
import apps as quarter
import apps as year





app = MultiApp()
st.markdown("""
# Taba Pares House Sale's Forecasting using LSTM
[Fabook page](https://www.facebook.com/TABAPARESHOUSE).
""")

# Add all your application here
app.add_app("WEEK", apps.app)
app.add_app("MONTH", apps.app)
app.add_app("QUARTER", apps.app)
app.add_app("YEAR", apps.app)
# The main app
app.run()
