import streamlit as st
from streamlit_option_menu import option_menu

from utils.career_path_util import career_path_ai
from utils.postgraduate_education_util import display_postgraduate_education_content
from utils.primary_education_util import display_primary_education_content
from utils.secondary_education_util import display_secondary_education_content
from utils.chat_bot_util import chat_bot_ai
from utils.undergraduate_education_util import display_undergraduate_education_content

# Page setup
st.set_page_config(page_title="Career Navigator AI", layout="wide")

# Styling
st.markdown("""
    <style>
    section[data-testid="stSidebar"] > div {
        padding-bottom: 2rem;
    }

        [data-testid="stExpander"] {
        border: 2px solid #3498db;  /* Green color border */
        border-radius: 10px;
        padding: 10px;
        background-color: #f9f9f9;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
    }
    [data-testid="stExpander"] > div:first-child {
        font-weight: bold;
        color: #2c3e50;
        font-size: 18px;
    }


        .tab-content {
        margin-top: 20px;
    }

    .tab-header {
        font-size: 24px;
        font-weight: bold;
        color: #007bff;
        margin-bottom: 10px;
    }

    .tab-subheader {
        font-size: 18px;
        font-weight: 600;
        color: #28a745;
        margin-top: 10px;
    }

    .tab-description {
        font-size: 16px;
        color: #555;
        margin-bottom: 15px;
    }

    .tab-list {
        margin-left: 20px;
        font-size: 16px;
        color: #333;
    }


    </style>
""", unsafe_allow_html=True)

def display_footer():
    # Footer
    st.markdown("---")
    st.caption("QIS Engineering College Team | © 2025")

# Sidebar - Navigation Menu
with st.sidebar:
    selected_level = option_menu(
        "Career Navigator",
        ["Home", "Primary Education", "Secondary Education", "Undergraduate Education", "Postgraduate Education", "Career Path", "Chat Bot"],
        icons=["house", "book", "journal-bookmark", "mortarboard", "award", "rocket", "chat"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",
    )

# --- Main Page Content ---

# Home Page
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

# Primary Education Page
elif selected_level == "Primary Education":
    display_primary_education_content()
    display_footer()

# Secondary Education Page
elif selected_level == "Secondary Education":
    display_secondary_education_content()
    display_footer()

# Undergraduate Education Page
elif selected_level == "Undergraduate Education":
    display_undergraduate_education_content()
    display_footer()

# Postgraduate Education Page
elif selected_level == "Postgraduate Education":
    display_postgraduate_education_content()
    display_footer()

# Career Path
elif selected_level == "Career Path":
    career_path_ai()
    display_footer()

# Chat Bot
elif selected_level == "Chat Bot":
    st.markdown(
        """
        <h1 style='font-size: 24px;'>🤖 Career AI Bot - Explore Your Future</h1>
        """,
        unsafe_allow_html=True
    )
    chat_bot_ai()


