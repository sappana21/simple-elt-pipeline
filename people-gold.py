# Databricks notebook source
import dlt
from pyspark.sql.functions import count, avg, col, when

# COMMAND ----------

#gender wise count
@dlt.table(name="people_gold_gender_summary")
def people_gold_gender_summary():
    return (
        dlt.read("people_silver")
        .groupBy("Sex")
        .agg(
            count("*").alias("people_count")
        )
    )

#top job titles
@dlt.table(name="people_gold_job_title_counts")
def people_gold_job_title_counts():
    return (
        dlt.read("people_silver")
        .groupBy("Job_Title")
        .agg(count("*").alias("people_count"))
        .orderBy(col("people_count").desc())
        .limit(10)
    )