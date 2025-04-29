import streamlit as st
import pandas as pd

def display_secondary_education_content():
    st.title("📚 Secondary Education")

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
    st.markdown('<div class="tab-header">🎓 Further Education After Grade 10</div>', unsafe_allow_html=True)

    st.markdown("""
            Explore the exciting pathways available after completing Grade 10. This section provides an overview of Intermediate, Diploma, and other valuable courses.
            """)

    st.markdown('<div class="tab-subheader">🏫 Intermediate (Grades 11 & 12)</div>', unsafe_allow_html=True)
    st.markdown("""
            The traditional academic route, preparing you for undergraduate studies. Choose a stream based on your interests:

            - **Science:** Physics, Chemistry, Mathematics, Biology. Leads to Engineering, Medicine, and research.
            - **Commerce:** Accountancy, Business Studies, Economics. Opens doors to finance and management.
            - **Arts/Humanities:** History, Political Science, Literature. Suitable for social sciences and humanities careers.
            """)

    st.markdown('<div class="tab-subheader">🛠️ Diploma Courses</div>', unsafe_allow_html=True)
    st.markdown("""
            Skill-based programs offering specialized training for specific industries. Typically shorter than degrees and focused on job readiness.

            **Popular Areas:** Engineering, Technology, Healthcare, Hospitality, Design, Commerce.

            - **Engineering Diplomas:** Mechanical, Civil, Electrical, Electronics.
            - **Design Diplomas:** Fashion Design, Interior Design, Graphic Design.
            - **Hotel Management Diploma:** Prepares you for a career in hospitality and hotel management.
            - **Healthcare Diplomas:** Lab Technician, Nursing, Radiology.
            """)

    st.markdown('<div class="tab-subheader">⚙️ ITI (Industrial Training Institutes)</div>', unsafe_allow_html=True)
    st.markdown("""
            Vocational training in technical and non-technical trades, providing practical skills for direct employment.

            **Examples:** Electrician, Fitter, Welder, Mechanic, Computer Operator.
            """)

    st.markdown('<div class="tab-subheader">🎨 Other Skill-Based Courses & Certifications</div>', unsafe_allow_html=True)
    st.markdown("""
            Short-term courses and certifications to enhance specific skills and improve employability.

            **Examples:** Digital Marketing, Web Design, Graphic Design, Photography.
            """)

    st.markdown('<div class="tab-subheader">📚 Specialized Courses</div>', unsafe_allow_html=True)
    st.markdown("""
            Explore specialized courses that offer unique skills and knowledge for a successful career:

            - **Polytechnic Courses:** Technical courses leading to jobs in various fields like Engineering, IT, etc.
            - **Paramedical Courses:** Like X-ray Technician, Lab Technician, and Medical Assistant.
            - **Animation and Multimedia Courses:** Focused on media production, animation, and graphics.
            - **Photography Courses:** Enhance your skills in photography and digital imaging.
            - **Beauty and Wellness Courses:** Training in cosmetology, skincare, hair styling, and wellness.
            - **Sports or Physical Education Courses:** Prepares you for careers in coaching, fitness training, and sports management.
            """)

    st.info(
        "💡 Choosing the right path depends on your interests and career goals. Explore each section for more details!")

