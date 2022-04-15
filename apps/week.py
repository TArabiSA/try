from html.entities import html5
import streamlit as st
import numpy as np
import pandas as pd
import requests
import matplotlib.pyplot as plt
import tensorflow as tf
from streamlit_lottie import st_lottie



def app():
 st.title('Data :page_facing_up:')   

 st.write("The following is the DataFrame of the `Taba Pares House` dataset.")

 def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#-------LOAD ASSETS------
 lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_o6spyjnc.json") 


 with st.container():
    
    left_column, right_column = st.columns(2)
    with left_column:
        df = pd.read.csv(r"C:/Users/yakul/mutipage/data/week.csv")
        st.write(df)
    with right_column:
        st_lottie(lottie_coding, height = 300, key ="coding")