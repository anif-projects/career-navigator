import streamlit as st
import google.generativeai as genai
import logging
from PIL import Image
import base64
import os

# Configure logging
logging.basicConfig(level=logging.INFO)

# Constants
NUMBER_OF_MESSAGES_TO_DISPLAY = 20

# --- Retrieve and Validate API key ---
GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY", os.getenv("GEMINI_API_KEY"))
if not GEMINI_API_KEY:
    st.error("Please add your Google Gemini API key to the Streamlit secrets.toml file or environment variables.")
    st.stop()

# --- Configure Gemini API ---
try:
    genai.configure(api_key=GEMINI_API_KEY)
    GEMINI_MODEL_NAME = 'gemini-1.5-flash-latest'  # Use the appropriate model name
except Exception as e:
    st.error(f"Error configuring Gemini API: {str(e)}")
    st.stop()

# --- Helper Functions ---
def img_to_base64(image_path):
    """Convert image to base64."""
    try:
        if not os.path.exists(image_path):
            logging.error(f"Image file not found: {image_path}")
            return None
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except Exception as e:
        logging.error(f"Error converting image to base64: {str(e)}")
        return None


# --- AI Conversation Logic ---
def get_gemini_chat_session():
    """Gets or creates a Gemini chat session."""
    if 'gemini_chat_session' not in st.session_state:
        model = genai.GenerativeModel(GEMINI_MODEL_NAME)
        initial_message_content = f"""
        You are Streamly, a helpful AI assistant powered by the Google Gemini {GEMINI_MODEL_NAME} model.
        I can assist you with a wide range of topics, including generating code, answering questions, and providing information.
        I am particularly knowledgeable about the Streamlit library.
        How can I help you today?
        """
        st.session_state.gemini_chat_session = model.start_chat(history=[
            {'role': 'user', 'parts': [initial_message_content]},
            {'role': 'model', 'parts': ["Okay, I understand. I am ready to assist with your queries."]}
        ])
        logging.info("Initialized new Gemini chat session.")
    return st.session_state.gemini_chat_session


def on_chat_submit(chat_input):
    """Handle chat input submissions."""
    user_input = chat_input.strip()

    # Ensure history exists for display
    if 'history' not in st.session_state:
        st.session_state.history = []

    st.session_state.history.append({"role": "user", "content": user_input})

    # --- AI Interaction ---
    try:
        chat_session = get_gemini_chat_session()
        response = chat_session.send_message(user_input)

        # Get assistant's reply
        assistant_reply = response.text
        st.session_state.history.append({"role": "assistant", "content": assistant_reply})

    except Exception as e:
        logging.error(f"Error occurred during Gemini API call: {e}")
        st.error(f"An error occurred: {str(e)}")
        st.session_state.history.append(
            {"role": "assistant", "content": "Sorry, I'm having trouble connecting right now. Please try again later."})


def initialize_session_state():
    """Initialize session state variables."""
    if "history" not in st.session_state:
        st.session_state.history = []
    get_gemini_chat_session()


def chat_bot_ai():
    """Display the chat interface."""
    initialize_session_state()

    if not st.session_state.history:
        initial_bot_message = """
        Hello! I am your Career AI Assistant. I can help you explore career paths, skills, education, scholarships, and job opportunities.
        How can I assist you today?
        """

        st.session_state.history.append({"role": "assistant", "content": initial_bot_message})
        get_gemini_chat_session()

    # Custom CSS for glowing effect
    st.markdown(
        """
        <style>
        .cover-glow {
            width: 100%;
            height: auto;
            padding: 3px;
            box-shadow: 0 0 5px #330000, 0 0 10px #660000, 0 0 15px #990000, 0 0 20px #CC0000;
            position: relative;
            z-index: -1;
            border-radius: 45px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Main chat interface
    chat_input = st.chat_input("Ask me anything...")
    if chat_input:
        on_chat_submit(chat_input)

    # Display chat history
    for message in st.session_state.history[-NUMBER_OF_MESSAGES_TO_DISPLAY:]:
        role = message["role"]
        avatar_image = "imgs/avatar_streamly.png" if role == "assistant" else "imgs/stuser.png"
        with st.chat_message(role, avatar=avatar_image):
            st.write(message["content"])
