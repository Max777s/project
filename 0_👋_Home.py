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
profile_image_file_path = "profile.png"       # TODO: Upload your profile image to the same folder as this script and update this if it has a different name

with open(profile_image_file_path, "rb") as img_file:
    img = "data:image/png;base64," + base64.b64encode(img_file.read()).decode()


# ----- Your Profile Image -----
st.write(f"""
<div style="display: flex; justify-content: center;">
    <img src="{img}" alt="Your Name" width="300" height="300" style="border-radius: 50%; object-fit: cover; margin-top: 40px; margin-bottom: 40px;">
</div>
""", unsafe_allow_html=True)


# ----- Personal title or short description -----
current_role = "Current Role and/or Studies or Description"   # TODO: Change this

st.write(f"""<div style="text-align: center;"><h4><i>{current_role}</i></h4></div>""", unsafe_allow_html=True)

st.write("##")    # Adding some space


# ----- About me section -----
st.subheader("About Me")

# TODO: Modify and adapt the following lines to your info, you can add or remove some details if you want
st.write("""
- 🧑‍💻 I am a Master student Big Data & analytics at EAE Business school in Barcelona .

- 🛩️ prev: Aviator , Air Traffic & ressource management and a Consulatant

- ❤️ FSX enthusiast and learning what others can not do .

- 🤖 Switching from Aviation to IT field is a Big step but interesting , as i am interested in the things i don't understand.

- 🏂 DJ'ing , Playing Music , Running ( preparing for Marathon) , Crossfit , Bootcamps , Ice bathing , Travelling.

- 📫 How to reach me: oussamamdouni@gmail.com 

- 🏠 Barcelona
""")

Linkedin  :https://www.linkedin.com/in/oussamaamdouni/ 
IG        :  That_av_dude 
