import streamlit as st

def render_navbar():
    # Custom CSS for nav bar
    st.markdown("""
        <style>
            .nav-container {
                position: fixed;
                top: 120px;
                left: 50%;
                transform: translateX(-50%);
                width: 90%;
                margin: -110px auto;
                border: 3px solid black;
                border-radius: 20px;
                background-color: #fcf6f5;
                padding: 10px 30px;
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            
            .main {
                margin-top: 110px;
            }

            .nav-logo img {
                height: 40px;
            }

            .nav-buttons {
                display: flex;
                gap: 10px;
            }

            .nav-button {
                border: 2px solid black;
                padding: 10px 20px;
                text-decoration: none;
                color: black;
                border-radius: 8px;
                font-weight: 600;
                transition: background-color 0.2s ease;
            }
                
            .first-btn {
                background-color: #d9d9d9;
            }

            .second-btn {
                background-color: #d9d9d9;
            }

            .third-btn {
                background-color: #ce7867;
            }            

            .nav-button:hover {
                opacity: 0.85;
                cursor: pointer;
            }
        </style>
    """, unsafe_allow_html=True)

    # Insert the nav bar using HTML
    st.markdown("""
        <div class="nav-container">
            <div class="nav-logo">
                <img src="https://i.postimg.cc/SxJpJ1H7/sample-logo.png" alt="Logo">
            </div>
            <div class="nav-buttons">
                <a class="nav-button first-btn" href="#home">----------</a>
                <a class="nav-button second-btn" href="#assessment">----------</a>
                <a class="nav-button third-btn" href="#contact">----------</a>
            </div>
        </div>
    """, unsafe_allow_html=True)
