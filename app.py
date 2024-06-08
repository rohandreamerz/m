import streamlit as st
import os
from streamlit_lottie import st_lottie
import json 
from PIL import Image
import time
import pandas as pd
import plotly.express as px

st.balloons()
time.sleep(1)
st.balloons()
time.sleep(1)
st.balloons()
time.sleep(2)

file_path = __file__
dir_name = os.path.dirname(file_path)
lottie_url= os.path.join(dir_name, "happy_bday.json")

st.markdown("<h1 style='text-align: center; color: #FF3C00;'>Hi Sapnaa...</h1>", unsafe_allow_html=True)

with open(lottie_url, "r") as f:
        lottie_json = json.load(f)

if lottie_json is not None:
        st_lottie(lottie_json)
else:
        pass

time.sleep(3)
st.markdown("<p style='font-family:cursive;font-size:30px;text-align: center; color: black;'>May all your Dreams Come True!🌈.<br>Cheers 🥂 to a fantastic year ahead!<br>-----------<br>Yours Truly,<br>Rohan</p>",unsafe_allow_html=True)
