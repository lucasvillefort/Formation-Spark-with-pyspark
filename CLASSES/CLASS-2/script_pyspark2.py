# now using sys.argv[1] to pass the path to the file despachantes.csv
import sys  # to use sys.argv[1] to pass the path to the file despachantes.csv in terminal

from pyspark.sql import SparkSession
from pyspark.sql.functions import *

# need to use spark-submit to run this script
# sys.argv[1] is the path to the file despachantes.csv in terminal for example: 
#       spark-submit script_pyspark2.py ../../DOWNLOAD/despachantes.csv

if __name__ == "__main__":
    spark = SparkSession.builder.appName("Example").getOrCreate()  # Create a SparkSession
    arq_schema = "id INT, nome STRING, status STRING, cidade STRING, vendas INT, data STRING"
    despachantes = spark.read.csv(sys.argv[1], header=False, schema=arq_schema)
    despachantes.show()
    despachantes.printSchema()
    calculo = despachantes.select("data").groupBy("data").count()
    calculo.write.format("console").save()
    spark.stop()
    
    
    
    