#  1.  To get the data into the Spark framework.
spark.read.jdbc("jdbc:postgresql://localhost:5432/pagila",
                "customer",
                {"user":"repl","password":"password"})
                
# 2.1. Write the pandas DataFrame film_pdf to a parquet file called "films_pdf.parquet".
        film_pdf.to_parquet("films_pdf.parquet")

# 2.2. Write the PySpark DataFrame film_sdf to a parquet file called "films_sdf.parquet".
        film_sdf.write.parquet("films_sdf.parquet")
