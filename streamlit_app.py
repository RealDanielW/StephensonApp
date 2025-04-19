import streamlit as st
from PIL import Image
import base64

# Set the page layout to wide
st.set_page_config(layout="wide")

# Load images
logo = Image.open("images/StephensonLogo.png")
arrow_up = Image.open("images/ArrowUp.png")
arrow_down = Image.open("images/ArrowDown.png")
pfp = Image.open("images/UserPFP.png")
light_mode = Image.open("images/LightMode.png")
dark_mode = Image.open("images/DarkMode.png")

# --- CSS Styles ---
st.markdown("""
    <style>
    body {
        margin: 0;
        background-color: #363c56;
    }
    .container {
        position: relative;
        width: 1920px;
        height: 1080px;
        background-color: #363c56;
    }
    .title-bar {
        position: absolute;
        top: 0;
        left: 0;
        width: 1920px;
        height: 80px;
        background-color: #242839;
    }
    .title-text {
        position: absolute;
        top: 12px;
        left: 300px;
        font-size: 26px;
        font-weight: bold;
        color: #00a9e0;
    }
    .sidebar {
        position: absolute;
        top: 0;
        left: 0;
        width: 280px;
        height: 1080px;
        background-color: #2a2f45;
    }
    .logo-img {
        position: absolute;
        top: 13px;
        left: 5px;
        width: 50px;
        height: 50px;
    }
    .stephenson-text {
        position: absolute;
        top: 12px;
        left: 70px;
        font-size: 24px;
        color: #00a9e0;
    }
    .line1 {
        position: absolute;
        top: 79px;
        left: 17px;
        width: 243px;
        height: 3px;
        background-color: #242839;
        border-radius: 3px;
    }
    .menu-btn {
        position: absolute;
        width: 274px;
        height: 90px;
        background-color: #242839;
        border: none;
        padding: 0;
    }
    .menu-btn:hover {
        background-color: #575969;
    }
    .white-line {
        position: absolute;
        width: 5px;
        height: 90px;
        background-color: #00a9e0;
        left: 0;
    }
    .arrow-img {
        position: absolute;
        width: 40px;
        height: 40px;
        left: 20px;
    }
    .menu-text {
        position: absolute;
        font-size: 18px;
        font-weight: bold;
        color: #00a9e0;
        left: 80px;
    }
    .profile-name {
        position: absolute;
        font-size: 18px;
        color: #00a9e0;
        left: 80px;
        top: 880px;
    }
    .pfp-img {
        position: absolute;
        width: 40px;
        height: 40px;
        left: 20px;
        top: 880px;
    }
    .line2 {
        position: absolute;
        top: 930px;
        left: 17px;
        width: 243px;
        height: 3px;
        background-color: #242839;
        border-radius: 3px;
    }
    .oval {
        position: absolute;
        width: 100px;
        height: 40px;
        top: 950px;
        left: 150px;
        background-color: #363c56;
        border-radius: 15px;
    }
    .oval-inner {
        position: absolute;
        width: 40px;
        height: 37px;
        top: 952px;
        left: 200px;
        background-color: #2a2f45;
        border-radius: 15px;
    }
    .dark-img {
        position: absolute;
        width: 40px;
        height: 40px;
        top: 950px;
        left: 200px;
    }
    .light-img {
        position: absolute;
        width: 40px;
        height: 40px;
        top: 950px;
        left: 155px;
    }
    .mode-label {
        position: absolute;
        top: 950px;
        left: 50px;
        font-size: 15px;
        color: #00a9e0;
    }
    </style>
""", unsafe_allow_html=True)

# --- Convert image to base64 for embedding ---
def img_to_base64(img):
    from io import BytesIO
    buf = BytesIO()
    img.save(buf, format="PNG")
    return base64.b64encode(buf.getvalue()).decode()

# --- HTML layout using your original positions ---
st.markdown(f"""
    <div class="container">

        <div class="title-bar"></div>
        <div class="sidebar"></div>
        <img src="data:image/png;base64,{img_to_base64(logo)}" class="logo-img" />
        <div class="stephenson-text">Stephenson</div>
        <div class="title-text">Upper Tank Farm (UTF)</div>
        <div class="line1"></div>

        <button class="menu-btn" style="top: 90px; left: 5px;">
            <div class="white-line" style="top: 0;"></div>
            <img src="data:image/png;base64,{img_to_base64(arrow_up)}" class="arrow-img" style="top: 20px;" />
            <div class="menu-text" style="top: 25px;">Upper Tank Farm</div>
        </button>

        <button class="menu-btn" style="top: 185px; left: 5px; background-color: #2a2f45;">
            <img src="data:image/png;base64,{img_to_base64(arrow_down)}" class="arrow-img" style="top: 22px;" />
            <div class="menu-text" style="top: 27px;">Lower Tank Farm</div>
        </button>

        <img src="data:image/png;base64,{img_to_base64(pfp)}" class="pfp-img" />
        <div class="profile-name">FirstN LastN</div>
        <div class="line2"></div>

        <div class="oval"></div>
        <div class="oval-inner"></div>
        <img src="data:image/png;base64,{img_to_base64(dark_mode)}" class="dark-img" />
        <img src="data:image/png;base64,{img_to_base64(light_mode)}" class="light-img" />
        <div class="mode-label">Dark Mode</div>

    </div>
""", unsafe_allow_html=True)
