import datetime
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
col0, col1, col2, col3 = st.columns(4)
with col0:
    st.image(fetch_poster(selected_movieid), width=130)
with col2:
    moviedetails = fetch_moviedetails(selected_movieid)
    user_score = int(moviedetails['vote_average'] * 10)
    y, m, d = moviedetails['release_date'].split("-")
    ymd = datetime.datetime(int(y), int(m), int(d))
    # fmtdate = ymd.strftime()

    st.markdown(f"**{selected_movie}**")
    st.caption(f"{ymd.strftime('%b')} {ymd.strftime('%d')}, {ymd.strftime('%Y')}")
    if user_score < 50:
        st.markdown(f"**User Score : :red[{user_score} %]**")
    else:
        st.markdown(f"**User Score : :green[{user_score} %]**")


#recommendbutton
if st.button('Select & Generate'):
    #pushtosessionstate
    st.session_state["selected_movieid"] = selected_movieid
    st.session_state["selected_movietitle"] = selected_movie
    #redirecttonewpage
    nav_page("recommendations")
