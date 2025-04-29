import streamlit as st
import pandas as pd

def display_postgraduate_education_content():
    st.title("📚 Postgraduate Education")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        ["Home", "Streams", "College List", "Scholarship", "Job Opportunities", "Career Opportunities"])

    with tab1:
        display_home_tab()
    with tab2:
        display_streams_tab()
    with tab3:
        display_colleges_list_tab()
    with tab4:
        display_scholarships_tab()
    with tab5:
        display_job_opportunities_tab()
    with tab6:
        display_career_opportunities_tab()


def display_home_tab():
    st.markdown('<div class="tab-header">🎓 Postgraduation: Elevate Your Education</div>', unsafe_allow_html=True)

    st.markdown("""
        Postgraduation refers to education pursued after completing an undergraduate degree. 
        It allows you to **gain deeper knowledge**, **specialize in a field**, and often **engage in research**. 
        Postgraduate degrees include Master's degrees (M.A., M.Sc., M.Tech., MBA), Diplomas, Doctoral programs (Ph.D.), and specialized Certificates. 

        Postgraduate education is crucial for career growth, academic development, and professional advancement.
    """)

    st.markdown('<div class="tab-subheader">🎯 Why Pursue Postgraduation?</div>', unsafe_allow_html=True)
    st.markdown("""
        - **Specialization:** Deepen your expertise in a specific field. E.g., pursue an M.Sc. in Data Science after a B.Sc. in Computer Science, or an MBA after a BBA.
        - **Career Advancement:** Many higher-level roles, especially in healthcare, academia, and research, require postgraduate qualifications.
        - **Better Earning Potential:** Advanced degrees often lead to higher salaries across industries like business, engineering, medicine, and IT.
        - **Academic Pursuit & Research:** Passionate about research? Ph.D. programs allow you to contribute original ideas to your field.
        - **Skill Enhancement:** Postgraduate studies refine technical, managerial, analytical, and critical thinking skills essential for complex roles.
    """)

    st.markdown('<div class="tab-subheader">🌍 Best Countries for Postgraduation</div>', unsafe_allow_html=True)
    st.markdown("""
        Your choice of country can shape your academic experience and career opportunities. Here are top destinations:

        **1. United States 🇺🇸**  
        - **Popular Programs:** MBA, M.Tech, M.Sc., M.A., Ph.D., Medical programs.  
        - **Why:** Home to Harvard, MIT, Stanford. Research-rich, diverse programs, strong industry ties (Silicon Valley, Wall Street), and flexible student visas (OPT, STEM extension).

        **2. United Kingdom 🇬🇧**  
        - **Popular Programs:** MBA, M.Sc., M.A., M.Tech, LL.M.  
        - **Why:** World-class universities like Oxford and Cambridge. 1-year Master's, scholarships, and a post-study work visa.

        **3. Canada 🇨🇦**  
        - **Popular Programs:** MBA, M.Sc., M.A., M.Eng, M.P.H., M.Ed.  
        - **Why:** High quality of life, affordable tuition, welcoming immigration policies, top universities (Toronto, UBC, McGill).

        **4. Australia 🇦🇺**  
        - **Popular Programs:** MBA, M.Tech, M.Sc., M.Ed, M.A., Medical programs.  
        - **Why:** Excellent universities (ANU, Melbourne), scholarships, multicultural environment, and strong post-study work options.

        **5. Germany 🇩🇪**  
        - **Popular Programs:** M.Sc. in Engineering, Computer Science, Environmental Science.  
        - **Why:** Low or no tuition fees, engineering excellence, and global internship/job opportunities.

        **6. Netherlands 🇳🇱**  
        - **Popular Programs:** M.Sc., MBA, M.Tech, Medical programs.  
        - **Why:** Innovative education, affordable living, English-taught programs, and strong post-graduation work opportunities.

        **7. Singapore 🇸🇬**  
        - **Popular Programs:** MBA, M.Sc., M.Tech, Master of Finance, M.Ed.  
        - **Why:** Top Asian universities (NUS, NTU), strategic location, strong finance and tech sectors, multicultural environment.
    """)

    st.markdown('<div class="tab-subheader">🏆 Benefits of Postgraduation</div>', unsafe_allow_html=True)
    st.markdown("""
        - **Enhanced Career Opportunities:** Access higher-level, managerial, and specialized roles.
        - **Higher Earning Potential:** Boost your salary prospects in competitive industries.
        - **Global Recognition:** Degrees from top universities are respected worldwide.
        - **Personal Growth:** Develop critical thinking, research, leadership, and time management skills.
        - **Professional Networking:** Connect with academics, industry leaders, and fellow students for future collaborations and career opportunities.
    """)

    st.info(
        "💡 Choosing the right postgraduate path depends on your academic interests, career aspirations, and future goals. Explore global options and find the best fit for you!")


