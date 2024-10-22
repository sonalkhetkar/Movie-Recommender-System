import streamlit as st
import pickle
import pandas as pd


# def poster_fetch(movie_id):
#     response = request.get('https://upload.wikimedia.org/wikipedia/en/thumb/3/3b/{}.jpg/220px-{}.jpg'.formate(title_x))
#     data = response.json
#     return data['']

def recommend(movie):
      movie_index = movies[movies['title_x']==movie].index[0]
      distances = similarity[movie_index]
      movies_list = sorted(list(enumerate(distances)),reverse = True,key=lambda x:x[1])[1:6]
      recommended_movies = []
      for i in movies_list:
          movie_id = i[0]
          recommended_movies.append(movies.iloc[i[0]].title_x)
      return recommended_movies    

movies_dict = pickle.load(open('movies_dict (1).pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity (1).pkl','rb'))

st.title('Movie Recommendation System')

select_movie_name = st.selectbox(
'How would you like to be Connected ?',
movies['title_x'].values)

if st.button('Recommend'):
    
    recommendations = recommend(select_movie_name)
    for i in recommendations:
       st.write(i)

