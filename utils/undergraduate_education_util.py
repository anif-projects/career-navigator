import streamlit as st
import pandas as pd

def display_undergraduate_education_content():
    st.title("📚 Undergraduate Education")

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
        display_job_opportunities()
    with tab6:
        display_career_opportunities_tab()

def display_home_tab():
    st.markdown('<div class="tab-header">🎓 Undergraduate Courses After Intermediate</div>', unsafe_allow_html=True)

    st.markdown("""
        Explore career options after completing Intermediate (Grade 12) based on your chosen stream:
    """)

    st.markdown('<div class="tab-subheader">🧮 After MPC (Maths, Physics, Chemistry)</div>', unsafe_allow_html=True)
    st.markdown("""
    - **Engineering (B.Tech / B.E.):** Professional courses in technology and innovation.
    - **B.Sc (Mathematics, Statistics, Physics):** Deep study of core science subjects.
    - **B.Arch (Architecture):** Designing buildings and physical structures.
    - **BCA (Bachelor of Computer Applications):** Career in software and IT.
    - **Merchant Navy Courses:** Careers at sea in navigation and engineering.
    - **NDA (National Defence Academy):** Military training for armed forces.
    """)

    st.markdown('<div class="tab-subheader">🧬 After BiPC (Biology, Physics, Chemistry)</div>', unsafe_allow_html=True)
    st.markdown("""
    - **MBBS (Medicine):** Become a licensed medical doctor.
    - **BDS (Dentistry):** Study of dental surgery and oral health.
    - **BAMS (Ayurvedic Medicine):** Traditional Indian medicine practice.
    - **BHMS (Homeopathy):** Alternative medicine using natural remedies.
    - **BPT (Physiotherapy):** Physical therapy and rehabilitation.
    - **B.Sc Nursing, Agriculture, Biotechnology, Microbiology:** Careers in healthcare, farming, and life sciences.
    - **Veterinary Science (BVSc):** Medical care for animals.
    """)

    st.markdown('<div class="tab-subheader">💹 After MEC (Maths, Economics, Commerce)</div>', unsafe_allow_html=True)
    st.markdown("""
    - **B.Com (General, Computers, Honors):** Commerce, accounting, and business fundamentals.
    - **BBA (Bachelor of Business Administration):** Management and business leadership.
    - **CA (Chartered Accountancy):** Professional accounting qualification.
    - **CS (Company Secretary):** Corporate law and governance expert.
    - **CMA (Cost and Management Accounting):** Financial planning and cost control.
    - **B.Sc (Statistics, Data Science):** Data analysis and statistical modeling.
    """)

    st.markdown('<div class="tab-subheader">🏛️ After CEC (Civics, Economics, Commerce)</div>', unsafe_allow_html=True)
    st.markdown("""
    - **B.A (Economics, Political Science, Public Administration):** Study of society, politics, and economy.
    - **BBA:** Business management and entrepreneurship.
    - **B.Com:** Focus on trade, finance, and business.
    - **LLB (5-Year Integrated Law Course):** Study to become a lawyer.
    - **Hotel Management:** Hospitality, hotel, and tourism industry careers.
    - **Travel and Tourism Management:** Careers in travel planning and tourism.
    """)

    st.markdown('<div class="tab-subheader">📜 After HEC (History, Economics, Civics)</div>', unsafe_allow_html=True)
    st.markdown("""
    - **B.A (History, Political Science, Sociology, Journalism):** Humanities and social sciences studies.
    - **BFA (Fine Arts):** Study of visual arts like painting and sculpture.
    - **BHM (Hotel Management):** Career in hospitality and hotel administration.
    - **Mass Communication and Journalism:** Media, reporting, and public communication.
    """)

    st.info("💡 Choose a course that matches your interests and career goals!")


