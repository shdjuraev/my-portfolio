import streamlit as st
from streamlit_lottie import st_lottie
import requests
import base64

st.set_page_config(page_title='My webpage', page_icon=":tada:", layout='wide')


def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def load_gif(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    return encoded


def load_image_base64(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


lottie_coding = load_lottie_url("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")

# -----HEADER SECTION-------

# Load and display profile photo at top of page
profile_img = load_image_base64("images/img.png")
phone_icon = load_image_base64("images/call-back.gif")
email_icon = load_image_base64("images/email (1).gif")
github_icon = load_image_base64("images/github.png")

with st.container():
    st.markdown(
        f"""
        <div style="display: flex; align-items: left; justify-content: left; gap: 40px; margin-top: 30px;">
            <div>
                <img src="data:image/jpeg;base64,{profile_img}" 
                     style="width: 180px; height: 180px; object-fit: cover; border-radius: 50%; border: 3px solid #555;" />
            </div>
            <div style="max-width: 600px;">
                <h1 style="margin-bottom: 0;">Hi, I am <span style="color: #4CAF50;">Shuhrat</span> 👋</h1>
                <h3 style="color: #888;">A Data Analyst from Uzbekistan</h3>
                <p style="font-size: 17px; line-height: 1.6;">
                    I love coding, teaching, doing research and collaborating.<br>
                    I am passionate about finding ways to use <b>Python</b> and <b>MS Excel</b> 
                    to be more efficient and effective in Business settings.
                </p>
                <!-- Contact Info Row -->
            <div style="margin-top: 25px; display: flex; gap: 40px; align-items: center;">
                <div style="display: flex; align-items: center; gap: 8px; white-space: nowrap; min-width: 110px;">
                    <img src="data:image/png;base64,{phone_icon}" width="22px" />
                    <span style="font-size: 15px;">+998 90 039 87 74</span>
                </div>
                <div style="display: flex; align-items: center; gap: 8px;">
                    <img src="data:image/png;base64,{email_icon}" width="22px" />
                    <span style="font-size: 15px;">shuhratdjuraev87@gmail.com</span>
                </div>
                <div style="display: flex; align-items: center; gap: 8px;">
                    <img src="data:image/png;base64,{github_icon}" width="22px" />
                    <a href="https://github.com/shdjuraev" target="_blank" style="font-size: 15px; color: #333; text-decoration: none;">
                        github.com/shdjuraev
                    </a>
                </div>
            </div>
        </div>
    </div>
    """,
        unsafe_allow_html=True
    )

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.markdown("<br>", unsafe_allow_html=True)  # Small line break
        st.write(
            """
            At work, I optimize and prepare university academic platform.
            - Aided in automating exams, registration, status tracking. 
            - Tracked student progress using [LMS/assessment tools] and provided actionable feedback.
            - Delivered beginner to advanced Python courses to students
            - Designed hands-on coding exercises and real-world mini-projects.
                        """
        )
        st.write("[YouTube Channel >](https://www.youtube.com/@ExcelbyShuhrat/videos)")

    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("My Projects")

    left_col, right_col = st.columns(2)
    with left_col:
        # Load the GIF
        gif_data = load_gif("images/loading bot.gif")

        # Inline GIF with text title
        st.markdown(
            f"""
            <div style="display: flex; align-items: center; gap: 10px;">
                <img src="data:image/gif;base64,{gif_data}" width="60px">
                <h3 style="margin: 0;">Telegram Bot: @tobbetu_bot</h3>
            </div>
            
            <div>
                <h4 style="font-size:24px; margin-top:10px;">📌 Purpose</h4>
            </div>
    
            """,
            unsafe_allow_html=True
        )

        st.write(
            """
            A Telegram bot designed to assist TOBB ETU Tashkent University 
            students by providing quick access to university-related info and services.\n
            **Tech Stack**
            - Python, Aiogram (async Telegram bot framework)
            - Telegram Bot API, FSM, dotenv\n\n
            if this sounds interesting to you
            """
        )
        st.markdown("[🚀 Try the bot on Telegram](https://t.me/tobbetu_bot)")

    with right_col:
        img_data = load_image_base64("images/tobbetu.jpg")
        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="data:image/jpeg;base64,{img_data}" 
                     style="width: 500px; border-radius: 12px; border: 1px solid #ccc;" />
            </div>
            """,
            unsafe_allow_html=True
        )

with st.container():
    st.write("---")
    left_col, right_col = st.columns(2)
    with left_col:
        # Load the GIF
        gif_data = load_gif("images/currency.gif")

        # Inline GIF with text title
        st.markdown(
            f"""
            <div style="display: flex; align-items: center; gap: 10px;">
                <img src="data:image/gif;base64,{gif_data}" width="60px">
                <h3 style="margin: 0;">Currency-Converter app</h3>
            </div>

            <div>
                <h4 style="font-size:24px; margin-top:10px;">📌 Purpose</h4>
            </div>

            """,
            unsafe_allow_html=True
        )

        st.write(
            """
            Developed a desktop-based Currency Converter application using Python, 
            focusing on simplicity and functionality for real-time currency conversion.\n
            **Tech Stack**
            - Python
            - Tkinter (likely, for GUI—will confirm after inspecting app.py)
            - Requests or an API (possibly used for exchange rates)
            - PyInstaller for packaging into standalone executables.\n\n
            
            if this sounds interesting to you
            """
        )
        st.markdown("[💾 Download EXE (GitHub)](https://github.com/shdjuraev/currency-converter1/raw/main/app.exe)")

    with right_col:
        img_data = load_image_base64("images/corrcon.png")
        st.markdown(
            f"""
            <div style="text-align: center;">
                <img src="data:image/jpeg;base64,{img_data}" 
                     style="width: 400px; border-radius: 12px; border: 1px solid #ccc;" />
            </div>
            """,
            unsafe_allow_html=True
        )

" "
