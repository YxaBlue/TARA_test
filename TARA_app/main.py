# To run the app, RUN THIS FILE
# Make sure to save progress on all modules

import streamlit as st
from landing_page import render_landing_page


st.set_page_config(page_title="TARA", layout="wide")

render_landing_page()