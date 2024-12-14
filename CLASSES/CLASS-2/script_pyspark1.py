from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# need to use spark-submit to run this script

if __name__ == "__main__":
    spark = SparkSession.builder.appName("Example").getOrCreate()  # Create a SparkSession
    arq_schema = "id INT, nome STRING, status STRING, cidade STRING, vendas INT, data STRING"
    despachantes = spark.read.csv("../../DOWNLOAD/despachantes.csv", header=False, schema=arq_schema)
    despachantes.show()
    despachantes.printSchema()
    calculo = despachantes.select("data").groupBy("data").count()
    calculo.write.format("console").save()
    spark.stop()
    
    
    
    