from app_utility import *
import datetime


st.title("Get Details & Recommendations")

try:# st.session_state["selected_movieid"] and st.session_state["selected_movietitle"]:
    selected_movieid = st.session_state["selected_movieid"]
    selected_movietitle = st.session_state["selected_movietitle"]
    selected = True
except:
   #  selected_movieid = 19995
   #  selected_movietitle = "Avatar"
   selected = False

if selected:
   st.subheader(f"You Selected : {selected_movietitle}")
   coll, colr = st.columns([2, 5], gap='medium')
   with coll:
      # st.subheader(f"You Selected : {selected_movietitle}")
      st.image(fetch_poster(selected_movieid), width=130)
   with colr:
      moviedetails = fetch_moviedetails(selected_movieid)
      user_score = int(moviedetails['vote_average'] * 10)
      y, m, d = moviedetails['release_date'].split("-")
      ymd = datetime.datetime(int(y), int(m), int(d))
      mtype = moviedetails['genres'][0]['name']
      hr = moviedetails['runtime'] // 60
      mn = moviedetails['runtime'] - hr
      descr = moviedetails['overview']

      st.markdown(f"**{selected_movietitle}**")
      st.caption(f"{ymd.strftime('%b')} {ymd.strftime('%d')}, {ymd.strftime('%Y')} 🔸 {mtype} 🔸 {hr}H {mn}min")
      if user_score < 50:
         st.markdown(f"**User Score : :red[{user_score} %]**")
      else:
         st.markdown(f"**User Score : :green[{user_score} %]**")
      st.markdown(f"**Overview :** {descr}")

   st.subheader("Your Recommendations")
   movienames, posters = recommendation_for(selected_movietitle)
   col1, col2, col3, col4, col5 = st.columns(5)
   with col1:
      moviedetails = fetch_moviedetails(selected_movieid)
      # y, m, d = moviedetails['release_date'].split("-")
      # ymd = datetime.datetime(int(y), int(m), int(d))
      st.caption(f"{movienames[0]}")
      # st.caption(f"{ymd.strftime('%b')} {ymd.strftime('%d')}, {ymd.strftime('%Y')}")
      st.image(posters[0])
      if st.button(f"Select {movienames[0]}"):
         selected_movieid = moviesdf.iloc[moviesdf[ moviesdf['title']==movienames[0] ].index[0]].id
         selected_movietitle = movienames[0]
         st.session_state["selected_movieid"] = selected_movieid
         st.session_state["selected_movietitle"] = selected_movietitle
         nav_page("recommendations")
   with col2:
      moviedetails = fetch_moviedetails(selected_movieid)
      # y, m, d = moviedetails['release_date'].split("-")
      # ymd = datetime.datetime(int(y), int(m), int(d))
      st.caption(f"{movienames[1]}")
      # st.caption(f"{ymd.strftime('%b')} {ymd.strftime('%d')}, {ymd.strftime('%Y')}")
      st.image(posters[1])
      if st.button(f"Select {movienames[1]}"):
         selected_movieid = moviesdf.iloc[moviesdf[ moviesdf['title']==movienames[1] ].index[0]].id
         selected_movietitle = movienames[1]
         st.session_state["selected_movieid"] = selected_movieid
         st.session_state["selected_movietitle"] = selected_movietitle
         nav_page("recommendations")
   with col3:
      moviedetails = fetch_moviedetails(selected_movieid)
      # y, m, d = moviedetails['release_date'].split("-")
      # ymd = datetime.datetime(int(y), int(m), int(d))
      st.caption(f"{movienames[2]}")
      # st.caption(f"{ymd.strftime('%b')} {ymd.strftime('%d')}, {ymd.strftime('%Y')}")
      st.image(posters[2])
      if st.button(f"Select {movienames[2]}"):
         selected_movieid = moviesdf.iloc[moviesdf[ moviesdf['title']==movienames[2] ].index[0]].id
         selected_movietitle = movienames[2]
         st.session_state["selected_movieid"] = selected_movieid
         st.session_state["selected_movietitle"] = selected_movietitle
         nav_page("recommendations")
   with col4:
      moviedetails = fetch_moviedetails(selected_movieid)
      # y, m, d = moviedetails['release_date'].split("-")
      # ymd = datetime.datetime(int(y), int(m), int(d))
      st.caption(f"{movienames[3]}")
      # st.caption(f"{ymd.strftime('%b')} {ymd.strftime('%d')}, {ymd.strftime('%Y')}")
      st.image(posters[3])
      if st.button(f"Select {movienames[3]}"):
         selected_movieid = moviesdf.iloc[moviesdf[ moviesdf['title']==movienames[3] ].index[0]].id
         selected_movietitle = movienames[3]
         st.session_state["selected_movieid"] = selected_movieid
         st.session_state["selected_movietitle"] = selected_movietitle
         nav_page("recommendations")
   with col5:
      moviedetails = fetch_moviedetails(selected_movieid)
      # y, m, d = moviedetails['release_date'].split("-")
      # ymd = datetime.datetime(int(y), int(m), int(d))
      st.caption(f"{movienames[4]}")
      # st.caption(f"{ymd.strftime('%b')} {ymd.strftime('%d')}, {ymd.strftime('%Y')}")
      st.image(posters[4])
      if st.button(f"Select {movienames[4]}"):
         selected_movieid = moviesdf.iloc[moviesdf[ moviesdf['title']==movienames[4] ].index[0]].id
         selected_movietitle = movienames[4]
         st.session_state["selected_movieid"] = selected_movieid
         st.session_state["selected_movietitle"] = selected_movietitle
         nav_page("recommendations")
else:
   st.warning("Please Select A Movie First In The Home Page And Let Our System Fetch Details And Generate Recommendations For You", icon="⚠️")
