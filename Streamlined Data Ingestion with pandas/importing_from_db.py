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
