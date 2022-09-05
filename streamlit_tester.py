import streamlit as st
import pandas as pd

# st.write("My First Streamlit Web App")

# st.write("Hello")


sample = {"Profile":
                    ["hi! i am 27. i currently work full time as a chemist and am in full time grad school. i have 2 cute guenea pigs. i really want a dog. i love camping, going to the beach, bbqs, and hanging out with friends. i love trying new things.",
                     "i just moved to san francisco. so far i am loving the city, but could use a few suggestions on where to go and what to do. generally on weekends i try mix things up and check out different neighborhoods.",
                     "born and raised in san francisco. love to go out and try new things. like reading, going to shows, hanging out, and going to bars....",
                     "eva the meat cleaver is my roller derby name, if i were into roller derby.",
                     "i'm a san francisco native who loves the giants and good sense of humor. if you can make me laugh you get a huge + in my book."],
         "Age":
                    [20,21,22,23,24],
         "Location":
                    ["san francisco, california", "san francisco, california", "san francisco, california", "san francisco, california", "san francisco, california"],
         "Status":
                    ["Single", "Single", "Single", "Single", "Single"]
        }

df = pd.DataFrame(sample)

# if "Liked" not in st.session_state():
#     st.session_state["Liked"]

# df = pd.DataFrame(sample)
# #st.table(df.iloc[[0]])
# for index, row in df.iterrows():
#     col1,col2,col3 = st.columns([1,1,1])
#     #print(row['c1'], row['c2'])
#     st.table(df.iloc[[index]])
#     with col1:
#         st.button("Pass")
#     with col2:
#         st.button("Like")

if "Liked" not in st.session_state:
    st.session_state.liked = pd.DataFrame(columns=['Profile', 'Age', 'Location', 'Status'])


if "a_counter" not in st.session_state:
    st.session_state["a_counter"] = 0

st.write(st.session_state.a_counter)
st.write(st.session_state.liked)



start_button = st.button("See my matches!")
like_button = st.button("Like")
pass_button = st.button("Pass")
end_button = st.button("See my matches")
#pass_button, col2, like_button = st.columns([1,1,1])

#blank_df = pd.DataFrame(columns=['Profile', 'Age', 'Location', 'Status'])

if start_button:
    st.table(df.iloc[[0]])

if like_button:
    st.session_state.a_counter += 1
    ##blank_df.append(df.iloc[st.session_state.a_counter], ignore_index= True)
    st.session_state.liked = pd.concat([st.session_state.liked, df.iloc[[st.session_state.a_counter]]], axis=0)
    #st.session_state.mdf = pd.concat([st.session_state.mdf, df_new], axis=0)
    st.table(df.iloc[[st.session_state.a_counter]])


if pass_button:
    st.session_state.a_counter += 1
    st.table(df.iloc[[st.session_state.a_counter]])

if end_button:
    trial = st.button("Trial")

def like():
    #st.session_state.liked = pd.concat([st.session_state.liked, df.iloc[[0]]], axis=0)
    st.session_state.a_counter += 1
    st.table(df.iloc[[st.session_state.a_counter]])




def nope():
    st.table(df.iloc[[4]])


#st.button("Like", on_click= like)
#st.button("Pass", on_click= nope)
