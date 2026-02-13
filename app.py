import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

# -----------------------
# Page Configuration
# -----------------------
st.set_page_config(
    page_title="My Portfolio",
    page_icon="🚀",
    layout="wide",
)

# -----------------------
# Sidebar
# -----------------------
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["Home", "About Me", "Skills", "Projects", "Contact"]
)

st.sidebar.divider()
st.sidebar.info("Built with ❤️ using Streamlit")

# -----------------------
# Home Page
# -----------------------
if page == "Home":
    st.title("🚀 My Streamlit Portfolio")
    st.subheader("Welcome to my interactive autobiography!")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("resource/Nillama_ID.png", caption="Profile Picture", use_container_width=True)

    with col2:
        st.write("""
        Hello! I'm an aspiring developer passionate about:
        - Data Science
        - Machine Learning
        - Web Development
        - AI Applications
        """)

        st.metric("Years Coding", "3", "+1 this year")
        st.metric("Projects Completed", "15", "+5 recent")

    st.divider()

    st.success("Thanks for visiting my portfolio!")

# -----------------------
# About Me
# -----------------------
elif page == "About Me":
    st.header("📖 About Me")

    with st.expander("Click to read my story"):
        st.write("""
        I started my journey in programming because I was curious
        about how technology works. Over time, I developed strong
        interests in AI, automation, and software engineering.
        """)

    birth_year = st.slider("Select my birth year", 1990, 2010, 2000)
    age = datetime.now().year - birth_year
    st.write(f"My calculated age is: {age}")

    st.progress(age / 50)

    st.divider()

    st.info("Fun Fact: I love building interactive applications!")

# -----------------------
# Skills
# -----------------------
elif page == "Skills":
    st.header("🛠️ My Skills")

    skills = {
        "Python": 90,
        "Machine Learning": 80,
        "Web Development": 75,
        "Data Analysis": 85
    }

    df = pd.DataFrame(
        list(skills.items()),
        columns=["Skill", "Proficiency"]
    )

    st.dataframe(df)

    st.bar_chart(df.set_index("Skill"))

    st.divider()

    selected_skills = st.multiselect(
        "Select skills you are interested in:",
        list(skills.keys())
    )

    if selected_skills:
        st.write("You selected:", selected_skills)

# -----------------------
# Projects
# -----------------------
elif page == "Projects":
    st.header("📂 My Projects")

    tab1, tab2, tab3 = st.tabs(["Project 1", "Project 2", "Analytics Demo"])

    with tab1:
        st.subheader("Machine Learning Model")
        st.write("A predictive model built using Scikit-learn.")
        st.code("model.fit(X_train, y_train)")

    with tab2:
        st.subheader("Web App")
        st.write("A Flask-based application.")
        st.code("app.run(debug=True)")

    with tab3:
        st.subheader("Data Visualization")

        chart_data = pd.DataFrame(
            np.random.randn(20, 3),
            columns=["A", "B", "C"]
        )

        st.line_chart(chart_data)
        st.area_chart(chart_data)

    st.divider()

    uploaded_file = st.file_uploader("Upload a file to analyze")

    if uploaded_file:
        st.success("File uploaded successfully!")

# -----------------------
# Contact Page
# -----------------------
elif page == "Contact":
    st.header("📬 Contact Me")

    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")

        submitted = st.form_submit_button("Send Message")

        if submitted:
            st.success("Message sent successfully!")
            st.balloons()
            st.toast("Thanks for reaching out!")

    st.divider()

    st.write("Download my resume below:")
    st.download_button(
        label="Download Resume",
        data="Sample Resume Content",
        file_name="resume.txt",
        mime="text/plain"
    )

    st.json({
        "email": "myemail@example.com",
        "linkedin": "linkedin.com/in/myprofile",
        "github": "github.com/myprofile"
    })
