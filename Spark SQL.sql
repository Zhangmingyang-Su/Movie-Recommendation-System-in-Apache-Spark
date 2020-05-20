movies_df.registerTempTable("movies")
ratings_df.registerTempTable("ratings")
links_df.registerTempTable("links")
tags_df.registerTempTable("tags")

# The number of Users
%sql 
Select count(distinct userID) as Number_of_users from ratings

# The number of Movies
%sql 
Select count(distinct movieId) as Numer_of_movies from movies


