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
# idx = moviesdf.iloc[moviesdf[ moviesdf['title']==selected_movie ].index[0]].id

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


# # SHOW SELECTED MOVIE
# st.write('You selected:', selected_movie)
# # col0, coll = st.columns(2)
# # with col0:
# st.image(fetch_poster(selected_movieid), width=130)
# st.markdown(f'[**`{selected_movie}`**](http://localhost:8501/new)')
# if st.button('Click'):
#     st.session_state["idx"] = idx
#     nav_page("new")

# # SHOW RECOMMENDED MOVIES
# if st.button('Recommend'):
#     st.write('Here are the recommendations for you : ')
#     movienames, posters = recommendation_for(selected_movie)

#     col1, col2, col3, col4, col5 = st.columns(5)
#     with col1:
#        st.caption(movienames[0])
#        st.image(posters[0])
#     #    if st.button("Next >"):
#     #     idx = moviesdf.iloc[moviesdf[ moviesdf['title']==movienames[0] ].index[0]].id
#     #     st.session_state["idx"] = idx
#         # nav_page("new")
#     #    if st.button('Select This'):
#     #     idx = moviesdf.iloc[moviesdf[ moviesdf['title']==movienames[0] ].index[0]].id
#     #     st.change_page("new")

#     with col2:
#        st.caption(movienames[1])
#        st.image(posters[1])

#     with col3:
#        st.caption(movienames[2])
#        st.image(posters[2])
    
#     with col4:
#        st.caption(movienames[3])
#        st.image(posters[3])

#     with col5:
#        st.caption(movienames[4])
#        st.image(posters[4])
