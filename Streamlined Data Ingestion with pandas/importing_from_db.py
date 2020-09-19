# Task: Create a database engine to manage connections to a database, data.db.

from sqlalchemy import create.engine() # importing the create engine fucntion
engine = create.engine("sqlite:///data.db") # creating the db engine
print(engine.table_names()) #view the table

#Task getting data from Database 

# Load pandas and sqlalchemy's create_engine
import pandas as pd 
from sqlalchemy import create_engine 

# Create database engine to manage connections 
engine = create_engine("sqlite:///data.db")

# Load entire weather table by table name
weather = pd.read_sql("weather", engine)


# Task: The records in hpd311calls often concern issues, like leaks or heating problems, that are exacerbated by weather conditions. In this exercise, you'll join weather data to call records and get everything in one data frame.

# Query to join weather to call records by date columns
query = """
SELECT * FROM hpd311calls JOIN weather 
  ON hpd311calls.created_date = weather.date;
"""
# Create data frame of joined tables
calls_with_weather = pd.read_sql(query, engine)