def display_streams_tab():
    st.title("🎓 Choose Your Stream After 10th")

    # Selectbox for grouping different sections
    section = st.selectbox(
        "Select Stream Type",
        ["Intermediate Streams", "Diploma Streams", "Hotel Management Stream"]
    )

    # Intermediate Streams Section
    if section == "Intermediate Streams":
        st.header("📚 Intermediate Streams")

        with st.expander("🧪 Science Stream"):
            st.markdown("""
            **Main Combinations:**
            - **MPC** (Maths, Physics, Chemistry)  
              → Good for **Engineering, Architecture, Navy, Defense, Data Science** careers.

            - **BiPC** (Biology, Physics, Chemistry)  
              → Good for **Medicine, Pharmacy, Agriculture, Veterinary, Nursing** careers.

            - **PCMB** (Physics, Chemistry, Maths, Biology)  
              → **Keeps both Engineering and Medical options open.**

            **Extra Options in Science:**
            - Computer Science (instead of Biology or an extra subject)
            - Electronics
            - Statistics
            """)

        with st.expander("📈 Commerce Stream"):
            st.markdown("""
            **Subjects Include:**
            - Accounts
            - Economics
            - Business Studies
            - Mathematics

            → Good for careers like **CA (Chartered Accountant), Banking, MBA, Stock Market, Company Secretary, Businessman**.

            **Extra Options in Commerce:**
            - Entrepreneurship
            - Information Practices (Computers)
            - Statistics
            """)

        with st.expander("🎨 Arts / Humanities Stream"):
            st.markdown("""
            **Subjects Include:**
            - History
            - Political Science
            - Psychology
            - Sociology
            - Geography
            - Economics

            → Good for careers like **Lawyer, Teacher, Journalist, Civil Services (IAS/IPS), Writer, Social Worker**.

            **Extra Options in Arts:**
            - Fine Arts
            - Literature (English, Hindi, Telugu, etc.)
            - Music
            - Home Science
            """)

        with st.expander("⚡ Diploma / Vocational Courses"):
            st.markdown("""
            **Examples:**
            - Polytechnic
            - Design
            - Hotel Management
            - Nursing Assistant

            ✅ These are skill-based programs and you can start working faster after completing them.
            """)

    # Hotel Management Stream Section
    elif section == "Hotel Management Stream":
        st.header("🍽️ Hotel Management Stream")

        with st.expander("Diploma in Hotel Management"):
            st.markdown("""
            **Course Duration:** 1 to 2 years  
            **Focus Areas:**  
            - Hotel Operations  
            - Food and Beverage Management  
            - Front Office Operations  
            - Housekeeping Management  
            - Event Management  

            **Career Opportunities:**  
            - Hotel Manager  
            - Event Planner  
            - Front Desk Supervisor  
            - Restaurant Manager  
            - Housekeeping Manager  
            - Hospitality Consultant
            """)

        with st.expander("Diploma in Food and Beverage Management"):
            st.markdown("""
            **Course Duration:** 1 to 2 years  
            **Focus Areas:**  
            - Food Production  
            - Food Safety and Hygiene  
            - Menu Planning  
            - Beverage Management  
            - Cost Control and Budgeting  

            **Career Opportunities:**  
            - Food and Beverage Manager  
            - Restaurant Supervisor  
            - Catering Manager  
            - Event Coordinator  
            - Banquet Manager
            """)

        with st.expander("Diploma in Front Office Operations"):
            st.markdown("""
            **Course Duration:** 1 year  
            **Focus Areas:**  
            - Reception Management  
            - Reservation Systems  
            - Guest Relations  
            - Communication Skills  
            - Billing and Payment Procedures  

            **Career Opportunities:**  
            - Front Desk Manager  
            - Guest Relations Officer  
            - Reservation Manager  
            - Concierge  
            - Hotel Receptionist
            """)

        with st.expander("Diploma in Housekeeping Management"):
            st.markdown("""
            **Course Duration:** 1 year  
            **Focus Areas:**  
            - Housekeeping Operations  
            - Cleaning and Sanitation  
            - Laundry Management  
            - Room and Property Management  
            - Cost Control  

            **Career Opportunities:**  
            - Housekeeping Supervisor  
            - Laundry Manager  
            - Room Attendant  
            - Housekeeping Manager
            """)

        with st.expander("Diploma in Event Management"):
            st.markdown("""
            **Course Duration:** 1 to 2 years  
            **Focus Areas:**  
            - Event Planning and Coordination  
            - Budgeting and Fundraising  
            - Vendor Management  
            - Marketing and Public Relations  
            - Event Logistics  

            **Career Opportunities:**  
            - Event Planner  
            - Wedding Planner  
            - Conference Coordinator  
            - Exhibition Manager  
            - Corporate Event Manager
            """)

    # Diploma Streams Section
    elif section == "Diploma Streams":
        st.header("🔧 Diploma Streams")

        # Using columns to organize diploma courses
        col1, col2 = st.columns(2)

        with col1:
            with st.expander("🛠️ Mechanical Engineering Diploma"):
                st.markdown("""
                **Duration**: 2 to 3 years  
                **Key Subjects**: Thermodynamics, Fluid Mechanics, Material Science, Manufacturing Processes, Machine Design  
                **Career Opportunities**: Mechanical Technician, Design Engineer, Production Supervisor, HVAC Engineer
                """)

            with st.expander("⚡ Electrical Engineering Diploma"):
                st.markdown("""
                **Duration**: 2 to 3 years  
                **Key Subjects**: Electrical Circuits, Electronics, Power Systems, Electrical Machines, Control Systems  
                **Career Opportunities**: Electrical Technician, Electrical Maintenance Engineer, Power System Engineer
                """)

            with st.expander("⚙️ Civil Engineering Diploma"):
                st.markdown("""
                **Duration**: 2 to 3 years  
                **Key Subjects**: Structural Analysis, Building Materials, Surveying, Construction Techniques, Environmental Engineering  
                **Career Opportunities**: Site Supervisor, Structural Designer, Civil Drafter, Construction Manager
                """)

            with st.expander("💻 Computer Engineering Diploma"):
                st.markdown("""
                **Duration**: 2 to 3 years  
                **Key Subjects**: Programming Languages (C, C++, Java), Data Structures, Operating Systems, Networking, Database Management  
                **Career Opportunities**: Software Developer, Network Administrator, IT Support Technician, Web Developer
                """)

        with col2:
            with st.expander("📱 Electronics Engineering Diploma"):
                st.markdown("""
                **Duration**: 2 to 3 years  
                **Key Subjects**: Digital Electronics, Analog Electronics, Microprocessors, Communication Systems, Signal Processing  
                **Career Opportunities**: Electronics Technician, Embedded Systems Engineer, Circuit Designer
                """)

            with st.expander("🚗 Automobile Engineering Diploma"):
                st.markdown("""
                **Duration**: 2 to 3 years  
                **Key Subjects**: Automotive Design, Engine Components, Vehicle Maintenance, Automobile Electronics, Manufacturing Processes  
                **Career Opportunities**: Automotive Technician, Service Engineer, Vehicle Maintenance Expert
                """)

            with st.expander("🛠️ Instrumentation Engineering Diploma"):
                st.markdown("""
                **Duration**: 2 to 3 years  
                **Key Subjects**: Process Control, Measuring Instruments, Industrial Automation, Control Systems, Sensors and Actuators  
                **Career Opportunities**: Instrumentation Engineer, Control Systems Technician, Automation Engineer
                """)

            with st.expander("⚗️ Chemical Engineering Diploma"):
                st.markdown("""
                **Duration**: 2 to 3 years  
                **Key Subjects**: Chemical Process Principles, Fluid Mechanics, Thermodynamics, Material Balance, Reactor Design  
                **Career Opportunities**: Chemical Process Technician, Plant Maintenance Engineer, Quality Control Technician
                """)

            with st.expander("⛏️ Mining Engineering Diploma"):
                st.markdown("""
                **Duration**: 2 to 3 years  
                **Key Subjects**: Mining Methods, Geology, Drilling and Blasting, Environmental Impact of Mining, Mine Safety  
                **Career Opportunities**: Mining Technician, Mining Safety Officer, Surveyor
                """)

            with st.expander("🌍 Environmental Engineering Diploma"):
                st.markdown("""
                **Duration**: 2 to 3 years  
                **Key Subjects**: Environmental Science, Water Treatment, Waste Management, Air Pollution Control, Environmental Legislation  
                **Career Opportunities**: Environmental Engineer, Waste Management Specialist, Pollution Control Analyst
                """)

    st.header("🔍 Quick Comparison Table")

    # Table for Stream vs Best For vs Examples
    stream_table = {
        "Stream": ["Science", "Commerce", "Arts"],
        "Best For": [
            "Doctor, Engineer, Scientist",
            "Business, Finance",
            "Law, Government, Teaching, Journalism"
        ],
        "Examples": [
            "MBBS, BTech, BSc",
            "BCom, CA, BBA",
            "BA, LLB, UPSC"
        ]
    }

    st.dataframe(stream_table, use_container_width=True)
    st.success("Explore each stream and choose your future path wisely! 🚀")