def display_streams_tab():
    st.title("🎓 Explore Post-Graduation Streams")

    st.markdown("""
    **Post-graduation courses** are advanced studies you can pursue after completing your graduation (bachelor’s degree).
    These programs help you **specialize** in a field or gain **deeper knowledge** for better career prospects.
    """)

    # Selectbox for grouping different sections
    pg_section = st.selectbox(
        "Select Post-Graduation Stream Type",
        [
            "Academic Master's Degrees",
            "Professional Master's Degrees",
            "Medical & Health Sciences PG Courses",
            "Agricultural & Allied Sciences PG Courses",
            "Postgraduate Diplomas",
            "Research Degrees"
        ]
    )

    # Academic Master's Degrees Section
    if pg_section == "Academic Master's Degrees":
        st.header("📚 Academic Master's Degrees (Duration: 2 Years)")

        with st.expander("🔬 M.Sc (Master of Science)"):
            st.markdown("""
            **Duration**: 2 Years  
            **Focus Areas**: 
            - Physics, Chemistry, Biology, Mathematics
            - Biotechnology, Data Science, Environmental Science
            - Focus on **Research, Scientific Careers**, and **Higher Education**.
            → Ideal for careers in **Research, Teaching, Data Science, Biotechnology**.
            """)

        with st.expander("📖 M.A (Master of Arts)"):
            st.markdown("""
            **Duration**: 2 Years  
            **Focus Areas**:
            - History, Economics, Political Science, Psychology
            - Sociology, Literature, Education
            - Focus on **Academia, Cultural Understanding, Social Research**.
            → Ideal for careers in **Academia, Civil Services, Journalism, Counseling**.
            """)

        with st.expander("📊 M.Com (Master of Commerce)"):
            st.markdown("""
            **Duration**: 2 Years  
            **Focus Areas**:
            - Accounting, Finance, Business Management
            - Banking, International Business, Taxation
            - Focus on **Financial Analysis, Business Strategy**, and **Corporate Management**.
            → Ideal for careers in **Accounting, Financial Management, Banking**.
            """)

    # Professional Master's Degrees Section
    elif pg_section == "Professional Master's Degrees":
        st.header("🏢 Professional Master's Degrees (Duration: 2 Years)")

        with st.expander("🛠️ M.Tech / M.E (Master of Technology / Engineering)"):
            st.markdown("""
            **Duration**: 2 Years  
            **Focus Areas**:
            - Artificial Intelligence, Robotics, Data Science
            - Mechanical, Civil, and Computer Science Engineering
            - Focus on **Advanced Engineering**, **Tech Leadership**, and **Research & Development**.
            → Ideal for careers in **Engineering Research, Technical Leadership**, and **R&D**.
            """)

        with st.expander("💼 MBA (Master of Business Administration)"):
            st.markdown("""
            **Duration**: 2 Years  
            **Focus Areas**:
            - Business Strategy, Marketing, Human Resources
            - Finance, International Business, Entrepreneurship
            - Focus on **Leadership, Management**, and **Entrepreneurship**.
            → Ideal for careers in **Management, Corporate Leadership, Consulting**.
            """)

        with st.expander("💻 MCA (Master of Computer Applications)"):
            st.markdown("""
            **Duration**: 2 Years  
            **Focus Areas**:
            - Software Development, IT Management
            - Network Security, Database Management
            - Focus on **Software Engineering**, **Application Development**, and **IT Management**.
            → Ideal for careers in **Software Development**, **IT Project Management**, and **System Architecture**.
            """)

        with st.expander("⚖️ LLM (Master of Laws)"):
            st.markdown("""
            **Duration**: 2 Years  
            **Focus Areas**:
            - Criminal Law, Corporate Law, Constitutional Law
            - International Law, Intellectual Property, Taxation
            - Focus on **Specialized Legal Practice** and **Law Theory**.
            → Ideal for careers as **Lawyers**, **Legal Consultants**, and **Academicians**.
            """)

        with st.expander("🏛️ M.Arch (Master of Architecture)"):
            st.markdown("""
            **Duration**: 2 Years  
            **Focus Areas**:
            - Urban Planning, Landscape Architecture
            - Sustainable Design, Architectural Engineering
            - Focus on **Urban Development**, **Sustainability**, and **Design Innovation**.
            → Ideal for careers in **Architecture Firms**, **Urban Planning**, and **Sustainable Architecture**.
            """)

        with st.expander("🎨 M.Des (Master of Design)"):
            st.markdown("""
            **Duration**: 2 Years  
            **Focus Areas**:
            - Product Design, Graphic Design, Fashion Design
            - Interaction Design, User Experience (UX)
            - Focus on **Creative Innovation**, **Design Thinking**, and **User-Centered Design**.
            → Ideal for careers as **Designers**, **Creative Directors**, and **UX/UI Experts**.
            """)

    # Medical & Health Sciences PG Courses Section
    elif pg_section == "Medical & Health Sciences PG Courses":
        st.header("🏥 Medical & Health Sciences PG Courses")

        with st.expander("🩺 MD (Doctor of Medicine)"):
            st.markdown("""
            **Duration**: 3 Years  
            **Focus Areas**:
            - Pediatrics, Dermatology, Radiology
            - Psychiatry, Internal Medicine, Surgery
            - Focus on **Clinical Expertise** and **Medical Research**.
            → Ideal for **MBBS graduates** seeking to specialize in non-surgical medical fields.
            """)

        with st.expander("🛡️ MS (Master of Surgery)"):
            st.markdown("""
            **Duration**: 3 Years  
            **Focus Areas**:
            - General Surgery, Orthopedics, ENT, Neurosurgery
            - Surgical Techniques, Post-Surgery Care
            - Focus on **Surgical Expertise**, **Trauma Care**, and **Patient Management**.
            → Ideal for **MBBS graduates** focusing on surgical specializations.
            """)

        with st.expander("🦷 MDS (Master of Dental Surgery)"):
            st.markdown("""
            **Duration**: 3 Years  
            **Focus Areas**:
            - Orthodontics, Prosthodontics, Oral Surgery
            - Periodontics, Oral Pathology, Pediatric Dentistry
            - Focus on **Advanced Dental Practice** and **Surgical Techniques**.
            → Ideal for **BDS graduates** aiming for specialization in advanced dental care.
            """)

        with st.expander("🏃‍♂️ MPT (Master of Physiotherapy)"):
            st.markdown("""
            **Duration**: 2 Years  
            **Focus Areas**:
            - Orthopedic, Neurological, Sports Physiotherapy
            - Musculoskeletal Rehabilitation, Pediatric Physiotherapy
            - Focus on **Physical Rehabilitation** and **Therapeutic Practices**.
            → Ideal for careers in **Physiotherapy**, **Sports Injury Management**, and **Rehabilitation**.
            """)

    # Agricultural & Allied Sciences PG Courses Section
    elif pg_section == "Agricultural & Allied Sciences PG Courses":
        st.header("🌾 Agricultural & Allied Sciences PG Courses")

        with st.expander("🌱 M.Sc Agriculture"):
            st.markdown("""
            **Duration**: 2 Years  
            **Focus Areas**:
            - Agronomy, Horticulture, Plant Pathology
            - Soil Science, Agricultural Engineering
            - Focus on **Agricultural Research**, **Crop Management**, and **Sustainable Farming**.
            → Ideal for careers in **Agriculture Research**, **Farm Management**, and **Agri-Business**.
            """)

        with st.expander("🌳 M.Sc Forestry / Horticulture"):
            st.markdown("""
            **Duration**: 2 Years  
            **Focus Areas**:
            - Forest Management, Conservation, Sustainable Development
            - Tree Plantation, Ecological Studies
            - Focus on **Environmental Sustainability**, **Forest Conservation**, and **Agroforestry**.
            → Ideal for careers in **Environmental Conservation**, **Forest Research**, and **Landscape Design**.
            """)

    # Postgraduate Diplomas Section
    elif pg_section == "Postgraduate Diplomas":
        st.header("📄 Postgraduate Diplomas (Duration: 1–1.5 Years)")

        with st.expander("🏢 PGDM (Post Graduate Diploma in Management)"):
            st.markdown("""
            **Duration**: 1–1.5 Years  
            **Focus Areas**:
            - Business Management, Strategy, Leadership
            - Marketing, Human Resource Management, Operations
            - Focus on **Management Skills**, **Leadership**, and **Strategic Thinking**.
            → Ideal for those aiming for **Corporate Leadership** and **Business Consulting**.
            """)

        with st.expander("💻 PGDCA (Post Graduate Diploma in Computer Applications)"):
            st.markdown("""
            **Duration**: 1 Year  
            **Focus Areas**:
            - Software Applications, Programming, IT Systems
            - Database Management, Network Security
            - Focus on **Application Development** and **System Support**.
            → Ideal for careers in **IT Support**, **Software Development**, and **System Administration**.
            """)

    # Research Degrees Section
    elif pg_section == "Research Degrees":
        st.header("📚 Research Degrees")

        with st.expander("🧪 M.Phil (Master of Philosophy)"):
            st.markdown("""
            **Duration**: 1–2 Years  
            **Focus Areas**:
            - Research Methods, Subject-Specific Studies
            - Academic Writing, Thesis Preparation
            - Focus on **Research Development** and **Specialized Academic Expertise**.
            → Ideal for those seeking to **pursue research**, leading to Ph.D. or academic roles.
            """)

        with st.expander("🎓 Ph.D (Doctor of Philosophy)"):
            st.markdown("""
            **Duration**: 3–5 Years  
            **Focus Areas**:
            - In-depth Research, Dissertation Writing
            - Subject-Specific Research, Data Analysis, Academic Publishing
            - Focus on **Advanced Research**, **Innovation**, and **Knowledge Development**.
            → Ideal for careers in **Academia, Research Institutions**, and **Policy-Making**.
            """)


