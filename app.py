from hashlib import new
import pandas as pd
import streamlit as st
from viv_front_util import ViV

st.title("ViV")
st.header("Vibe, Interact, Live!")
st.write("Using Machine Learning to Find the Top Dating Profiles for you")

"""### gif hello"""
file_ = open("images/cinnamo-hello.gif", "rb")
contents = file_.read()
data_url = base64.b64encode(contents).decode("utf-8")
file_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
    unsafe_allow_html=True,
)




with st.expander("See what's inside ViV!"):
    st.write("""
        This is for ViV's description
    """)



# Instantiating a new user DF
new_profile = pd.DataFrame(columns=['Name','Bio','Age','Status','Sex','Location']
                           )
# Asking for new profile data
name = st.text_input("Enter your name: ")
bio = st.text_input("Enter a Bio for yourself: ")
age = st.slider("What is your age?", 18, 70)
age = int(age)
status = st.selectbox(
'Choose your relationship status',
('--','Single', 'In a relationship', 'Married'))
sex = st.selectbox(
'Choose your gender',
('--','Male', 'Female', 'Others'))
location = st.text_input("Enter your location: ")

new_profile_dict = {'Name':[name],
                    'Bio':[bio],
                    'Age':[age],
                    'Status':[status],
                    'Sex':[sex],
                    'Location':[location]}

new_profile = new_profile_dict
st.write(pd.DataFrame(new_profile))

# Instantiating a new user preference DF to use as a filter later
preference_df = pd.DataFrame(columns= ['Age_start','Age_end','Status','Sex'])

st.header("Tell ViV your preference!")

a,b = st.slider(
     'Prefered ages',
     18, 70, (18, 25))

st.write('Your prefered ages:', a)
st.write('Your prefered ages:', b)

a= int(a)
b= int(b)

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

if st.button('ViV Me!'):

    result = user.predict_model()
    st.write(result)
# preference_df= a,b,c,d

# st.write(pd.DataFrame(preference_dict))

# matches_df = Matcher(bio).top_matches()
# matches_df['sex'] = matches_df['sex'].map({1:'Male',2:'Female'})
# st.write(matches_df)
# st.write(matches_df.shape)

# filtered_df = matches_df[(matches_df['sex'] == d) &( matches_df['age'].between(a,b)) & (matches_df['status'] == c.lower())]
# st.write(filtered_df)

# front_list=['Text_x','age','status','sex','location']
# front_df = filtered_df[front_list]
# front_df.sample(frac=1).reset_index(drop=True) #shuffle
# st.write(front_df)
# st.write(front_df.shape)
# st.write(front_df['Text_x'])
# st.button('finished')
# mai profile = Simple is the best. Great food, drinks and people make my life fabulous. i like bar hopping, summer night, winter events, movie theatre's atmosphere, eat, drinks and sometimes cooking and board games
