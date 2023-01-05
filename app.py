import streamlit as st
import pandas as pd
import pickle
import requests
import os

API_KEY = '8d6a6e382c1cf4ed59d16b3a99ff2658'
# basedir = os.path.abspath(os.path.dirname(__file__))
# MOVIESDICT_PATH = os.path.join(basedir, "../model")

### DUMP FILES OF OUR MODEL
### -----------------------
moviesdf = pd.DataFrame(pickle.load(open('model/moviesdict.pkl', 'rb')))
similarity_matrix = pickle.load(open('model/simimat.pkl', 'rb'))

### USEFUL FUNCTIONS
### -----------------
def fetch_poster(movie_id):
    responsedata = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}').json()
    completeposterpath = "https://image.tmdb.org/t/p/w500/" + responsedata['poster_path']
    return completeposterpath

def recommendation_for(selected_movie):
    movieindx = moviesdf[ moviesdf['title']==selected_movie ].index[0]
    distances = similarity_matrix[movieindx]
    recommandationlist = sorted(list(enumerate(distances)), reverse=True, key=lambda x : x[1])[1:6]

    recommended_movies = []
    movie_posters = []
    for rec_movie in recommandationlist:
        movie_id = rec_movie[0]
        recommended_movies.append(moviesdf.iloc[movie_id].title)
        movie_posters.append(fetch_poster(moviesdf.iloc[movie_id].id))
    return recommended_movies, movie_posters


### STREAMLIT APP STARTED............
###----------------------------------

# TITLE
st.title("Movie Recommender App")

# MOVIE SELECT BOX
selected_movie = st.selectbox(
    'Which Movie Would You Like To Watch?',
    moviesdf['title'].values)

# SHOW SELECTED MOVIE
st.write('You selected:', selected_movie)

# SHOW RECOMMENDED MOVIES
if st.button('Recommend'):
    st.write('Here are the recommendations for you : ')
    movienames, posters = recommendation_for(selected_movie)

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
       st.caption(movienames[0])
       st.image(posters[0])

    with col2:
       st.caption(movienames[1])
       st.image(posters[1])

    with col3:
       st.caption(movienames[2])
       st.image(posters[2])
    
    with col4:
       st.caption(movienames[3])
       st.image(posters[3])

    with col5:
       st.caption(movienames[4])
       st.image(posters[4])
