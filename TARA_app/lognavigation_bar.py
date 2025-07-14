import streamlit as st

def render_log_navbar():
    st.markdown(
        """
        <div style="width: 100vw; position: fixed; top: 20px; left: 0; z-index: 0; display: flex; justify-content: center;">
            <div style="position: relative; width: 90%;">
                <img src='https://res.cloudinary.com/dxrsfbpbq/image/upload/v1752496828/Menu_logged_p5quyt.png' style='width: 100%; display: block;'>
            </div>
        </div>
        <div style="height: 0px;"></div>
        """,
        unsafe_allow_html=True
    )
