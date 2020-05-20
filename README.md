# Movie Recommendation System
In this notebook, we will use an Alternating Least Squares(ALS) algorithm with Spark APIs to predict the ratings for the movies.

## Matrix Factorization -> ALS:
with our training and testing ratings matrices in hand, we can now move towards training a recommendation system. Explanations of matrix factorization often start with talks of "low rank matrices and singular value decomposition".

## Matrix Factorization Assumes that:
1. Each user can be described by k attributes or features(better understanding is the number of topics).
2. Each item can be described by an analagous set of k attributes or features.
3. If we multiply each feature of the user by the corresponding feature of the item and add everything together, this will be a good approximation for the rating the user would give that item.
![](My%20Folder/ALS.png)

## Write the report
1.Conduct exploratory data analysis like split genres into categories, count the number of movies under each category, etc. 

2.Build a recommendation model based on historical movie ratings and solve it by matrix factorization and alternating least squares (ALS).  

3.Tune the model parameters through grid search and crossvalidation with the metric root mean square errors (rmse). The optimal model has rmse = 0.64 on the training dataset and rmse = 0.889 on the test dataset.  

4.Recommend 10 movies to some certain users and find top 10 similar movies in terms of some specific movies.  

The best model I got has 5 latent factors (hidden features). These features describe a movie in 5 dimensions. Based on the feature, I can define the similarity between movies.  

In this model, I droped all unseen items and/or items during training process. The evaluation metric was computed over the non-NaN data and so, was valid. 

I tried twice to run it on the large dataset for the whole night. Maybe due to the community version, everytime when training the model more than 2 hours, my Spark broke down. In the future, I will run this model on a much larger dataset.  
