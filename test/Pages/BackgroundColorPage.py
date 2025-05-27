import streamlit as st

# 페이지 배경색을 설정하는 사용자 정의 CSS
def set_background_color(color: str):
    st.markdown(f"""
        <style>
        .stApp {{
            background-color: {color};
        }}
        </style>
    """, unsafe_allow_html=True)

# 원하는 배경 색상 지정
set_background_color("#2F4F4F")  # 예: 베이지색

st.title("Custom Background Color Page")
st.write("이 페이지의 배경색은 커스텀 지정된 색상입니다.")