def display_streams_tab():
    st.markdown('<div class="tab-header">🎓 Choose Your Stream After Secondary Education</div>', unsafe_allow_html=True)

    # Selectbox for grouping different sections
    section = st.selectbox(
        "Select Stream Type",
        ["Engineering Programs", "Medical Sciences", "Architecture & Design", "Agriculture Studies", "Marine & Navy Careers"]
    )

    # BTech Streams Section
    if section == "Engineering Programs":
        st.header("📚 BTech Streams")

        # Using columns to organize BTech courses
        col1, col2 = st.columns(2)

        with col1:
            with st.expander("💻 Computer Science and Engineering (CSE)"):
                st.markdown("""
                **What You Study**:  
                - Programming languages (C, Java, Python)  
                - Software Development, Databases  
                - Artificial Intelligence, Machine Learning  
                - Data Science, Cybersecurity

                **Career Opportunities**:  
                Software Developer, Data Scientist, Cybersecurity Engineer, Systems Architect
                """)

            with st.expander("📡 Electronics and Communication Engineering (ECE)"):
                st.markdown("""
                **What You Study**:  
                - Electronic Circuits, Signal Processing  
                - Mobile Networks, IoT Devices  
                - Wireless Communications

                **Career Opportunities**:  
                Electronics Engineer, Telecom Engineer, Embedded Systems Developer
                """)

            with st.expander("⚡ Electrical and Electronics Engineering (EEE)"):
                st.markdown("""
                **What You Study**:  
                - Power Systems, Electrical Machines  
                - Circuit Analysis, Control Systems

                **Career Opportunities**:  
                Electrical Engineer, Power Plant Engineer, Automation Engineer
                """)

            with st.expander("⚙️ Mechanical Engineering"):
                st.markdown("""
                **What You Study**:  
                - Machines, Engines, Manufacturing Technologies  
                - Robotics and Automation

                **Career Opportunities**:  
                Design Engineer, Automotive Engineer, Robotics Expert
                """)

            with st.expander("🏗️ Civil Engineering"):
                st.markdown("""
                **What You Study**:  
                - Building Construction, Structural Analysis  
                - Bridges, Roads, Urban Planning

                **Career Opportunities**:  
                Civil Engineer, Construction Manager, Urban Planner
                """)

            with st.expander("🌐 Information Technology (IT)"):
                st.markdown("""
                **What You Study**:  
                - Software Development, Web Technologies  
                - Networking, Cybersecurity Basics

                **Career Opportunities**:  
                Web Developer, IT Analyst, Network Administrator
                """)

        with col2:
            with st.expander("🤖 Artificial Intelligence & Machine Learning (AI & ML)"):
                st.markdown("""
                **What You Study**:  
                - Machine Learning Algorithms, Deep Learning  
                - Neural Networks, Data Analytics

                **Career Opportunities**:  
                AI Engineer, ML Specialist, Data Analyst
                """)

            with st.expander("📊 Data Science"):
                st.markdown("""
                **What You Study**:  
                - Big Data, Data Analysis, Statistics  
                - Python for Data Science, Data Visualization

                **Career Opportunities**:  
                Data Scientist, Business Analyst, Data Engineer
                """)

            with st.expander("✈️ Aeronautical Engineering"):
                st.markdown("""
                **What You Study**:  
                - Aircraft Design, Aerodynamics, Flight Mechanics

                **Career Opportunities**:  
                Aerospace Engineer, Aircraft Maintenance Engineer
                """)

            with st.expander("🧪 Chemical Engineering"):
                st.markdown("""
                **What You Study**:  
                - Chemical Plants, Petroleum Processing, Bioprocessing

                **Career Opportunities**:  
                Chemical Engineer, Process Engineer
                """)

            with st.expander("🧬 Biomedical Engineering"):
                st.markdown("""
                **What You Study**:  
                - Medical Devices, Bioelectronics, Tissue Engineering

                **Career Opportunities**:  
                Biomedical Engineer, Medical Equipment Specialist
                """)

            with st.expander("⚙️🤖 Mechatronics Engineering"):
                st.markdown("""
                **What You Study**:  
                - Robotics, Mechanical-Electrical Systems  
                - Embedded Systems, AI Hardware

                **Career Opportunities**:  
                Robotics Engineer, Automation Engineer
                """)

            with st.expander("🌍 Environmental Engineering"):
                st.markdown("""
                **What You Study**:  
                - Pollution Control, Waste Management, Sustainability

                **Career Opportunities**:  
                Environmental Consultant, Sustainability Expert
                """)

    if section == "Medical Sciences":
        st.header("🏥 MBBS Stream")

        with st.expander("🩺 MBBS (Bachelor of Medicine and Bachelor of Surgery)"):
            st.markdown("""
            **Duration**: 5.5 years (including 1-year internship)  
            **Eligibility**: 12th pass with PCB (Physics, Chemistry, Biology), entrance via NEET or equivalent.

            **Course Structure**:
            - **1st Year**: Anatomy, Physiology, Biochemistry, Histology, Embryology, Medical Physics
            - **2nd Year**: Pathology, Microbiology, Pharmacology, Forensic Medicine
            - **3rd Year**: General Medicine, Surgery, Pediatrics, ENT, Ophthalmology, Orthopedics
            - **4th Year**: Advanced Clinical subjects (Psychiatry, Dermatology, Radiology, Anesthesiology)
            - **5th Year**: Full-time Internship in hospitals, covering rotations across departments

            **Career Opportunities**:  
            Doctor (General Practitioner), Surgeon, Specialist Doctor (Pediatrics, Surgery, etc.), Hospital Administrator
            """)

    if section == "Architecture & Design":
        st.header("🏛️ Architect Stream")

        with st.expander("🏛️ B.Arch (Bachelor of Architecture)"):
            st.markdown("""
            **Duration**: 5 years (10 semesters)  
            **Eligibility**: 12th MPC (Maths, Physics), entrance via NATA or JEE Main Paper 2

            **Course Highlights**:
            - **Foundation Years**: Basics of Design, History of Architecture, Material Science, Environmental Studies, Drawing and CAD
            - **Advanced Design**: Electrical and HVAC systems, Structural Design, Urban Design, Climate-Responsive Design
            - **Specialization Years**: Green Architecture, Structural Systems, Interior and Landscape Design
            - **Professional Development**: Project Management, Building Codes, Final Thesis
            - **Final Year**: Major design project + Internship in Architecture firms

            **Career Opportunities**:  
            Architect, Urban Planner, Interior Designer, Landscape Architect
            """)

    if section == "Agriculture Studies":
        # --- Agriculture Stream ---
        st.header("🌾 B.Sc Agriculture Stream")

        with st.expander("🌿 B.Sc (Agriculture)"):
            st.markdown("""
            **Duration**: 4 years

            **Course Flow**:
            - **1st Year**: Agricultural Chemistry, Botany, Soil Science, Physics, Mathematics
            - **2nd Year**: Crop Production, Horticulture, Entomology, Plant Pathology, Farm Management
            - **3rd Year**: Plant Breeding, Agroforestry, Irrigation, Microbiology, Agricultural Engineering
            - **4th Year**: Agricultural Economics, Organic Farming, Agricultural Extension, Internship & Research Projects

            **Career Opportunities**:  
            Agricultural Officer, Agronomist, Farm Manager, Agricultural Scientist, Research Assistant
            """)

    if section == "Marine & Navy Careers":
        # --- Navy Stream ---
        st.header("⚓ Navy Stream")

        with st.expander("⚓ B.E./B.Tech in Marine Engineering"):
            st.markdown("""
            **Duration**: 4 years

            **What You Study**:
            - Ship Design and Construction
            - Marine Engines, Boilers, and Systems
            - Navigation and Communication Systems
            - Safety at Sea, Maritime Laws, Life-saving Techniques

            **Career Opportunities**:  
            Marine Engineer, Naval Architect, Ship Maintenance Engineer, Officer in Merchant Navy
            """)


    st.success("Explore each stream and choose your future path wisely! 🚀")


