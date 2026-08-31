# Databricks notebook source
import dlt
from pyspark.sql.functions import *

# COMMAND ----------

@dlt.table(name="people_bronze")
def people_bronze():
    return(
        spark.readStream
        .format("cloudFiles")
        .option("cloudFiles.format","csv")
        .option("header","true")
        .option("inferschema","true")
        .load("/Volumes/practice/sapana_p/practice_volume/people/")
        .withColumn("ingestion_time",current_timestamp() )
        
    )

    
    