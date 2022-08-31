from hashlib import new
import streamlit as st
import time
#from st_aggrid import AgGrid
#config page
st.set_page_config(
    page_title='ViV: Vibe, Interact, Live!',
    page_icon='🐼',
    layout = 'wide')

import pandas as pd
import base64
from viv_front_util import ViV

# Remove the menu button and footer note from Streamlit
st.markdown(
    """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    </style>
    """,
    unsafe_allow_html=True)

#background image
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('images/panda-sweet-dark.jpg')


# Instantiating a new user DF
new_profile = pd.DataFrame(columns=['Name','Bio','Age','Status','Sex','Location']
                           )
pad, row1_1, row1_2 = st.columns((3,7,10)) #instantiate row 1

with row1_1:
    st.image('images/hello.gif', width= 360)

with row1_2:
    row1_2.subheader(
    """

        Hi! I'm ViV, your personal matchmaker!
        Not only do I match you with someone based on the preferences you set, I also consider the information you write in your bio! This is called my **“Vibes-Tingle”** which helps me to find the most suitable match for you.
        So go ahead and get started, and remember: *the more information you fill out in your bio, the stronger my Vibes-Tingle will set off in finding you a match!*

    """)
    row1_2.write('**Created by Norty Nakagawa and special thanks to Tony! Connect with me on [github](https://github.com/yourpandaboy) and [linkedin](https://www.linkedin.com/in/norutado-nakagawa/)**')

# model info
with st.expander("See more about ViV!"):
        st.markdown("**Introduction:**")
        st.write("""An unsupervised learning project trained from 60k OkCupid profiles from [Kaggle](https://www.kaggle.com/datasets/andrewmvd/okcupid-profiles). ViV matches user's bio by identifying which topics it belong.""")

        st.markdown("**Approach and Challenges:**")
        st.write("""Clustering or grouping different dating bio with random topics is a challeging yet fun task. After weeks of research, trials & errors, and insane amount of coffee ☕️ , Java-based MALLET gave the best result.""")
        st.write("""You can check out different approaches used and step by step procedure and training used in this repo [ViV-backend](https://github.com/yourpandaboy/ViV).""")
        st.write("""The model was able to group the profiles into 19 topics (see WordCloud below).""")

        st.markdown("**Model Output:**")
        st.write("""By converting the model to Python-based LDA and adding the new bio, ViV allocates user's bio within the 19 groups, then returns you profiles you are highly correlated within those groups (WordCloud topics).""")
        st.image('images/ViV_wordcloud2_8_24.png')

# ---------------------------
#        User Input
# ---------------------------

row2_1 , row2_2 = st.columns((1,1)) #instantiate row 2

with row2_1:
    name = st.text_input("Enter your name: ")
    age = st.number_input("What is your age?", 18, 120)
    age = int(age)
    sex = st.selectbox(
                    'Choose your gender',
                    ('--','Male', 'Female', 'Others'))
    status = st.selectbox(
                    'Choose your relationship status',
                    ('--','Single', 'In a relationship', 'Married'))


with row2_2:
    bio = st.text_area("Enter a bio for yourself (4 words minumum): ")
    tmp_arr = bio.split()

    location = st.text_input("Enter your location: ")



new_profile_dict = {'Name':[name],
                    'Bio':[bio],
                    'Age':[age],
                    'Status':[status],
                    'Sex':[sex],
                    'Location':[location]}

new_profile = new_profile_dict

# ---------------------------
#        User Preference
# ---------------------------

st.markdown("""<hr style="height:6px;border:none;color:#FFFFFF;background-color:#FFFFFF;" /> """, unsafe_allow_html=True)

# Instantiating a new user preference DF to use as a filter later
preference_df = pd.DataFrame(columns= ['Age_start','Age_end','Status','Sex'])
st.header("Tell ViV your preference!")


row3_1 , row3_2 = st.columns((1,1)) #instantiate row 3

with row3_1:
    a,b = st.slider(
            'Prefered ages',
            18, 100, (18, 25))

    a= int(a)
    b= int(b)

with row3_2:
    c = st.selectbox(
        'Your prefered status you want to meet',
        ('--','Single', 'In a relationship', 'Married'))

    d = st.selectbox(
        'Your prefered gender you want to meet',
        ('--','Male', 'Female', 'Others'))

preference_dict = {'Age_start': [a],
                   'Age_end':[b],
                   'Status':[c],
                   'Sex':[d]}

user = ViV(name,bio,age,status,a,b,d,c)

# ---------------------------
#        Run model
# ---------------------------


start_execution = st.button('ViV Me!')
if start_execution and len(tmp_arr) < 4:
    st.warning('Please enter at least 4 words.')
    st.stop()
if start_execution and len(tmp_arr) >= 4:
    with st.spinner("ViV's Vibe-Tingle Activated!"):
        time.sleep(10)
    #gif_runner = st.image('images/wiggle.gif')
    result = user.predict_model()
    #gif_runner.empty()
    if len(result) == 0:
        st.warning('Sorry! Try again or make sure to choose your preference. 😉')
        st.image('images/sleep.gif', width= 300)
    else:
        st.success('Here are your potential matches!')
        st.image('images/WG8T.gif', width= 250)
        st.table(result)

    #AgGrid(result)

# filtered_df = matches_df[(matches_df['sex'] == d) &( matches_df['age'].between(a,b)) & (matches_df['status'] == c.lower())]
# st.write(filtered_df)


# mai profile = Simple is the best. Great food, drinks and people make my life fabulous. i like bar hopping, summer night, winter events, movie theatre's atmosphere, eat, drinks and sometimes cooking and board games
