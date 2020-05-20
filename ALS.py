from pyspark.sql.types import IntegerType, FloatType
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.ml.tuning import CrossValidator,ParamGridBuilder

ratings_df.show()
# drop column
movie_ratings=ratings_df.drop('timestamp')
# Data type convert
movie_ratings = movie_ratings.withColumn("userId", movie_ratings["userId"].cast(IntegerType()))
movie_ratings = movie_ratings.withColumn("movieId", movie_ratings["movieId"].cast(IntegerType()))
movie_ratings = movie_ratings.withColumn("rating", movie_ratings["rating"].cast(FloatType()))

movie_ratings.show()

# ALS model selection and evaluation
#Create test and train set
(training,test)=movie_ratings.randomSplit([0.8,0.2], seed = 2020)

#Create ALS model
als = ALS(maxIter=5, rank=10, regParam=0.01, userCol="userId", itemCol="movieId", ratingCol="rating",
          coldStartStrategy="drop")

#Tune model using ParamGridBuilder
paramGrid = ParamGridBuilder()\
            .addGrid(als.regParam, [0.1, 0.01, 0.001])\
            .addGrid(als.maxIter, [3, 5, 10])\
            .addGrid(als.rank, [5, 10, 15])\
            .build()

# Define evaluator as RMSE
evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating",
                                predictionCol="prediction")

# Build Cross validation 
crossval = CrossValidator(estimator=als,
                          estimatorParamMaps=paramGrid,
                          evaluator=evaluator,
                          numFolds=5)

#Fit ALS model to training data
model = als.fit(training)

#Extract best model from the tuning exercise using ParamGridBuilder
cvModel = crossval.fit(training)
predictions = cvModel.transform(training)
rmse = evaluator.evaluate(predictions)
print("Root-mean-square error = " + str(rmse))

# Model testing
#Generate predictions and evaluate using RMSE
best_model = cvModel.bestModel
predictions=best_model.transform(test)
rmse = evaluator.evaluate(predictions)

#Print evaluation metrics and model parameters
print ("RMSE = "+str(rmse))
print ("**Best Model**")
print (" Rank:"+str(best_model._java_obj.parent().getRank())), 
print (" MaxIter:"+str(best_model._java_obj.parent().getMaxIter())), 
print (" RegParam:"+str(best_model._java_obj.parent().getRegParam()))

predictions.show()

# Model apply and see the performance
alldata=best_model.transform(movie_ratings)
rmse = evaluator.evaluate(alldata)
print ("RMSE = "+str(rmse))
