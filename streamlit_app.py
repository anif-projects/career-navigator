import streamlit as st
from streamlit_option_menu import option_menu
from utils.auth_utils import login_user, register_user

from utils.career_path_util import career_path_ai
from utils.chat_bot_util import chat_bot_ai
from utils.postgraduate_education_util import display_postgraduate_education_content
from utils.primary_education_util import display_primary_education_content
from utils.secondary_education_util import display_secondary_education_content
from utils.undergraduate_education_util import display_undergraduate_education_content

# Page setup
st.set_page_config(page_title="Career Navigator AI", layout="wide")

# --- Styling ---
st.markdown("""
    <style>
    section[data-testid="stSidebar"] > div { padding-bottom: 2rem; }
    [data-testid="stExpander"] { border: 2px solid #3498db; border-radius: 10px; padding: 10px; background-color: #f9f9f9; box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);}
    [data-testid="stExpander"] > div:first-child { font-weight: bold; color: #2c3e50; font-size: 18px;}
    .tab-content { margin-top: 20px; }
    .tab-header { font-size: 24px; font-weight: bold; color: #007bff; margin-bottom: 10px; }
    .tab-subheader { font-size: 18px; font-weight: 600; color: #28a745; margin-top: 10px; }
    .tab-description { font-size: 16px; color: #555; margin-bottom: 15px; }
    .tab-list { margin-left: 20px; font-size: 16px; color: #333; }
    </style>
""", unsafe_allow_html=True)


# --- Footer ---
def display_footer():
    st.markdown("---")
    st.caption("QIS Engineering College Team | © 2025")


# --- Authentication Logic ---
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    st.title("🔐 Welcome to Career Navigator AI")

    tab1, tab2 = st.tabs(["🔑 Login", "📝 Register"])

    # --- Login Tab ---
    with tab1:
        username = st.text_input("Username", key="login_user")
        password = st.text_input("Password", type="password", key="login_pass")

        if st.button("Login"):
            success, msg = login_user(username, password)
            if success:
                st.session_state['logged_in'] = True
                st.session_state['username'] = username
                st.success(msg)
                st.experimental_rerun()
            else:
                st.error(msg)

    # --- Register Tab ---
    with tab2:
        new_username = st.text_input("Choose Username", key="reg_user")
        new_password = st.text_input("Choose Password", type="password", key="reg_pass")
        confirm_password = st.text_input("Confirm Password", type="password", key="reg_confirm")

        if st.button("Register"):
            if new_password != confirm_password:
                st.error("❌ Passwords do not match!")
            elif new_username.strip() == "" or new_password.strip() == "":
                st.error("❌ Username/Password cannot be empty!")
            else:
                success, msg = register_user(new_username, new_password)
                if success:
                    st.success(msg)
                    st.info("Now login with your new credentials.")
                else:
                    st.error(msg)

# --- Main App (after login) ---
else:
    with st.sidebar:
        st.success(f"👋 Welcome, {st.session_state['username']}")
        if st.button("Logout"):
            st.session_state['logged_in'] = False
            st.experimental_rerun()

        selected_level = option_menu(
            "Career Navigator",
            ["Home", "Primary Education", "Secondary Education", "Undergraduate Education", "Postgraduate Education",
             "Career Path", "Chat Bot"],
            icons=["house", "book", "journal-bookmark", "mortarboard", "award", "rocket", "chat"],
            menu_icon="cast",
            default_index=0,
            orientation="vertical",
        )

    # --- Page Routing ---
    if selected_level == "Home":
        st.title("🚀 Career Navigator")
        st.markdown("""
        Welcome to **Career Navigator AI**, your trusted companion for academic and career guidance! 🌟

        **Purpose:**  
        - Help students discover suitable **subjects** 📚  
        - Provide information about **scholarships** 🎓  
        - Explore top **colleges** 🏫  
        - Find relevant **job opportunities** 💼  
        - Ask the Chat Bot for personalized career advice, subjects, and job recommendations 💬

        <br>
        Our platform ensures personalized and updated information to guide you at every step of your career journey. 🚀
        """, unsafe_allow_html=True)
        display_footer()

    elif selected_level == "Primary Education":
        display_primary_education_content()
        display_footer()

    elif selected_level == "Secondary Education":
        display_secondary_education_content()
        display_footer()

    elif selected_level == "Undergraduate Education":
        display_undergraduate_education_content()
        display_footer()

    elif selected_level == "Postgraduate Education":
        display_postgraduate_education_content()
        display_footer()

    elif selected_level == "Career Path":
        career_path_ai()
        display_footer()

    elif selected_level == "Chat Bot":
        st.markdown("<h1 style='font-size: 24px;'>🤖 Career AI Bot - Explore Your Future</h1>", unsafe_allow_html=True)
        chat_bot_ai()
