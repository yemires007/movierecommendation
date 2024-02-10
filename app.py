import streamlit as st
import pickle
import pandas as pd
import requests
from PIL import Image
from io import BytesIO

movies = pd.read_pickle('movies.pkl')
similarity = pd.read_pickle('similarity.pkl')


movies_list = movies['user_id'].values

# @st.cache  # Cache the dataset to avoid loading it on every run
# def load_data():
    # retpd.read_csv("s3_bucket_links_1.csv")


st.header('Movie Recommendation')
selectvalue = st.selectbox("select the user_id", movies_list)


def fetch_poster(movie_id):
    url = f"https://tezda-images.s3.amazonaws.com/{movie_id}"
    # url = "https://tezda-images.s3.amazonaws.com/shortVideos/".format(movie_id) 
    response = requests.get(url)
    # data = data.json()
    # half_part = movies['item_id'].values
    # response = url + half_part

    # return response
    # data = data.json()
    if response.status_code == 200:
        return response.content
    else:
        return None
    # poster_path = movies['item_id']
    # full_path = "https://tezda-images.s3.amazonaws.com/shortVideos/"+poster_path
    # return full_path

def recommend(movie):
    index = movies[movies['user_id'] == movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse = True, key=lambda vector:vector[1])
    recommend_m = []
    recommend_poster = []
    
    for i in distance[0:5]:
        movies_id = movies.iloc[i[0]].object_key
        recommend_m.append(movies.iloc[i[0]].item_id)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_m, recommend_poster



if st.button("Show recommendation"):
    movie_user_id, recommend_poster = recommend(selectvalue)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.text(movie_user_id[0])
        # st.image(movie_poster[0])
        st.video(recommend_poster[0])
    # with col2:
    #     st.text(movie_user_id[1])
    #     # st.image(movie_poster[1])
    #     st.video(recommend_poster[2])
    # with col3:
    #     st.text(movie_user_id[2])
    #     # st.image(movie_poster[2])
    #     # st.image(BytesIO(movie_poster[3]))
    #     st.video(recommend_poster[3])

