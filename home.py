# import streamlit as st
# import pandas as pd
# import pickle
# import requests
# from streamlit.components.v1 import html
from app_utility import *


### STREAMLIT APP STARTED............
###----------------------------------
st.set_page_config(
    page_title='MovieRecommenderApp',
    page_icon='🎬',
)

# TITLE
st.title("Movie Recommender App")

# MOVIE SELECT BOX
selected_movie = st.selectbox(
    "Which Movie Would You Like To Watch?",
    moviesdf['title'].values)

selected_movieid = moviesdf.iloc[moviesdf[ moviesdf['title']==selected_movie ].index[0]].id
# print(selected_movie, selected_movieid)

st.write('You Choosed:', selected_movie)
# col0, coll = st.columns(2)
# with col0:
st.image(fetch_poster(selected_movieid), width=130)

#recommendbutton
if st.button('Select & Generate'):
    #pushtosessionstate
    st.session_state["selected_movieid"] = selected_movieid
    st.session_state["selected_movietitle"] = selected_movie
    #redirecttonewpage
    nav_page("recommendations")
