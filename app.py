import streamlit as st

# Custom imports 
from multiapp import MultiPage
import apps as week
import apps as month
import apps as quarter
import apps as year



# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.title("Data Storyteller Application")

# Add all your applications (pages) here
app.add_page("Upload Data", week)
app.add_page("Change Metadata", month)
app.add_page("Machine Learning", quarter)
app.add_page("Data Analysis", year)

# The main app
app.run()