def display_colleges_list_tab():
    with st.expander("🏫 College List", expanded=True):
        try:
            # Load the CSV file
            df_colleges = pd.read_csv('data/undergraduate_college_list.csv', sep=',', quotechar='"')

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
            st.error("Collge list CSV file not found. Please check the path: data/undergraduate_college_list.csv")
        except Exception as e:
            st.error(f"An error occurred while loading the college list: {e}")


def display_scholarships_tab():
    st.markdown('<h5 style="color: #0d6efd;">🎓 Scholarships for Undergraduate Students in Andhra Pradesh & Telangana</h5>', unsafe_allow_html=True)

    # Create two columns for Andhra Pradesh and Telangana
    col1, col2 = st.columns(2)

    # Andhra Pradesh Scholarships Card
    with col1:
        with st.container(border=True):
            st.markdown('<h5 style="color: #0dcaf0;">🏅 Andhra Pradesh Scholarships</h5>', unsafe_allow_html=True)

            st.markdown("""
            - **Jnanabhumi Scholarships**  
              *For SC, ST, BC, EBC, Kapu, Minority, and Disabled students with 75% attendance.*

            - **Pre-Matric and Post-Matric Scholarships**  
              *Available for SC/ST/BC/EBC/Minority/Disabled students with income criteria.*

            - **Vidyadhan Scholarship**  
              *For students who completed Class 10 with at least 80% marks.*

            - **NTR Vidyonnathi Scheme**  
              *Free coaching for civil services for SC, ST, BC, Kapu, Brahmin, EBC, and Minority groups.*

            - **Veda Vyasa Scheme for Vedic Education**  
              *For Brahmin students aged 8–19 pursuing full-time Vedic courses.*
            """)

    # Telangana Scholarships Card
    with col2:
        with st.container(border=True):
            st.markdown('<h5 style="color: #0dcaf0;">🏅 Telangana Scholarships</h5>', unsafe_allow_html=True)

            st.markdown("""
            - **Telangana ePASS Scholarships**  
              *Pre-Matric and Post-Matric support for SC, ST, BC, EBC, Minority, and Disabled students.*

            - **TS Ambedkar Overseas Vidya Nidhi**  
              *Scholarship up to ₹20 lakhs for minority students pursuing higher education abroad.*

            - **Chief Minister's Overseas Scholarship Scheme for Minorities**  
              *Financial assistance for minority students for overseas studies.*
            """)

    st.success("🌟 Remember: Eligibility criteria and application deadlines vary each year. Stay updated!")


