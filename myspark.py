#spark session
from pyspark.sql import SparkSession
from functools import lru_cache

def get_spark():
    return (SparkSession.builder
                .master("local")
                .appName("myapp")
                .getOrCreate())