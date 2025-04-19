import streamlit as st
from PIL import Image

# --- Custom CSS for styling ---
st.markdown("""
    <style>
        body {
            background-color: #363c56;
        }
        .title-bar {
            background-color: #242839;
            padding: 20px;
            margin-bottom: 0;
        }
        .side-menu {
            background-color: #2a2f45;
            height: 100vh;
            padding: 10px;
        }
        .menu-button {
            background-color: #242839;
            color: #00a9e0;
            font-weight: bold;
            font-size: 18px;
            border: none;
            padding: 15px;
            width: 100%;
            margin-bottom: 10px;
        }
        .menu-button:hover {
            background-color: #575969;
        }
        .highlight-bar {
            background-color: #00a9e0;
            width: 5px;
            height: 90px;
            float: left;
            margin-right: 10px;
        }
        .user-info {
            color: #00a9e0;
            font-size: 18px;
            margin-top: 100px;
        }
        .mode-toggle {
            background-color: #2a2f45;
            border-radius: 20px;
            padding: 5px 10px;
            width: fit-content;
            margin-top: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .mode-label {
            color: #00a9e0;
            font-size: 15px;
        }
    </style>
""", unsafe_allow_html=True)

# --- Top bar with logo and title ---
st.markdown('<div class="title-bar">', unsafe_allow_html=True)
cols = st.columns([0.1, 0.3, 0.6])
with cols[0]:
    logo = Image.open("StephensonLogo.png")
    st.image(logo, width=50)
with cols[1]:
    st.markdown('<h3 style="color: #00a9e0;">Stephenson</h3>', unsafe_allow_html=True)
with cols[2]:
    st.markdown('<h2 style="color: #00a9e0;">Upper Tank Farm (UTF)</h2>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# --- Main layout with sidebar ---
left_col, right_col = st.columns([0.2, 0.8])

with left_col:
    st.markdown('<div class="side-menu">', unsafe_allow_html=True)

    # Upper Tank button
    st.markdown('<div class="highlight-bar"></div>', unsafe_allow_html=True)
    st.markdown('<button class="menu-button">⬆️ Upper Tank Farm</button>', unsafe_allow_html=True)

    # Lower Tank button
    st.markdown('<button class="menu-button">⬇️ Lower Tank Farm</button>', unsafe_allow_html=True)

    # User info
    pfp = Image.open("UserPFP.png")
    st.image(pfp, width=40)
    st.markdown('<div class="user-info">FirstN LastN</div>', unsafe_allow_html=True)

    # Light/Dark mode toggle
    st.markdown('<div class="mode-toggle">', unsafe_allow_html=True)
    light_icon = Image.open("LightMode.png")
    dark_icon = Image.open("DarkMode.png")
    col1, col2 = st.columns([0.5, 0.5])
    with col1:
        st.image(light_icon, width=40)
    with col2:
        st.image(dark_icon, width=40)
    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('<div class="mode-label">Dark Mode</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

with right_col:
    st.markdown("<!-- Main content would go here -->")
    st.markdown('<p style="color: #00a9e0;">Welcome to the Stephenson Tank Dashboard!</p>', unsafe_allow_html=True)