def display_job_opportunities():
    st.markdown(
        '<h5 style="text-align: center; color: #007bff;">🎯 Career Opportunities After Undergraduation (B.Tech, B.Sc, B.Com, B.A, BBA, etc.)</h3>',
        unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    # Private Sector Jobs
    with col2:
        st.markdown('<h5 style="color: purple;">🏢 Private Sector Jobs</h5>', unsafe_allow_html=True)

        st.markdown('<h6 style="color: #0d6efd;">🔧 Engineering (B.Tech, BE)</h5>', unsafe_allow_html=True)
        st.markdown("""
        - **Software Developer / IT Engineer**  
          *Opportunities in Hyderabad HITEC City, Gachibowli, Vizag IT SEZ.*
        - **Data Analyst / Data Scientist**  
          *Growing demand in tech and fintech startups.*
        - **Cloud Engineer / Cybersecurity Analyst**  
          *MNCs hiring in Hyderabad, Vizag, Vijayawada.*
        """)

        st.markdown('<h6 style="color: #0d6efd;">📊 Commerce (B.Com, BBA)</h5>', unsafe_allow_html=True)
        st.markdown("""
        - **Accountant / Auditor**  
          *Opportunities in corporates and startups.*
        - **Financial Analyst**  
          *Openings in investment firms, banks.*
        - **Marketing Executive / Sales Officer**  
          *Demand across FMCG, Retail, and Pharma companies.*
        """)

        st.markdown('<h6 style="color: #0d6efd;">🎨 Arts & Sciences (BA, B.Sc)</h5>', unsafe_allow_html=True)
        st.markdown("""
        - **Content Writer / Digital Marketer**  
          *Roles in EdTech, Media houses, and startups.*
        - **Research Assistant / Lab Technician**  
          *Openings in universities and biotech labs.*
        - **Graphic Designer / UI/UX Designer**  
          *Creative jobs with startups and agencies.*
        """)

    # Government Sector Jobs
    with col1:
        st.markdown('<h5 style="color: tule;">🏛️ Government Jobs</h5>', unsafe_allow_html=True)

        st.markdown('<h6 style="color: #0d6efd;">🔧 Engineering (B.Tech, BE)</h5>', unsafe_allow_html=True)
        st.markdown("""
        - **APPSC/TSPSC AE, AEE, Polytechnic Lecturer Jobs**  
          *Government Engineering roles.*
        - **Railways (RRB JE, SSE)**  
          *Junior Engineer opportunities.*
        - **Defense Services (Army Technical Entry, CDS)**  
          *Technical and engineering entries.*
        """)

        st.markdown('<h6 style="color: #0d6efd;">📊 Commerce (B.Com, BBA)</h5>', unsafe_allow_html=True)
        st.markdown("""
        - **Banking Jobs (IBPS PO/Clerk, SBI PO/Clerk)**  
          *Recruitments for finance graduates.*
        - **SSC CGL, State Tax Officers**  
          *Commercial tax and audit-related roles.*
        - **Municipal Administration, Revenue Department**  
          *Administrative posts through APPSC/TSPSC.*
        """)

        st.markdown('<h6 style="color: #0d6efd;">🎨 Arts & Sciences (BA, B.Sc)</h5>', unsafe_allow_html=True)
        st.markdown("""
        - **Group 1, Group 2 Services (Deputy Collector, DSP, etc.)**  
          *Prestigious administrative roles.*
        - **School Assistant, Junior Lecturer**  
          *Education department recruitments.*
        - **Police Constable, SI Exams**  
          *Law enforcement jobs through AP Police, Telangana Police.*
        """)

    st.success(
        "✅ Summary: Based on your graduation stream, there are wide opportunities in Andhra Pradesh and Telangana — both in the private and government sectors!")


def display_career_opportunities_tab():
    # Higher Education Section
    st.markdown('<h5 style="color: #0d6efd;">🎓 Higher Education Options</h5>', unsafe_allow_html=True)
    st.markdown("""
    - **M.Tech / ME**  
      *Through AP PGECET / TS PGECET / GATE.*
    - **MBA**  
      *Via AP ICET / TS ICET / CAT / MAT.*
    - **M.Sc / M.Com / M.A**  
      *Admissions through respective university entrance exams.*
    - **LLB (Law)**  
      *3-year or 5-year Law programs via AP LAWCET / TS LAWCET / CLAT (Common Law Admission Test).*
    - **Professional Courses**  
      *CA (Chartered Accountant), CS (Company Secretary), CMA (Cost Management Accounting) through ICAI/ICSI/ICMAI exams.*
    - **Competitive Exams**  
      *APPSC (Group 1, Group 2), TSPSC (Group 1, Group 2), Banking (IBPS PO, Clerk), Railways (RRB Secunderabad).*
    """)

    # Entrance Exams Section (More Expanded)
    st.markdown('<h4 style="color: #0d6efd;">🎯 Entrance Exams Based on Courses</h4>', unsafe_allow_html=True)

    # MPC Students
    st.markdown('<h5 style="color: #0d6efd;">📘 For MPC Students (Maths, Physics, Chemistry)</h5>', unsafe_allow_html=True)
    st.markdown("""
    - **EAMCET (AP/TS)** – Engineering admissions.
    - **BITSAT** – Admission to BITS Pilani, Hyderabad.
    - **VITEEE** – VIT University engineering entrance.
    - **SRMJEEE** – SRM Institute engineering admissions.
    - **GATE (Post Graduation)** – For M.Tech admissions after B.Tech.
    """)

    # BiPC Students
    st.markdown('<h5 style="color: #0d6efd;">🧪 For BiPC Students (Biology, Physics, Chemistry)</h5>', unsafe_allow_html=True)
    st.markdown("""
    - **NEET** – Medical entrance (MBBS, BDS, BAMS, BHMS).
    - **EAMCET (AP/TS)** – Agriculture, Veterinary Science.
    - **ICAR AIEEA** – Agriculture universities admissions.
    - **Pharmacy Entrance Tests (GPAT after B.Pharm)**.
    """)

    # CEC / MEC Students
    st.markdown('<h5 style="color: #0d6efd;">📚 For CEC / MEC Students (Commerce & Economics)</h5>', unsafe_allow_html=True)
    st.markdown("""
    - **CA Foundation** – Chartered Accountancy course.
    - **CMA Foundation** – Cost and Management Accounting.
    - **CS Foundation** – Company Secretary course.
    - **BBA Entrance Exams** – SET (Symbiosis), IPMAT (IIM Indore), NMIMS NPAT.
    """)

    # Arts & General Courses
    st.markdown('<h5 style="color: #0d6efd;">🎨 For Arts & General Degree Students</h5>', unsafe_allow_html=True)
    st.markdown("""
    - **CLAT / LSAT India** – Law admissions.
    - **CUET (UG/PG)** – Common University Entrance Test for central universities.
    - **TISSNET** – Tata Institute of Social Sciences admissions.
    - **Hotel Management (NCHMCT JEE)** – For careers in hospitality.
    """)

    # Entrepreneurship & Skill-Based Careers Section
    st.markdown('<h5 style="color: #0d6efd;">🚀 Entrepreneurship & Skill-Based Careers</h5>', unsafe_allow_html=True)
    st.markdown("""
    - **Startups** – Emerging startup hubs: Vizag FinTech Valley, Amaravati Innovation Hub, Hyderabad T-Hub.
    - **Skills in Demand** – Digital Marketing, Cloud Computing, Cybersecurity, Data Science, UI/UX Design.
    - **Agripreneurship** – Innovative opportunities in agriculture and food technology.
    - **Freelancing Platforms** – Freelance content writing, graphic designing, web development.
    """)

    # Footer
    st.markdown("---")
    st.caption("QIS Engineering College Team | © 2025")
