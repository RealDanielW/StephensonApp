import streamlit as st
import base64
from PIL import Image
import os

st.set_page_config(layout="wide")

# Function to encode image to base64
def img_to_base64(image):
    with open(image, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# Paths (adjust if your images are in 'images/' folder)
img_folder = "images"
logo = os.path.join(img_folder, "StephensonLogo.png")
arrow_up = os.path.join(img_folder, "ArrowUp.png")
arrow_down = os.path.join(img_folder, "ArrowDown.png")
pfp = os.path.join(img_folder, "UserPFP.png")
dark_mode = os.path.join(img_folder, "DarkMode.png")
light_mode = os.path.join(img_folder, "LightMode.png")

# HTML + CSS layout
st.markdown(f"""
<style>
    .container {{
        background-color: #363c56;
        width: 100vw;
        height: 100vh;
        overflow: hidden;
        position: relative;
        font-family: sans-serif;
    }}
    .title-bar {{
        position: absolute;
        top: 0; left: 0;
        width: 100%;
        height: 80px;
        background-color: #242839;
        z-index: 1;
    }}
    .sidebar {{
        position: absolute;
        top: 0; left: 0;
        width: 280px;
        height: 100%;
        background-color: #2a2f45;
        z-index: 0;
    }}
    .logo-img {{
        position: absolute;
        top: 13px;
        left: 5px;
        width: 50px;
        height: 50px;
    }}
    .stephenson-text {{
        position: absolute;
        top: 12px;
        left: 70px;
        color: #00a9e0;
        font-size: 24px;
    }}
    .title-text {{
        position: absolute;
        top: 12px;
        left: 300px;
        color: #00a9e0;
        font-size: 26px;
        font-weight: bold;
    }}
    .line1 {{
        position: absolute;
        top: 79px;
        left: 17px;
        width: 243px;
        height: 3px;
        background-color: #242839;
        border-radius: 3px;
    }}
    .menu-btn {{
        position: absolute;
        width: 274px;
        height: 90px;
        background-color: #242839;
        border: none;
    }}
    .menu-btn:hover {{ background-color: #575969; }}
    .menu-btn:active {{ background-color: #131728; }}
    .white-line {{
        position: absolute;
        left: 0;
        width: 5px;
        height: 90px;
        background-color: #00a9e0;
    }}
    .arrow-img {{
        position: absolute;
        left: 20px;
        width: 40px;
        height: 40px;
    }}
    .menu-text {{
        position: absolute;
        left: 80px;
        color: #00a9e0;
        font-size: 18px;
        font-weight: bold;
    }}
    .pfp-img {{
        position: absolute;
        top: 880px;
        left: 20px;
        width: 40px;
        height: 40px;
    }}
    .profile-name {{
        position: absolute;
        top: 880px;
        left: 80px;
        color: #00a9e0;
        font-size: 18px;
    }}
    .mode-switcher {{
        position: absolute;
        top: 950px;
        left: 150px;
        width: 100px;
        height: 40px;
        background-color: #363c56;
        border-radius: 15px;
    }}
    .mode-switcher-inner {{
        position: absolute;
        top: 952px;
        left: 200px;
        width: 40px;
        height: 37px;
        background-color: #2a2f45;
        border-radius: 15px;
    }}
    .dark-img, .light-img {{
        position: absolute;
        width: 40px;
        height: 40px;
        top: 950px;
    }}
    .light-img {{ left: 155px; }}
    .dark-img {{ left: 200px; }}
    .mode-label {{
        position: absolute;
        top: 950px;
        left: 50px;
        color: #00a9e0;
        font-size: 15px;
    }}
</style>

<div class="container">
    <div class="title-bar"></div>
    <div class="sidebar"></div>
    <img src="data:image/png;base64,{img_to_base64(logo)}" class="logo-img" />
    <div class="stephenson-text">Stephenson</div>
    <div class="title-text">Upper Tank Farm (UTF)</div>
    <div class="line1"></div>

    <button class="menu-btn" style="top: 90px; left: 5px;">
        <div class="white-line"></div>
        <img src="data:image/png;base64,{img_to_base64(narrow_up)}" class="arrow-img" style="top: 20px;" />
        <div class="menu-text" style="top: 25px;">Upper Tank Farm</div>
    </button>

    <button class="menu-btn" style="top: 185px; left: 5px; background-color: #2a2f45;">
        <img src="data:image/png;base64,{img_to_base64(narrow_down)}" class="arrow-img" style="top: 22px;" />
        <div class="menu-text" style="top: 27px;">Lower Tank Farm</div>
    </button>

    <img src="data:image/png;base64,{img_to_base64(pfp)}" class="pfp-img" />
    <div class="profile-name">FirstN LastN</div>

    <div class="mode-switcher"></div>
    <div class="mode-switcher-inner"></div>
    <img src="data:image/png;base64,{img_to_base64(dark_mode)}" class="dark-img" />
    <img src="data:image/png;base64,{img_to_base64(light_mode)}" class="light-img" />
    <div class="mode-label">Dark Mode</div>
</div>
""", unsafe_allow_html=True)
