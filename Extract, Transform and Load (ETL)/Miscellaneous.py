#  1.  To get the data into the Spark framework.
spark.read.jdbc("jdbc:postgresql://localhost:5432/pagila",
                "customer",
                {"user":"repl","password":"password"})
                
# 2.1. Write the pandas DataFrame film_pdf to a parquet file called "films_pdf.parquet".
        film_pdf.to_parquet("films_pdf.parquet")

# 2.2. Write the PySpark DataFrame film_sdf to a parquet file called "films_sdf.parquet".
        film_sdf.write.parquet("films_sdf.parquet")

# 3.  add a DAG to Airflow. 
    1. If the workspace comes with Airflow pre-configured, but it's easy to install on your own.
    2. Move the dag.py file containing the DAG you defined in the previous exercise to, the DAGs folder. Here are the steps to find it:
        a. The airflow home directory is defined in the AIRFLOW_HOME environment variable. Type echo $AIRFLOW_HOME to find out.
        b. In this directory, find the airflow.cfg file. Use head to read the file, and find the value of the dags_folder.
    3. Now you can find the folder and move the dag.py file there: mv ./dag.py <dags_folder>. 
