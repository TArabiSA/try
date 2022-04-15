import streamlit as st

# Custom imports 
from multipage import MultiPage
from apps import week, month, quarter, year # import your pages here

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
