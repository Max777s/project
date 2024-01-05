import streamlit as st
import base64

    
# ----- Page configs (tab title, favicon) -----
st.set_page_config(
    page_title="Oussama AMDOUNI Portfolio",
    page_icon="📊",
)


# ----- Left menu -----
with st.sidebar:
    st.image("eae_img.png", width=200)
    st.header("Introduction to Programming Languages for Data")
    st.write(" A quick blink on my first Github project")
    st.write("***Final Project - Dec 2023***")
    st.write("**Author:Oussama AMDOUNI")
    st.write("**Instructor:** [Enric Domingo](https://github.com/enricd)")


# ----- Top title -----
st.write(f"""<div style="text-align: center;"><h1 style="text-align: center;">👋 Hi! My name is Oussama AMDOUNI""", unsafe_allow_html=True)  # TODO: Add your name


# ----- Profile image file -----
profile_image_file_path = "9f95d665-a4ea-4286-834e-30aab3f4f89d.JPG"       # TODO: Upload your profile image to the same folder as this script and update this if it has a different name

with open(profile_image_file_path, "rb") as img_file:
    img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


# ----- Your Profile Image -----
st.write(f"""
<div style="display: flex; justify-content: center;">
    <img src="{img}" alt="Your Name" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
</div>
""", unsafe_allow_html=True)


# ----- Personal title or short description -----
current_role = 

st.write("""
- 👨‍💻 Currently working on my Master's project in Big Data & Analytics at EAE Business School.
- ✈️ Former Aviator with experience in Air Traffic & Resource Management.
- 🤖 Exploring the transition from Aviation to the IT field, focusing on areas I find interesting.
- ...
""")
"  

st.write(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""", unsafe_allow_html=True)

st.write("##")    #


# ----- About me section -----
st.subheader("st.subheader("Skills")

st.write("""
- Python
- Data Analysis
- Machine Learning
- ...
""")
")

# TODO: Modify and adapt the following lines to your info, you can add or remove some details if you want
st.write("""
st.subheader("Projects")

st.write("""
- 🚀 [Project Name 1](link_to_project1): Brief description.
- 🌐 [Project Name 2](link_to_project2): Brief description.
- ...
""")

st.subheader("Education")

st.write("""
- 📚 Master's in Big Data & Analytics, EAE Business School, Barcelona
- ✈️ Previous education or certifications
- ...
""")


- 📫 How to reach me: oussamamdouni@gmail.com 

- 🏠 Barcelona
""")

Linkedin  :https://www.linkedin.com/in/oussamaamdouni/ 
IG        :  That_av_dude 
