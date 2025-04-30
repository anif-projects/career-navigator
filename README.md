# 🚀 Career Navigator AI

**Career Navigator AI** is an intelligent, user-friendly dashboard built with **Streamlit** and powered by **Gemini AI**. It provides personalized career guidance for students at various educational stages — from SSC to Intermediate, Engineering, Agriculture, and beyond.

Whether you're looking for the right subjects, top scholarships, top schools/colleges, or jobs (private and government), Career Navigator AI acts as your smart career companion.

---

## 🎯 Features

- ✅ Career exploration by education level:
  - **SSC**, **Intermediate**, **Engineering**, **Agriculture**, and more
- 🎓 Explore:
  - Subjects
  - Scholarships
  - Top Schools/Colleges
  - Jobs (Private & Government)
- 🌐 Multilingual support *(optional)*
- 🤖 Gemini AI integration for smart recommendations
- 📊 Clean, intuitive Streamlit dashboard

---

## 📁 Project Structure

career-navigator-ai/
├── app.py                       # Main Streamlit dashboard
├── .streamlit/
│   └── config.toml              # Optional: Streamlit theming/settings
├── data/                        # CSV/JSON files with subjects, jobs, etc.
│   ├── ssc_subjects.json
│   ├── intermediate_jobs.csv
│   ├── engineering_scholarships.json
│   └── agriculture_colleges.csv
├── components/                  # Reusable dashboard sections
│   ├── subject_section.py
│   ├── scholarship_section.py
│   ├── colleges_section.py
│   └── jobs_section.py
├── utils/                       # Helper functions & integrations
│   ├── gemini_client.py         # Gemini API calls
│   ├── data_loader.py           # Load/transform data
│   └── translator.py            # Language support (if needed)
├── assets/
│   ├── images/                  # Logos, icons
│   └── styles.css               # Optional custom styling
├── requirements.txt             # Python dependencies
└── README.md                    # Project overview, setup, usage

---
## 🛠️ Built With
#### Python == 3.12.10
#### pandas
#### requests
#### python-dotenv
#### streamlit_option_menu
#### google-generativeai


---
## 🤖 Gemini AI Setup
#### 1. Get an API key from Google AI Studio.
#### 2. Set the API key as an environment variable and in secrets (.streamlit/secrets.toml)

```bash
export GEMINI_API_KEY="your-api-key"
```


---
## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/career-navigator-ai.git
cd career-navigator-ai
```

---
## 2. Create a Virtual Environment (optional but recommended)
If we use any IDE Tool, default Virtual Environment will be created
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```


---
## 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---
## 4. Run the streamlit app
```bash
streamlit run app.py
```