def display_colleges_list_tab():
    with st.expander("🏫 College List", expanded=True):
        try:
            # Load the CSV file
            df_colleges = pd.read_csv('data/secondary_college_list.csv', sep=',', quotechar='"')

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
            st.error("Collge list CSV file not found. Please check the path: data/secondary_college_list.csv")
        except Exception as e:
            st.error(f"An error occurred while loading the college list: {e}")


def display_scholarships_tab():
    st.markdown('<h5 style="text-align:center;color: #007bff;">🏅 Scholarships for Secondary Education</h5>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        # Andhra Pradesh Scholarships
        st.markdown('<h5 style="color: #0dcaf0;">🏅 Andhra Pradesh Scholarships</h5>', unsafe_allow_html=True)

        st.info("📚 Jnanabhumi Scholarships")
        st.markdown("""
        - Managed by the Andhra Pradesh government.
        - For **SC, ST, BC, EBC, Kapu, Minority, and Disabled** students.
        - Minimum **75% attendance** in the previous academic year required.
        """)

        st.info("🎒 Pre-Matric and Post-Matric Scholarships")
        st.markdown("""
        - Available for **SC, ST, BC, EBC, Minority, and Disabled** students.
        - Family income limits apply (e.g., ≤ ₹2.5 lakh for SC/ST).
        - Minimum **75% attendance** needed.
        """)

        st.info("📜 Veda Vyasa Scheme for Vedic Education")
        st.markdown("""
        - For **Brahmin students** aged **8–19 years**.
        - Must be pursuing full-time **Vedic courses**.
        - Students should be enrolled in recognized **Veda Patasalas**.
        """)

        st.info("🏆 Vidyadhan Scholarship")
        st.markdown("""
        - Offered by the **Sarojini Damodaran Foundation**.
        - Supports students who have completed **Class 10** and are pursuing further education.
        - Must have scored at least **80%** in the previous class.
        """)

    with col2:
        # Telangana Scholarships
        st.markdown('<h5 style="color: #0dcaf0;">🏅 Telangana Scholarships</h5>', unsafe_allow_html=True)

        st.info("📚 Telangana ePASS Scholarships")
        st.markdown("""
        - Pre-Matric and Post-Matric scholarships.
        - For **SC, ST, BC, EBC, Minority, and Disabled** students.
        - Minimum **75% attendance** required after Class 10.
        """)

        st.info("🌍 TS Ambedkar Overseas Vidya Nidhi")
        st.markdown("""
        - Supports **minority students** for higher education **abroad**.
        - Covers up to **₹20 lakhs**, including tuition, airfare, and visa charges.
        - Eligible countries: **USA, UK, Australia, Canada**, etc.
        """)

        st.info("🌏 Chief Minister's Overseas Scholarship Scheme for Minorities")
        st.markdown("""
        - Financial assistance for **overseas studies**.
        - For **minority students** meeting specific academic and income criteria.
        """)

    st.divider()

    # Additional Scholarships for Intermediate & Related Courses
    st.markdown('<h5 style="text-align:center;color: #0dcaf0;">📍 Scholarships for Intermediate & Related Courses</h5>', unsafe_allow_html=True)
    st.markdown('<h5 style="color: olive;">🏫 Intermediate (Grades 11 & 12) Scholarships</h5>', unsafe_allow_html=True)

    st.markdown("""
    - **Central Sector Scheme of Scholarships for College and University Students**
      - For **Class 12** students from **low-income families**.
      - Provides financial support for undergraduate education.

    - **Inspire Scholarship Scheme**
      - For **science students** who have scored 80% or higher in their **Class 12 Science stream**.
      - Provides support for pursuing higher education in natural and basic sciences.

    - **National Merit Scholarship Scheme**
      - For **top students** from **Class 12** based on merit.
      - Rewards students pursuing undergraduate education in various streams.
    """)

    st.markdown('<h5 style="color: olive;">🛠️ Diploma Courses Scholarships</h5>', unsafe_allow_html=True)
    st.markdown("""
    - **Dr APJ Abdul Kalam Technical University (AKTU) Scholarships**
      - For students enrolled in **technical diploma courses**.
      - Provides financial assistance for **diploma programs** in engineering and technology.

    - **National Apprenticeship Training Scheme (NATS) Scholarships**
      - For students undergoing **apprenticeship training** in technical and non-technical trades.
      - Provides monthly stipends and incentives.
    """)

    st.markdown('<h5 style="color: olive;">⚙️ ITI (Industrial Training Institutes) Scholarships</h5>', unsafe_allow_html=True)
    st.markdown("""
    - **National Scholarship for ITI Students**
      - For students pursuing **ITI courses** in various technical trades.
      - Offers financial support to reduce tuition fees and training costs.
    """)

    st.markdown('<h5 style="color: olive;">🎨 Skill-Based Course Scholarships</h5>', unsafe_allow_html=True)
    st.markdown("""
    - **National Skill Development Corporation (NSDC) Scholarships**
        - Supports students enrolled in skill development programs across sectors like healthcare, hospitality, and IT.
        - Offers funding and job placement opportunities.
    """)

    st.markdown("""
    - **Adobe India Creativity Scholarships**
        - For students pursuing creative fields such as Graphic Design, Animation, and Multimedia.
        - Provides financial aid and internship opportunities.
    """)

    st.success("Stay informed about eligibility criteria and apply on time! 🌟")


def display_job_opportunities():
    st.markdown('<h4 style="text-align: center; color: #007bff;">🧑‍💼 Job Opportunities after Secondary Education</h4>',
                unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown('<h5 style="color: teal;">🏛️ Government Job Opportunities</h5>', unsafe_allow_html=True)
        st.markdown("""
        - **Railway Group D Posts**
          *Track Maintainer, Helper, Assistant Pointsman*  
          (Recruitment via RRB)

        - **SSC CHSL Jobs**  
          *Lower Division Clerk (LDC), Postal Assistant, Data Entry Operator*  
          (Recruitment through SSC exams)

        - **State Government Jobs**  
          *Village Revenue Officer (VRO), Junior Assistant, Typist*  
          (Various State Boards recruit 12th pass students)

        - **Defense Sector**  
          *Indian Army Soldier GD, Indian Navy Sailor MR, Air Force Group Y*  
          (Physical and written tests after +2)

        - **Banking Jobs**  
          *Clerk posts after 12th*  
          (Limited banks like Cooperative/Rural Banks offer clerk jobs)

        - **Postal Department Jobs**  
          *Gramin Dak Sevak (GDS), Postman, Mail Guard*  
          (Recruitment through India Post)

        - **Health Sector Jobs**  
          *Lab Technician, Nursing Assistant, Radiology Technician*  
          (After Diplomas like DMLT, Nursing, Radiology)
        """)

    with col2:
        st.markdown('<h5 style="color: purple;">🏢 Private Job Opportunities</h5>', unsafe_allow_html=True)
        st.markdown("""
        - **BPO/Call Center Jobs**  
          *Customer Support Executive, Technical Support Representative*  
          (Voice and Non-Voice Processes)

        - **Data Entry Operator**  
          *Back Office Data Entry Clerk, Typist*  
          (Simple office typing jobs)

        - **Sales & Marketing Executive**  
          *Business Development Executive, Field Sales Executive*  
          (Work in Retail, Banking, FMCG sectors)

        - **Telecaller Jobs**  
          *Outbound/Inbound Calling Executive*  
          (Customer Relationship Management)

        - **Hospital Front Office Jobs**  
          *Receptionist, Patient Care Coordinator*  
          (Especially for BiPC background students)

        - **Retail Jobs**  
          *Showroom Sales Executive, Store Assistant*  
          (Opportunities in malls, showrooms)

        - **Hotel Management Jobs**  
          *Front Office Executive, Food & Beverage Staff, Housekeeping*  
          (After Diploma/Certificate in Hotel Management)

        - **Technician Jobs (ITI Courses)**  
          *Electrician, Fitter, Welder, Mechanic*  
          (Jobs after ITI certifications)
        """)

def display_career_opportunities_tab():
    st.markdown('<h5 style="color: #0d6efd;">🎯 Entrance Exams for MPC Students (Maths, Physics, Chemistry)</h4>',
                unsafe_allow_html=True)

    st.markdown("""
    - **🎓 Engineering & Technology**
      - JEE Main / JEE Advanced – Admission to NITs, IITs, top engineering colleges
      - BITSAT – BITS Pilani and campuses
      - VITEEE – Vellore Institute of Technology
      - SRMJEEE – SRM University
      - MET – Manipal University
      - State CETs – EAMCET (AP & TS), KCET (Karnataka), MHT CET (Maharashtra)

    - **🚢 Defense & Navy**
      - NDA (National Defence Academy) – For Army, Navy, Air Force
      - IMU CET – Indian Maritime University (Marine Engineering, Nautical Science)

    - **💼 Other Career Paths**
      - ISRO / DRDO Internships (after graduation) – Early preparation helps
      - IIIT-H UGEE / SPEC – IIIT Hyderabad special entry for research-focused students
    """)

    st.markdown('<h4 style="color: #0d6efd;">🔧 Entrance Exams for BiPC Students (Biology, Physics, Chemistry)</h4>',
                unsafe_allow_html=True)

    st.markdown("""
    - **🧬 Medical & Paramedical**
      - NEET-UG – For MBBS, BDS, BAMS, BHMS, BPT, B.Sc. Nursing, Veterinary, etc.
      - AIIMS / JIPMER – (Merged into NEET, but top colleges)

    - **🔬 Life Sciences & Research**
      - ICAR AIEEA – B.Sc. Agriculture, Horticulture, Forestry
      - CUET (UG) – Central Universities (B.Sc. Biotech, Microbiology)
      - IISER Aptitude Test – Research science programs (BiPC & MPC)

    - **🧑‍⚕️ Pharmacy & Allied Health**
      - GPAT (PG Entrance – plan ahead) – B.Pharm → M.Pharm
      - State CETs – Admission to B.Pharm and paramedical courses
    """)

    st.markdown('<h4 style="color: #0d6efd;">📍 Specific to AP & Telangana Students</h4>', unsafe_allow_html=True)

    st.markdown("""
    - **💡 For MPC Students**
      - EAMCET (AP EAMCET / TS EAMCET) – For B.Tech, B.Pharmacy, Agriculture (BiPC too)
        - Conducted by: JNTU Kakinada (AP), JNTU Hyderabad (TS)
      - POLYCET – Polytechnic/Diploma courses (technical jobs focus)
      - IIIT RGUKT (AP & TS) – 6-year integrated B.Tech (after 10th/Intermediate)
      - NDA – Indian Army, Navy, Air Force (PCM required for Navy/Air Force)

    - **🧬 For BiPC Students**
      - NEET-UG – MBBS, BDS, AYUSH, BPT, B.Sc. Nursing, Veterinary
      - EAMCET (AP & TS) – B.Sc. Agriculture, Horticulture, Fisheries, B.Pharm, Pharma.D
      - ICAR AIEEA (National) – B.Sc. Agriculture & Allied Sciences
      - CUET (UG) – Central Universities like University of Hyderabad (UoH)
    """)

    st.markdown('<h4 style="color: #0d6efd;">🏛️ Popular Diploma Options After 10th or Intermediate</h4>',
                unsafe_allow_html=True)

    st.markdown("""
    - **💊 1. Diploma in Pharmacy (D.Pharm)**
      - **Eligibility:** BiPC or MPC (10+2)
      - **Duration:** 2 years
      - **Entrance:** 
        - EAMCET (AP/TS) – For B.Pharm / Pharma.D after Intermediate
        - No entrance needed for many private colleges for D.Pharm
      - **After D.Pharm:** 
        - Join B.Pharm (Lateral Entry) – via ECET (AP ECET / TS ECET)
      - **Job Roles:** Pharmacist, Medical Store Assistant, Hospital Dispenser

    - **🖥️ 2. Diploma in Commerce / Accountancy / Office Management**
      - **Eligibility:** 10th or Intermediate (Commerce)
      - **Courses:**
        - Diploma in Financial Accounting
        - Diploma in Taxation / GST
        - Diploma in Office Automation
        - Diploma in Banking & Finance
      - **After Diploma:**
        - Option to join B.Com / BBA (lateral entry possible in some cases)
      - **Job Roles:** Junior Accountant, Office Assistant, Data Entry Operator, Clerk
    """)
