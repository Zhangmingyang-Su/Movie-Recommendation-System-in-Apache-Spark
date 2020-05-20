# Movie Recommender System
In this notebook, we will use an Alternating Least Squares(ALS) algorithm with Spark APIs to predict the ratings for the movies.

## Matrix Factorization -> ALS:
with our training and testing ratings matrices in hand, we can now move towards training a recommendation system. Explanations of matrix factorization often start with talks of "low rank matrices and singular value decomposition".

## Matrix Factorization Assumes that:
1. Each user can be described by k attributes or features(better understanding is the number of topics).
2. Each item can be described by an analagous set of k attributes or features.
3. If we multiply each feature of the user by the corresponding feature of the item and add everything together, this will be a good approximation for the rating the user would give that item.
