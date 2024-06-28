import streamlit as st
import pickle
import requests
import pandas as pd
import numpy as np

movies = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies['title'].values

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')
selected_movies_name = st.selectbox("Select a movie from the list", movies_list)


def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?'
                            'api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()

    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):

    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:13]

    recommended_movies = []
    recommended_movies_posters = []

    for i in movie_list:
        movie_id = movies.iloc[i[0]].movie_id

        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


if st.button('Recommend Movie'):
    names, posters = recommend(selected_movies_name)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.text(names[0])
        st.image(posters[0])

    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col1:
        st.text(names[3])
        st.image(posters[3])

    with col2:
        st.text(names[4])
        st.image(posters[4])

    with col3:
        st.text(names[5])
        st.image(posters[5])

    with col1:
        st.text(names[6])
        st.image(posters[6])

    with col2:
        st.text(names[7])
        st.image(posters[7])

    with col3:
        st.text(names[8])
        st.image(posters[8])

    with col1:
        st.text(names[9])
        st.image(posters[9])

    with col2:
        st.text(names[10])
        st.image(posters[10])

    with col3:
        st.text(names[11])
        st.image(posters[11])

