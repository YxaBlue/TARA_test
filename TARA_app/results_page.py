import streamlit as st
from lognavigation_bar import render_log_navbar

st.set_page_config(page_title="TARA", layout="wide")

def render_results_page():
    # Determine background based on test result
    passed_bg = "https://res.cloudinary.com/dxrsfbpbq/image/upload/v1752509274/Job_Assessment_Results_PASSED_pbrdyl.png"
    failed_bg = "https://res.cloudinary.com/dxrsfbpbq/image/upload/v1752509272/Job_Assessment_Results_FAILED_b5lvy1.png"
    bg_url = passed_bg if st.session_state.get('test_result') == 'pass' else failed_bg

    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url({bg_url});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    </style>
    """

    render_log_navbar()
    st.markdown(page_bg_img, unsafe_allow_html=True)

    st.markdown("""
    <style>
    div[data-testid="stButton"] > button {
        width: 100% !important;
        max-width: 600px !important;
        height: 70px !important;
        font-size: 1.1rem !important;
        margin: 0 auto;
        margin-top: 450px;   
        margin-left: 230px; 
        display: block;
        opacity: 0;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<br><br><br><br>", unsafe_allow_html=True) 

    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)
        next_btn = st.button("Next", key="next_btn", use_container_width=True)
        if next_btn:
            st.session_state.page = "Upskill"  