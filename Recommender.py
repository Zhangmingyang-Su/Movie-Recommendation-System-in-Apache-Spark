# Recommend movie to users with id: 575, 232

# Recommend top 10 movies
userRecs = best_model.recommendForAllUsers(10)
display(userRecs.filter(userRecs.userId == 575))

user_recommendation = userRecs.to_koalas()
user_recommendation.head()

movies_koalas = movies_df.to_koalas()

# Build recommendation function
def movie_recommendation(user_recommendation, userId, movies_koalas):
  rec_movieId = []
  for item in user_recommendation.loc['userId' == userId][1]:
    rec_movieId.append(item[0])
  return movies_koalas.loc[movies_koalas.movieId.isin(rec_movieId)]

movie_recommendation(user_recommendation, 575, movies_koalas)
movie_recommendation(user_recommendation, 232, movies_koalas)


# Find the similar movies for movie with id: 463. 471
item_factors = best_model.itemFactors
movie_factors = item_factors.to_koalas()
movie_factors.head()

# Build similar movies function
def similar_movies(features, movieId):

  try: 
    target_id_feature = movie_factors.loc[movie_factors.id == movieId].features.to_numpy()[0]
  except:
    return 'There is no movie with id ' + str(movieId)

  similarities = []
  for feature in movie_factors['features'].to_numpy():
    similarity = np.dot(target_id_feature,feature)/(np.linalg.norm(target_id_feature) * np.linalg.norm(feature))
    similarities.append(similarity)
    
  ks_similarity = ks.DataFrame({'similarity' : similarities}, index = movie_factors.id.to_numpy())
  # top 11 similar movies contain the movie itself with similarity = 1, so I need to remove it. 
  top_11 = ks_similarity.sort_values(by = ['similarity'], ascending = False).head(11)
  joint = top_11.merge(movies_koalas, left_index=True, right_on = 'movieId', how = 'inner')
  joint.sort_values(by = ['similarity'], ascending = False,inplace = True)
  joint.reset_index(inplace = True)
  # take top 10 similar movies
  return joint.loc[1:,['movieId','title','genres']]

similar_movies(features = movie_factors['features'], movieId = 463)
similar_movies(features = movie_factors['features'], movieId = 471)

