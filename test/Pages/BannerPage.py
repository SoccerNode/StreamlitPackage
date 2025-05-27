import streamlit as st

class Banner:
    def __init__(self,
                 default_img_url,
                 hover_img_url,
                 link_url,
                 title_text,
                 font_family,
                 font_size,
                 font_color,
                 text_shadow,
                 banner_height,
                 border_radius):

        self.banner_html = f"""
        <style>
        .banner-container {{
            position: relative;
            width: 100%;
            height: {banner_height};
            background-image: url('{default_img_url}');
            background-size: cover;
            background-position: center;
            transition: background-image 0.3s ease-in-out;
            border-radius: {border_radius};
            cursor: pointer;
        }}
        
        .banner-container:hover {{
            background-image: url('{hover_img_url}');
        }}
        
        .banner-text {{
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-family: {font_family};
            font-size: {font_size};
            color: {font_color};
            text-shadow: {text_shadow};
            text-align: center;
        }}
        </style>
        
        <a href="{link_url}" target="_blank">
            <div class="banner-container">
                <div class="banner-text">
                    {title_text}
                </div>
            </div>
        </a>
        """

        st.markdown(self.banner_html, unsafe_allow_html=True)

# 페이지 레이아웃 설정
st.set_page_config(layout="wide")

# ✅ 배너 설정 변수 정의
default_img_url = "https://www.shutterstock.com/image-vector/super-mario-classic-video-game-260nw-2375538295.jpg"
hover_img_url = "https://via.placeholder.com/1200x200.png?text=Hovered+Banner"
link_url = "https://example.com"

title_text = "Clickable Banner Title"
font_family = "Arial Black, sans-serif"
font_size = "48px"
font_color = "white"
text_shadow = "2px 2px 4px #000000"

banner_height = "280px"
border_radius = "12px"

banner = Banner(default_img_url, hover_img_url, link_url, title_text, font_family, font_size, font_color, text_shadow, banner_height, border_radius)
