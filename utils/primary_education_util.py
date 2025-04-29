import streamlit as st

def display_primary_education_content():
    st.title("📚 Primary Education")

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(
        ["Home", "Syllabus", "School List", "Scholarship", "Job Opportunities", "Career Opportunities"])

    # Home Tab Content
    # Home Tab Content
    with tab1:
        st.markdown('<div class="tab-header">🎓 SSC (Grade 10) Education</div>', unsafe_allow_html=True)

        st.markdown("""
           The **Secondary School Certificate (SSC)** is an important academic milestone for students.  
           It is usually awarded after completing **Grade 10** under various state education boards in India.

           **Key Highlights:**
           - Focuses on building strong academic foundations in core subjects.
           - Prepares students for higher secondary education (11th and 12th grades).
           - Helps in choosing future streams like Science, Commerce, or Arts.
           - Develops skills needed for entrance exams and career planning.
           """)

        st.markdown('<div class="tab-subheader">📚 Core Subjects Studied</div>', unsafe_allow_html=True)

        st.markdown("""
           - **Mathematics**  
           - **Science** (Physics, Chemistry, Biology)  
           - **Social Studies** (History, Geography, Civics, Economics)  
           - **First Language** (State language or Hindi)  
           - **Second Language** (English or other regional language)  
           - **Optional Subjects** (Computer Science, Physical Education, etc.)
           """)

        st.markdown('<div class="tab-subheader">🏆 Importance of SSC Grade 10</div>', unsafe_allow_html=True)

        st.markdown("""
           - Acts as a gateway to higher studies and specialized streams.
           - Forms the base for competitive exams and scholarship opportunities.
           - Builds academic confidence and future career direction.
           """)

        st.success("✨ Performing well in SSC Grade 10 opens many doors for future success!")

    # Syllabus Tab Content
    with tab2:
        st.markdown('<div class="tab-header">📚 Select Education Board Syllabus</div>', unsafe_allow_html=True)

        syllabus_option = st.radio(
            "Choose the syllabus to view:",
            ["CBSE Syllabus", "IGCSE Syllabus", "State Board Syllabus"]
        )

        if syllabus_option == "CBSE Syllabus":
            st.markdown('<div class="tab-subheader">Key Subjects in CBSE</div>', unsafe_allow_html=True)
            st.write(
                """
                - **Mathematics**: Algebra, Trigonometry, Calculus, and Geometry.
                - **Science**: Physics, Chemistry, and Biology.
                - **English**: Focuses on communication skills, comprehension, and writing.
                - **Hindi and Regional Languages**: Language proficiency and literature.
                """
            )

        elif syllabus_option == "IGCSE Syllabus":
            st.markdown('<div class="tab-subheader">Key Subjects in IGCSE</div>', unsafe_allow_html=True)
            st.write(
                """
                - **Mathematics**: Emphasis on problem-solving and application.
                - **Science**: Physics, Chemistry, Biology, and Environmental Science.
                - **English**: English Literature and Language.
                - **Foreign Languages**: Options include French, Spanish, German, etc.
                """
            )

        elif syllabus_option == "State Board Syllabus":
            st.markdown('<div class="tab-subheader">Key Subjects in State Board</div>', unsafe_allow_html=True)
            st.write(
                """
                - **Mathematics**: Similar to national standards, but with regional emphasis.
                - **Science**: Physics, Chemistry, and Biology with a local context.
                - **Social Science**: Focuses on regional history and geography.
                - **Regional Languages**: The primary focus is on the local language.
                """
            )
    import pandas as pd

    with tab3:
        with st.expander("🏫 CBSE Board Schools List", expanded=False):
            try:
                # Load the CSV file
                df_schools = pd.read_csv('data/ssc_cbse_schools_list.csv', sep=',', quotechar='"')

                if not df_schools.empty:
                    # Search box
                    search_query = st.text_input("🔍 Search for a school or location:")

                    # Filter the dataframe based on search query
                    if search_query:
                        filtered_df = df_schools[df_schools.apply(
                            lambda row: row.astype(str).str.contains(search_query, case=False, na=False).any(), axis=1)]
                    else:
                        filtered_df = df_schools

                    # Display the filtered dataframe
                    st.dataframe(filtered_df, use_container_width=True)
                else:
                    st.warning("No school data found in the CSV file.")

            except FileNotFoundError:
                st.error("School list CSV file not found. Please check the path: data/ssc_cbse_schools_list.csv")
            except Exception as e:
                st.error(f"An error occurred while loading the school list: {e}")

        with st.expander("🏫 State Board Schools List", expanded=False):
            try:
                # Load the CSV file
                df_schools = pd.read_csv('data/ssc_state_schools_list.csv', sep=',', quotechar='"')

                if not df_schools.empty:
                    # Search box with a unique key
                    search_query = st.text_input("🔍 Search for a school or location:", key="search_box_1")

                    # Filter the dataframe based on search query
                    if search_query:
                        filtered_df = df_schools[df_schools.apply(
                            lambda row: row.astype(str).str.contains(search_query, case=False, na=False).any(), axis=1)]
                    else:
                        filtered_df = df_schools

                    # Display the filtered dataframe
                    if filtered_df.empty:
                        st.warning("No schools match your search query.")
                    else:
                        st.dataframe(filtered_df, use_container_width=True)
                else:
                    st.warning("No school data found in the CSV file.")

            except FileNotFoundError:
                st.error("School list CSV file not found. Please check the path: data/ssc_state_schools_list.csv")
            except pd.errors.ParserError:
                st.error("Error while parsing the CSV file. Please ensure it is in the correct format.")
            except Exception as e:
                st.error(f"An error occurred while loading the school list: {e}")

    with tab4:
        st.markdown('<h5 style="text-align: center; color: #007bff;">🎓 SSC Scholarships</h5>', unsafe_allow_html=True)

        # Create two columns for Andhra Pradesh and Telangana
        col1, col2 = st.columns(2)

        # Andhra Pradesh Scholarships Card
        with col1:
            with st.container(border=True):
                st.markdown('<h5 style="color: #0dcaf0;">🏅 Andhra Pradesh Scholarships</h5>', unsafe_allow_html=True)

                st.markdown("""
                   - **Pre-Matric Scholarships for SC/ST/BC/Minorities**  
                     *Fee reimbursement + Monthly allowance.*

                   - **Jagananna Vidya Deevena (Fee Reimbursement Scheme)**  
                     *Full fee reimbursement for SSC pass students.*

                   - **NTR Vidyonnathi Scheme**  
                     *Coaching support for higher studies after SSC.*

                   - **National Means-cum-Merit Scholarship (NMMS)**  
                     *Scholarship for meritorious students from low-income families.*
                   """)

                st.markdown('<a href="https://apepass.cgg.gov.in/" target="_blank">🔗 Apply via AP ePASS Portal</a>',
                            unsafe_allow_html=True)

        # Telangana Scholarships Card
        with col2:
            with st.container(border=True):
                st.markdown('<h5 style="color: #0dcaf0;">🏅 Telangana Scholarships</h5>', unsafe_allow_html=True)

                st.markdown("""
                   - **Pre-Matric Scholarships for SC/ST/BC/EBC/Minorities**  
                     *Covers tuition + Monthly allowance.*

                   - **Telangana NMMS**  
                     *Merit-based scholarships for SSC students.*

                   - **Chief Minister’s Overseas Scholarship Scheme**  
                     *Support for higher studies (post SSC).*

                   """)

                st.markdown(
                    '<a href="https://telanganaepass.cgg.gov.in/" target="_blank">🔗 Apply via Telangana ePASS Portal</a>',
                    unsafe_allow_html=True)

    with tab5:
        st.markdown('<h4 style="text-align: center; color: #007bff;">🧑‍💼 Job Opportunities after SSC</h4>',
                    unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            st.markdown('<h5 style="color: teal;">🏛️ Government Job Opportunities</h3>', unsafe_allow_html=True)
            st.markdown("""
               - **Railway Group D Posts**  
                 *Track Maintainer, Helper, Assistant Pointsman*  
                 (Recruitment via RRB)

               - **Police Constable Jobs**  
                 *State Police departments (AP/Telangana) often recruit 10th pass candidates.*

               - **Defense Sector**  
                 *Indian Army - Soldier Tradesman, GD (General Duty)*  
                 *Indian Navy - Sailor Entry (MR - Matric Recruit)*  
                 *Indian Air Force - Group Y (Non-Technical trades)*

               - **Postal Department**  
                 *Gramin Dak Sevak (GDS)*  
                 *Postman, Mail Guard*

               - **State Government Jobs**  
                 *Various departmental jobs via APPSC / TSPSC.*  
               """)

        with col2:
            st.markdown('<h5 style="color: purple;">🏢 Private Sector Opportunities</h3>', unsafe_allow_html=True)
            st.markdown("""
               - **Apprenticeships**  
                 *Apprentice posts in Railways, PSUs, Private Factories.*

               - **Data Entry Operator / Office Assistant**  
                 *Back-office support jobs in companies.*

               - **Retail Jobs**  
                 *Sales Executive, Customer Service Representative.*

               - **Manufacturing / Factory Jobs**  
                 *Machine Operator, Assembly Line Worker.*

               - **Delivery Jobs**  
                 *Courier, Food Delivery (Swiggy, Zomato, Amazon Flex).*

               - **Call Center / BPO**  
                 *Domestic customer support roles.*
               """)

        st.success(
            "🔔 Tip: After SSC, pursuing ITI (Industrial Training Institutes) or Polytechnic courses can open even better job options!")

    with tab6:
        st.info("🚧 Content for Career Options is under construction.")


