import streamlit as st
import plotly.graph_objects as go
import requests
import json
import paho.mqtt.client as mqtt
from json2html import *
from datetime import datetime
import time
import pandas as pd
import streamlit.components.v1 as components

st.set_page_config(layout="wide", initial_sidebar_state='expanded')
# SET THE API FROM WHICH TO EXTRACT DATA
markethost = 'http://YOUR_LINK'

# CREATE YOUR CSS FILE
 
with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
st.sidebar.header('Dashboard NAME')
st.sidebar.subheader('YOUR SUB HEADER')
with st.sidebar:
    add_radio = st.radio(
        "CHANGE THOS",
        ("CHANGE THIS", "CHANGE THIS")
    )

# THIS IS THE RELEVANT PART
# THIS SHOWS HOW TO CALL A HTML FILE IN STREAMLIT
st.markdown("### YOUR_TITLE")
HtmlFile = open("live-chart.html",'r', encoding='utf-8')
source_code = HtmlFile.read() 
components.html(source_code, height = 400)
    
      