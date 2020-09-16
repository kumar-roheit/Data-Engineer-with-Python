# cat /home/repl/spark-script.py to view the code
if __name__ == "__main__":
    spark = SparkSession.builder.getOrCreate()
    athlete_events_spark = (spark
        .read
        .csv("/home/repl/datasets/athlete_events.csv",
             header=True,
             inferSchema=True,
             escape='"'))

    athlete_events_spark = (athlete_events_spark
        .withColumn("Height",
                    athlete_events_spark.Height.cast("integer")))

    print(athlete_events_spark
        .groupBy('Year')
        .mean('Height')
        .orderBy('Year')
        .show())
        
# Spark submit to submit the above script to spark cluster. 
# RESULT : A DataFrame with average Olympian heights by year.
spark-submit \
> --master local[4] \
> /home/repl/spark-script.py

