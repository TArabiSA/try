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
app.add_app("WEEK", .app)
app.add_app("MONTH", .app)
app.add_app("QUARTER", .app)
app.add_app("YEAR", .app)
# The main app
app.run()
