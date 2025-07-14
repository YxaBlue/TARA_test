import streamlit as st
from lognavigation_bar import render_log_navbar

st.set_page_config(page_title="TARA", layout="wide")

def render_upskilling_page():
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: url(https://res.cloudinary.com/dxrsfbpbq/image/upload/v1752510189/Upskilling_Page_wbmzkr.png);
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    </style>
    """

    render_log_navbar()
    st.markdown(page_bg_img, unsafe_allow_html=True)