import streamlit as st

# Custom imports 
from multiapp import MultiPage
import apps as week
from week import app



# Create an instance of the app 
app = MultiPage()

# Title of the main page
st.title("Data Storyteller Application")

# Add all your applications (pages) here
app.add_page("Upload Data", week.app)
app.add_page("Change Metadata", month.app)
app.add_page("Machine Learning", quarter.app)
app.add_page("Data Analysis", year.app)

# The main app
app.run()
