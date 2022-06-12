import pyspark
import os
import numpy
from pyspark.sql import SparkSession
import pyspark.sql.functions as sql_fun
from pyspark.ml.recommendation import ALS


# Load the dataset
DATAPATH = r'/home/daniel/Desktop/programming/pythondatascience/datascience/dataengineering/datasets/movieLens25m/'
movies = os.path.join(DATAPATH, 'movies.csv')
ratings = os.path.join(DATAPATH, 'ratings.csv')

spark = SparkSession.builder.appName('recommend').getOrCreate()
# movies = spark.read.csv(movies, inferSchema = True, header = True)
# ratings = spark.read.csv(ratings, inferSchema = True, header = True)


# sc = spark.sparkContext
# # Load the recommender model
# model = ALS.load("modelV1.model")
# print(model)

# # We will only work with 5 million records
# ratings = ratings.limit(5000000)

# # Load the movies and ratings dataset in memory to improve performance
# ratings=ratings.repartition(10).cache()
# movies=movies.repartition(10).cache()


