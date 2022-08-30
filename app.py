from hashlib import new
import streamlit as st
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
row1_1, row1_2 = st.columns((0.4,0.4)) #instantiate row 1

with row1_1:
    st.image('images/cinnamo-hello.gif')

with row1_2:
    row1_2.title("Hi! I'm ViV, your personal matchmaker!")
    row1_2.subheader(
    """

        Not only do I match you with someone based on the preferences you set, I also consider the information you write in your bio! This is called my **“Vibes-Tingle”** which helps me to find the most suitable match for you.
        So go ahead and get started, and remember: *the more information you fill out in your bio, the stronger my Vibes-Tingle will set off in finding you a match!*

    """)
    row1_2.write('**Created by Norty Nakagawa! Connect with me on [github](https://github.com/yourpandaboy) and [linkedin](https://www.linkedin.com/in/norutado-nakagawa/)**')

# model info
with st.expander("See what's inside ViV!"):
    st.write("""
        This is for ViV's description
    """)
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

st.markdown("""<hr style="height:4px;border:none;color:#161F6D;background-color:#161F6D;" /> """, unsafe_allow_html=True)

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
if start_execution:
    gif_runner = st.image('images/wiggle.gif')
    result = user.predict_model()
    gif_runner.empty()
    if len(result) == 0:
        st.write('Sorry! Try again!')
    st.write(result)
    #AgGrid(result)

# filtered_df = matches_df[(matches_df['sex'] == d) &( matches_df['age'].between(a,b)) & (matches_df['status'] == c.lower())]
# st.write(filtered_df)


# mai profile = Simple is the best. Great food, drinks and people make my life fabulous. i like bar hopping, summer night, winter events, movie theatre's atmosphere, eat, drinks and sometimes cooking and board games
