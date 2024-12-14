# now using sys.argv[1] to pass the path to the file despachantes.csv
# to use sys.argv[1] to pass the path to the file despachantes.csv in terminal
import getopt  # to get arguments from command line for example: python script_pyspark3.py -f ../../DOWNLOAD/despachantes.csv
import sys

from pyspark.sql import SparkSession
from pyspark.sql.functions import *
 
# need to use spark-submit to run this script
# sys.argv[1] is the path to the file despachantes.csv in terminal for example: 
#       spark-submit script_pyspark3.py ../../DOWNLOAD/despachantes.csv

if __name__ == "__main__":
    spark = SparkSession.builder.appName("Example").getOrCreate()  # Create a SparkSession
    opts, args = getopt.getopt(sys.argv[1:], "t:i:o:") # "t:i:o:" is the format of the arguments
    format_file, input_file, output_directory = "", "", ""
    for opt, arg in opts:
        if opt == "-t":
            format_file = arg
        elif opt == "-i":
            input_file = arg
        elif opt == "-o":
            output_directory = arg
            
    datas = spark.read.csv(input_file, header=False, inferSchema=True)
    datas.write.format(format_file).save(output_directory)
    spark.stop()
    
# to run this script in terminal:
#       spark-submit script_pyspark3.py -t parquet -i ../../DOWNLOAD/despachantes.csv -o ../../DOWNLOAD/output
    
    
    