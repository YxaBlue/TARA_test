import streamlit as st
from navigation_bar import render_navbar

st.set_page_config(page_title="TARA", layout="wide")

def render_landing_page():
    # Landing Page Background
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url(https://res.cloudinary.com/doddwukae/image/upload/v1752430731/Log_in_Page_ecat10.png);
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """

    # Display Background
    render_navbar()
    st.markdown(page_bg_img, unsafe_allow_html=True)