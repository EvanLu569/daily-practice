from pyspark.sql import SparkSession

# 1. 用 RDD 实现 WordCount：读取一段英文文本，统计词频前 10 名
from pyspark import SparkContext

sc = SparkContext("local[*]", "WordCount")

# 造一段英文文本
text = """
 Python is great and Python is powerful
 Spark is fast and Spark is scalable
 Python and Spark together are amazing
 Python Python Spark Spark Spark
 """

rdd = sc.parallelize(text.split())

top10 = (
    rdd.map(lambda word: (word, 1))
    .reduceByKey(lambda a, b: a + b)
    .sortBy(lambda x: x[1], ascending=False)
    .take(10)
)
print("词频 Top 10：", top10)

sc.stop()

# 2. 用 Spark DataFrame 读取 CSV，按类别分组统计均值和总数
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, sum as spark_sum

spark = SparkSession.builder \
  .appName("DataAnalysis") \
  .master("local[*]") \
  .getOrCreate()

# 造数据
import pandas as pd
df_pd = pd.DataFrame({
  "类别": ["电子产品", "服装", "食品", "电子产品","服装", "食品", "电子产品"],
  "销售额": [35000, 28000, 42000, 30000, 25000, 40000,28000],
  "数量": [10, 20, 15, 12, 18, 14, 8],
})
df_pd.to_csv("day30/sales_spark.csv", index=False,encoding="utf-8-sig")

# Spark 读取 CSV
df = spark.read.csv("day30/sales_spark.csv", header=True,inferSchema=True)

df.show()
df.printSchema()

# 按类别分组：总销售额 + 平均销售额 + 总数量
result = df.groupBy("类别").agg(
  spark_sum("销售额").alias("总销售额"),
  avg("销售额").alias("平均销售额"),
  spark_sum("数量").alias("总数量"),
)
result.show()
# 3. 模拟 100 万条销售数据（造数据），用 PySpark 计算每个月的总销售额
#    对比用 pandas（单机）和 PySpark（分布式）的耗时差异
import time
import numpy as np

np.random.seed(42)
months = np.random.randint(1, 13, 1_000_000)
amounts = np.random.uniform(10, 1000, 1_000_000)
data_pd = pd.DataFrame({"月份": months, "金额": amounts})

# —— pandas 单机计算 ——
start = time.time()
pandas_result = data_pd.groupby("月份")["金额"].sum()
pandas_time = time.time() - start
print(f"\npandas 耗时：{pandas_time:.4f} 秒")

# —— PySpark 分布式计算 ——
df_spark = spark.createDataFrame(data_pd)
start = time.time()
spark_result = df_spark.groupBy("月份").agg(spark_sum("金额").alias("总销售额"))
spark_result.collect()  # 触发计算
spark_time = time.time() - start
print(f"PySpark 耗时：{spark_time:.4f} 秒")
print(f"pandas 快了 {spark_time / pandas_time:.1f} 倍")
print("（小数据下 pandas 更快，PySpark 优势在 TB级数据上才体现）")

spark.stop()















