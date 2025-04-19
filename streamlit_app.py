import streamlit as st
from PIL import Image

st.set_page_config(layout="wide")

# --- Custom CSS ---
st.markdown("""
    <style>
    body {
        background-color: #363c56;
        color: #00a9e0;
    }
    .main-container {
        display: grid;
        grid-template-columns: 280px 1fr;
        grid-template-rows: 80px 1fr;
        grid-template-areas:
            "sidebar header"
            "sidebar main";
        height: 100vh;
    }
    .header {
        grid-area: header;
        background-color: #242839;
        padding: 15px 30px;
        display: flex;
        align-items: center;
        gap: 20px;
    }
    .sidebar {
        grid-area: sidebar;
        background-color: #2a2f45;
        padding: 20px 10px;
        display: flex;
        flex-direction: column;
        align-items: flex-start;
    }
    .main {
        grid-area: main;
        padding: 30px;
    }
    .menu-button {
        width: 100%;
        text-align: left;
        background-color: #242839;
        color: #00a9e0;
        font-size: 18px;
        font-weight: bold;
        padding: 15px;
        margin: 10px 0;
        border: none;
        border-left: 5px solid #00a9e0;
    }
    .menu-button:hover {
        background-color: #575969;
    }
    .user-section {
        margin-top: auto;
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 20px;
    }
    .mode-toggle {
        background-color: #2a2f45;
        border-radius: 20px;
        padding: 5px 10px;
        display: flex;
        align-items: center;
        gap: 10px;
    }
    .darkmode-label {
        font-size: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# --- HTML Layout ---
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# --- Sidebar ---
st.markdown('<div class="sidebar">', unsafe_allow_html=True)

logo = Image.open("images/StephensonLogo.png")
st.image(logo, width=50)
st.markdown('<h4 style="color:#00a9e0; margin-top: 5px;">Stephenson</h4>', unsafe_allow_html=True)

# Menu buttons
st.markdown('<button class="menu-button">⬆️ Upper Tank Farm</button>', unsafe_allow_html=True)
st.markdown('<button class="menu-button">⬇️ Lower Tank Farm</button>', unsafe_allow_html=True)

# Spacer and user
pfp = Image.open("images/UserPFP.png")
st.markdown('<div class="user-section">', unsafe_allow_html=True)
st.image(pfp, width=40)
st.markdown('<div>FirstN LastN</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Dark/Light mode toggle
light = Image.open("images/LightMode.png")
dark = Image.open("images/DarkMode.png")
st.markdown('<div class="mode-toggle">', unsafe_allow_html=True)
col1, col2 = st.columns([1,1])
with col1:
    st.image(light, width=30)
with col2:
    st.image(dark, width=30)
st.markdown('</div>', unsafe_allow_html=True)
st.markdown('<div class="darkmode-label">Dark Mode</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # end sidebar

# --- Header ---
st.markdown('<div class="header"><h3>Upper Tank Farm (UTF)</h3></div>', unsafe_allow_html=True)

# --- Main Content Placeholder ---
st.markdown('<div class="main"><p>Welcome to the overview dashboard!</p></div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # end main-container
