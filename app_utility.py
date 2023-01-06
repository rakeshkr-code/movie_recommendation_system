import streamlit as st
import pandas as pd
import pickle
import requests
from streamlit.components.v1 import html

API_KEY = '8d6a6e382c1cf4ed59d16b3a99ff2658'

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

def nav_page(page_name, timeout_secs=3):
    nav_script = """
        <script type="text/javascript">
            function attempt_nav_page(page_name, start_time, timeout_secs) {
                var links = window.parent.document.getElementsByTagName("a");
                for (var i = 0; i < links.length; i++) {
                    if (links[i].href.toLowerCase().endsWith("/" + page_name.toLowerCase())) {
                        links[i].click();
                        return;
                    }
                }
                var elasped = new Date() - start_time;
                if (elasped < timeout_secs * 1000) {
                    setTimeout(attempt_nav_page, 100, page_name, start_time, timeout_secs);
                } else {
                    alert("Unable to navigate to page '" + page_name + "' after " + timeout_secs + " second(s).");
                }
            }
            window.addEventListener("load", function() {
                attempt_nav_page("%s", new Date(), %d);
            });
        </script>
    """ % (page_name, timeout_secs)
    html(nav_script)