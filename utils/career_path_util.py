import streamlit as st


def career_path_ai():
    st.markdown(f"""
            <h4 style="text-align: center;color:blue">Career Path: Courses and Opportunities</h4><br/>
            """, unsafe_allow_html=True)

    # The list of image URLs and their corresponding descriptions
    slides = [
        {"image": "imgs/career_path_imgs/PR_1.jpg",
         "description": "Secondary Graduation Courses"},
        {"image": "imgs/career_path_imgs/UG_1.jpg",
         "description": "Undergraduation Courses"}

    ]

    # Default slide index
    if 'index' not in st.session_state:
        st.session_state.index = 0

    # Navigation buttons at the top
    col1, col2, col3 = st.columns([1, 6, 1])  # Create three columns for previous, next buttons

    with col1:
        if st.button("Previous"):
            st.session_state.index = (st.session_state.index - 1) % len(slides)

    with col3:
        if st.button("Next"):
            st.session_state.index = (st.session_state.index + 1) % len(slides)


    # Get the current slide
    current_slide = slides[st.session_state.index]

    # Display description centered using HTML
    st.markdown(f"""
        <h5 style="text-align: center;color:purple">{current_slide['description']}</h5>
        """, unsafe_allow_html=True)

    # Show the current image and its description
    st.image(current_slide["image"], use_container_width=True)


