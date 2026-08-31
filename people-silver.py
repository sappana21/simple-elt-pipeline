# Databricks notebook source
import dlt

# COMMAND ----------

@dlt.table(name="people_silver")
def people_silver():
    return(
        dlt.read("people_bronze")
        .select(
            "User_ID",
            "Email",
            "Phone",
            "Date_of_birth",
            "Job_Title",
            "Sex"
        ) .dropDuplicates(["Phone","Email","User_ID"])
        
    )
