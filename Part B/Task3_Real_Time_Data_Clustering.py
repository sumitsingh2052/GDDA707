from pyspark.sql import SparkSession
from pyspark.ml.clustering import KMeans
from pyspark.ml.feature import VectorAssembler

# Initialize Spark session with Kafka package
spark = SparkSession.builder \
    .appName("RealTimeClustering") \
    .config("spark.jars.packages", "org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1") \
    .getOrCreate()

# Read real-time data from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "social_media") \
    .load()

# Transform data
df_transformed = df.selectExpr("CAST(value AS STRING) as json_data") \
    .selectExpr("CAST(json_data AS STRING) AS value")

# Use VectorAssembler to prepare data for K-Means
vector_assembler = VectorAssembler(inputCols=["feature1", "feature2"], outputCol="features")
data_vectorized = vector_assembler.transform(df_transformed)

# Apply K-means clustering
kmeans = KMeans(k=3, seed=1)
model = kmeans.fit(data_vectorized)
clusters = model.transform(data_vectorized)

# Output clustered data
query = clusters.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()
