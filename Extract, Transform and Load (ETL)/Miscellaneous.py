#  1. To get the data into the Spark framework.
spark.read.jdbc("jdbc:postgresql://localhost:5432/pagila",
                "customer",
                {"user":"repl","password":"password"})
                
                
