dbutils.library.installPyPI("koalas")
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
import databricks.koalas as ks

import warnings
warnings.filterwarnings("ignore")
import os
os.environ["PYSPARK_PYTHON"] = "python3"

from pyspark.sql import SparkSession
spark = SparkSession \
    .builder \
    .appName("moive analysis") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

# load data from DBFS
movies_df = spark.read.load("/FileStore/tables/movies.csv", format='csv', header = True)
ratings_df = spark.read.load("/FileStore/tables/ratings.csv", format='csv', header = True)
links_df = spark.read.load("/FileStore/tables/links.csv", format='csv', header = True)
tags_df = spark.read.load("/FileStore/tables/tags.csv", format='csv', header = True)

movies_df.show(5)
ratings_df.show(5)
links_df.show(5)
tags_df.show(5)

tmp1 = ratings_df.groupBy("userID").count().select('count').rdd.min()[0]
tmp2 = ratings_df.groupBy("movieId").count().select('count').rdd.min()[0]
print('For the users that rated movies and the movies that were rated:')
print('Minimum number of ratings per user is {}'.format(tmp1))
print('Minimum number of ratings per movie is {}'.format(tmp2))

tmp1 = ratings_df.groupBy("movieId").count().filter('count = 1').count()
tmp2 = ratings_df.select('movieId').distinct().count()
print('{} out of {} movies are rated by only one user'.format(tmp1, tmp2))