def display_colleges_list_tab():
    with st.expander("🏫 College List", expanded=True):
        try:
            # Load the CSV file
            df_colleges = pd.read_csv('data/postgraduate_college_list.csv', sep=',', quotechar='"')

            if not df_colleges.empty:
                # Search box
                search_query = st.text_input("🔍 Search for a college or location:")

                # Filter the dataframe based on search query
                if search_query:
                    filtered_df = df_colleges[df_colleges.apply(
                        lambda row: row.astype(str).str.contains(search_query, case=False, na=False).any(), axis=1)]
                else:
                    filtered_df = df_colleges

                # Display the filtered dataframe
                st.dataframe(filtered_df, use_container_width=True)
            else:
                st.warning("No college data found in the CSV file.")

        except FileNotFoundError:
            st.error("Collge list CSV file not found. Please check the path: data/postgraduate_college_list.csv")
        except Exception as e:
            st.error(f"An error occurred while loading the college list: {e}")


def display_scholarships_tab():
    st.markdown('<h5 style="text-align:center;color: #0d6efd;">🎓 Scholarships for Postgraduate Students</h5>', unsafe_allow_html=True)

    st.markdown('<h5 style="color: #0dcaf0;">🏛 University-Specific Scholarships</h5>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.info("🏆 Rhodes Scholarship - University of Oxford (UK)")
        st.markdown("""
        - Highly competitive and fully funded.
        """)

        st.info("🎓 Gates Cambridge Scholarship - University of Cambridge (UK)")
        st.markdown("""
        - Fully funded for international postgraduate students.
        """)

        st.info("🇨🇭 ETH Zurich Excellence Scholarship")
        st.markdown("""
        - For master's students at ETH Zurich (Switzerland).
        """)

    with col2:
        st.info("🎓 Knight-Hennessy Scholars - Stanford University (USA)")
        st.markdown("""
        - Fully funded graduate study at Stanford University (USA).
        """)

    st.divider()

    # International Scholarships
    st.markdown('<h5 style="color: #0dcaf0;">🌍 International Scholarships</h5>', unsafe_allow_html=True)

    col3, col4 = st.columns(2)

    with col3:
        st.info("🇬🇧 Chevening Scholarships (UK)")
        st.markdown("""
        - Fully funded for any master's degree at any UK university.
        """)

        st.info("🇬🇧 Commonwealth Scholarships (UK)")
        st.markdown("""
        - For students from Commonwealth countries.
        """)

        st.info("🇺🇸 Fulbright Program (USA)")
        st.markdown("""
        - For non-US students to pursue graduate studies in the US.
        """)

        st.info("🇩🇪 DAAD Scholarships (Germany)")
        st.markdown("""
        - Fully/partially funded master's and PhD programs for international students.
        """)

        st.info("🇪🇺 Erasmus Mundus Joint Master Degrees (EU)")
        st.markdown("""
        - Fully funded master's programs across European universities.
        """)

    with col4:
        st.info("🇦🇺 Australia Awards Scholarships")
        st.markdown("""
        - For students from developing countries to study in Australia.
        """)

        st.info("🇨🇭 Swiss Government Excellence Scholarships")
        st.markdown("""
        - For postgraduate researchers in any discipline.
        """)

        st.info("🇳🇿 New Zealand Scholarships")
        st.markdown("""
        - Fully funded opportunities for students from selected countries.
        """)

    st.divider()

    # Field-Specific Scholarships
    st.markdown('<h5 style="color: #0dcaf0;">🔬 Field-Specific Scholarships</h5>', unsafe_allow_html=True)


    col5, col6 = st.columns(2)

    with col5:
        st.info("🎓 AAUW Fellowships")
        st.markdown("""
        - For women pursuing graduate degrees in the US.
        """)

        st.info("🕊 Rotary Peace Fellowships")
        st.markdown("""
        - Master’s degrees in peace and conflict resolution.
        """)

    with col6:
        st.info("🌍 Joint Japan/World Bank Graduate Scholarship Program")
        st.markdown("""
        - For students from developing countries in development-related fields.
        """)

    st.success("Stay informed about eligibility criteria and apply on time! 🌟")


def display_job_opportunities_tab():
    st.markdown('<h4 style="text-align: center; color: #007bff;">🧑‍💼 Job Opportunities after Post Graduation</h4>',
                unsafe_allow_html=True)

    # Two columns for Government and Private Jobs
    col1, col2 = st.columns(2)

    with col1:
        # Government Jobs Section
        st.markdown('<h5 style="color: teal;">🏛️ Government Job Opportunities</h4>', unsafe_allow_html=True)
        st.markdown("""
        - **AI/ML Researcher (ISRO)**  
          *Develop AI solutions for space missions, satellite data processing, and research.*  
          **Industries**: Government (ISRO)  
          **Skills**: Python, TensorFlow, Deep Learning, Space Research

        - **Defence Research & Development Organisation (DRDO) Scientist**  
          *Work on research in AI, machine learning, robotics, and national security technology.*  
          **Industries**: Government (DRDO)  
          **Skills**: Robotics, AI, Research Methodologies, Defense Technology

        - **Public Sector Bank Jobs**  
          *Probationary Officer (PO), Specialist Officer (SO), Clerical Posts*  
          (Recruitment through exams like IBPS PO/Clerk)  
          **Industries**: Banking Sector  
          **Skills**: Banking, Finance, Communication, Customer Handling

        - **Teaching/Faculty Positions in Government Universities**  
          *Lecturer, Assistant Professor, Associate Professor*  
          (Eligibility through NET, SLET, or university-specific exams)  
          **Industries**: Education  
          **Skills**: Subject Expertise, Research, Teaching Methodologies

        - **Civil Services (IAS, IPS, IFS)**  
          *Join the Indian Administrative Service, Police Service, or Foreign Service.*  
          **Industries**: Government  
          **Skills**: Leadership, Governance, Public Administration

        - **NABARD Development Assistant**  
          *Assist in policy planning, project financing, and rural development.*  
          **Industries**: Banking, Agriculture  
          **Skills**: Rural Development, Banking, Policy Planning

        - **Indian Railway Management Services (IRMS)**  
          *Join the Indian Railways in management and technical roles.*  
          **Industries**: Government (Indian Railways)  
          **Skills**: Engineering, Management, Transport Planning

        - **Health Sector Jobs in Government Hospitals**  
          *Medical Officer, Public Health Specialist, Lab Technician*  
          **Industries**: Healthcare (Government Hospitals)  
          **Skills**: Medical Sciences, Public Health

        - **Government Research Labs (CSIR, DRDO)**  
          *Scientist, Researcher*  
          **Industries**: Government Research  
          **Skills**: Scientific Research, Data Analysis, Technology Development
        """)

    with col2:
        # Private Jobs Section
        st.markdown('<h5 style="color: purple;">🏢 Private Job Opportunities</h5>', unsafe_allow_html=True)
        st.markdown("""
        - **AI/ML Engineer**  
          *Design and develop machine learning models, deep learning systems, and AI applications.*  
          **Industries**: Tech, Healthcare, Finance, Autonomous Vehicles, Robotics  
          **Skills**: Python, TensorFlow, PyTorch, Data Structures, Algorithms, Statistical Modeling

        - **Data Scientist**  
          *Analyze complex data sets, design predictive models, and provide insights for decision-making.*  
          **Industries**: E-commerce, Healthcare, Finance, Marketing, Tech  
          **Skills**: Data Wrangling, Statistical Analysis, R/Python, Machine Learning, SQL

        - **AI Researcher/Scientist**  
          *Conduct advanced research, develop algorithms, and solve complex AI problems.*  
          **Industries**: Research Labs, Academic Institutions, Tech Companies  
          **Skills**: Deep Learning, Reinforcement Learning, Research Methodologies

        - **Robotics Engineer**  
          *Design and build robotic systems, including autonomous robots and RPA.*  
          **Industries**: Manufacturing, Healthcare, Aerospace, Consumer Electronics  
          **Skills**: Robotics, Control Systems, Programming (C++, Python), Sensors, Automation

        - **Big Data Engineer**  
          *Build and manage data architectures for large data volumes, including real-time systems.*  
          **Industries**: Finance, Telecommunications, E-commerce, Healthcare  
          **Skills**: Hadoop, Spark, NoSQL, Data Pipelines, Cloud Platforms

        - **Cloud Solutions Architect**  
          *Design and manage cloud architectures, integrating AI/ML solutions into cloud platforms.*  
          **Industries**: AWS, Azure, Google Cloud, Enterprise Companies, Startups  
          **Skills**: AWS/Azure/GCP, Kubernetes, Docker, Cloud Security, Infrastructure Management

        - **Cybersecurity Specialist**  
          *Protect technology systems from cyber threats, securing data and system integrity.*  
          **Industries**: Tech, Financial Institutions, Government, Healthcare  
          **Skills**: Encryption, Ethical Hacking, Security Protocols, Network Security
        """)

    st.success("Stay updated on job openings and skill requirements! 🌟")


def display_career_opportunities_tab():
    st.markdown('<h5 style="color: #0d6efd;">🎓 Career Opportunities After Post-Graduation (Master’s Degree)</h4>', unsafe_allow_html=True)

    st.markdown(""" 
    - **🧑‍🔬 M.Sc (Master of Science)**
      - Fields: Physics, Chemistry, Biology, Computer Science, Biotechnology, Microbiology, Data Science, etc.
      - **Career Opportunities:**
        - Research Scientist (laboratories, universities, private R&D companies)
        - Data Scientist / Analyst (tech companies, finance, healthcare)
        - University Lecturer / Professor (after qualifying UGC-NET)
        - Quality Control Analyst (chemical, pharmaceutical, biotech industries)
        - Environmental Consultant (environmental organizations, NGOs, government bodies)
        - Biotech Industry Professional (genetics, medical research)
        - Software Developer / Engineer (Computer Science graduates)
        - Government Research Jobs (ISRO, DRDO, BARC, CSIR)

    - **🎓 M.A (Master of Arts)**
      - Fields: English, Political Science, History, Sociology, Psychology, Journalism, Economics, etc.
      - **Career Opportunities:**
        - Civil Services (IAS, IPS, IFS) – After passing UPSC exams
        - Teacher / Lecturer (schools, colleges, after clearing UGC-NET)
        - Journalist / Content Writer (media houses, publications, digital media)
        - Social Worker / NGO Worker (community services, child welfare, health)
        - Psychologist / Counselor (clinics, hospitals, schools, corporate sector)
        - Policy Analyst (government think tanks, research organizations)
        - Public Relations Officer (PR firms, corporate communications, media)

    - **💼 M.Com (Master of Commerce)**
      - Fields: Accounting, Finance, Business Studies, Banking, Taxation, etc.
      - **Career Opportunities:**
        - Chartered Accountant (CA) – After completing CA certification
        - Financial Analyst (banks, financial institutions, investment firms)
        - Tax Consultant (working with firms or starting own practice)
        - Investment Banker (top financial firms, stock markets)
        - Corporate Governance Expert (large corporations)
        - Bank PO / Clerk (via IBPS/SBI exams)
        - Lecturer in Commerce (after qualifying for UGC-NET)

    - **📚 M.Lib (Master of Library Science)**
      - Field: Library and Information Science
      - **Career Opportunities:**
        - Librarian (schools, universities, public libraries)
        - Digital Information Manager (digital libraries, archives)
        - Archivist (preserving historical records)
        - Information Systems Manager (large organizations)
        - Knowledge Manager (corporate sectors, universities)
        - Research Librarian (research institutions)

    - **👨‍🏫 M.Ed (Master of Education)**
      - Field: Educational Studies, Curriculum Design, and Teaching Methods
      - **Career Opportunities:**
        - School Principal / Headmaster
        - Curriculum Developer
        - Education Consultant
        - Lecturer / Assistant Professor (education colleges, universities)
        - Corporate Trainer (professional skills)
        - Educational Psychologist (schools, counseling centers)

    - **📊 M.Stat (Master of Statistics)**
      - Field: Statistics, Probability, Data Analysis, Econometrics
      - **Career Opportunities:**
        - Statistician (government agencies, research firms)
        - Data Analyst / Data Scientist (tech, healthcare, retail, finance)
        - Market Research Analyst (consumer trends)
        - Quantitative Analyst (investment banks, hedge funds)
        - Actuary (insurance, finance)
        - Professor / Lecturer (after qualifying UGC-NET)

    - **🔢 M.Math (Master of Mathematics)**
      - Field: Pure Mathematics, Applied Mathematics, Computational Mathematics
      - **Career Opportunities:**
        - Mathematician (research, tech, finance)
        - Data Scientist (advanced analytics, machine learning, AI)
        - Quantitative Analyst (investment banks, stock markets)
        - Cryptographer (cybersecurity, tech firms)
        - Academician (Professor / Researcher in Mathematics)
        - Operations Research Analyst (optimization problems in industries)

    - **🎨 MFA (Master of Fine Arts)**
      - Field: Creative Arts (Painting, Sculpture, Photography, Animation)
      - **Career Opportunities:**
        - Professional Artist (galleries, exhibitions, studio work)
        - Art Curator (museums, galleries)
        - Graphic Designer (advertising, media, publishing)
        - Animator / Visual Effects Artist (film production, gaming industry)
        - Art Teacher / Professor (art schools, universities)
        - Creative Director (media, fashion, advertising agencies)

    - **🤝 MSW (Master of Social Work)**
      - Field: Social Welfare, Counseling, Social Services
      - **Career Opportunities:**
        - Social Worker (NGOs, welfare organizations, hospitals)
        - Counselor / Therapist (emotional and psychological support)
        - Human Rights Advocate (human rights organizations, government)
        - Policy Researcher (think tanks, government bodies)
        - Community Organizer (social change projects, local development)
        - Social Work Lecturer (social work colleges, universities)

    - **🏃 M.P.Ed (Master of Physical Education)**
      - Field: Physical Fitness, Sports Training, Kinesiology
      - **Career Opportunities:**
        - Sports Coach (training athletes or teams)
        - Physical Education Teacher (schools, colleges)
        - Fitness Trainer (personal training, gym instructor)
        - Sports Psychologist (helping athletes with mental well-being)
        - Sports Manager (organizing sports events, managing teams)
        - Rehabilitation Specialist (working with injured athletes)

    - **🔧 General Career Opportunities for Post-Graduates (Applicable to many courses)**
      - Higher Education – Pursue a Ph.D. or M.Phil for deeper academic research.
      - Government Jobs – Through exams like UPSC, SSC, and State PCS for administrative, research, and policy-making positions.
      - Corporate Jobs – In management, marketing, human resources, finance, data analysis, etc.
      - Entrepreneurship – Start your own business in consulting, content creation, design, healthcare, etc.
    """)