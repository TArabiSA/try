import streamlit as st
# Create a page dropdown 
page = st.selectbox("Choose your page", ["Page 1", "Page 2", "Page 3"]) 
if page == "WEEK":
    # Display details of page 1
elif page == "MONTH":
    # Display details of page 2
elif page == "QUARTER":
    # Display details of page 3
elif page == "YEAR":
    # Display details of page 4
    
