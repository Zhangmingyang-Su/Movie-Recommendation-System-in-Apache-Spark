movies_df.registerTempTable("movies")
ratings_df.registerTempTable("ratings")
links_df.registerTempTable("links")
tags_df.registerTempTable("tags")

--The number of Users
%sql 
Select count(distinct userID) as Number_of_users from ratings

--The number of Movies
%sql 
Select count(distinct movieId) as Numer_of_movies from movies

--How many movies are rated by users? List movies not rated before
%sql
Select m.title, m.genres from movies as m 
where m.movieId not in 
  (Select movieId from ratings)
  
 --How many movies are rated by users?
 %sql 
Select count(distinct b.movieId) as Number_movies_are_rated_by_users from ratings as b

--List Movie Genres
%sql
Select distinct genres from movies
%sql
Select distinct Category from movies
lateral view explode(split(genres,'[|]')) as Category order by Category

--Movie for Each Category
%sql
Select Category, count(movieId) as number from movies
lateral view explode(split(genres,'[|]')) as Category group by Category order by number desc 
%sql
select t.Category, concat_ws(',',collect_set(t.title)) as list_of_movies from
  (
    Select Category, title from movies
    lateral view explode(split(genres,'[|]')) as Category 
    group by Category, title
    ) as t
group by t.Category
                         
                         



