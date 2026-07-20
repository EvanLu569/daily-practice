'''
PySpark 是大数据领域的标配框架，底层是 Spark（Scala 写的），通过 Python API 调用。
RDD（弹性分布式数据集）：Spark 最基础的抽象，已基本被 DataFrame 取代
DataFrame：类似 pandas DataFrame，但数据分布在多台机器上
分布式计算：数据拆分到多个节点，每个节点算自己那份，最后汇总
懒执行：转换操作不立即执行，遇到 action（如 count/collect）才触发计算
'''
from pyspark import SparkContext
sc=SparkContext("local[*]","MyApp") # # local[*] = 用你电脑所有 CPU 核心模拟分布式
rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# 转换（懒执行，不触发计算）
rdd2 = rdd.filter(lambda x: x % 2 == 0)
rdd3 = rdd2.map(lambda x: x ** 2)

# action（触发计算）
print(rdd3.collect())  # [4, 16, 36, 64, 100]
print(rdd.count())  # 10
print(rdd.sum())  # 55
print(rdd.take(3))  # [1, 2, 3]

text = sc.parallelize(["hello world", "hello spark","world spark"])
word_counts=(
    text
    .flatMap(lambda line:line.split())
    .map(lambda word:(word,1))
    .reduceByKey(lambda a,b:a+b)
    .sortBy(lambda x:x[1],ascending=False)
)
print(word_counts.collect())
sc.stop()

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, max, min, count, sum as spark_sum
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

spark = SparkSession.builder \
    .appName("DataAnalysis") \
    .master("local[*]") \
    .getOrCreate()

# 从列表创建 DataFrame
data = [
    ("张三", 20, 85),
    ("李四", 22, 92),
    ("王五", 21, 78),
    ("赵六", 23, 88),
    ("孙七", 19, 95),
]
columns = ["姓名", "年龄", "分数"]
df = spark.createDataFrame(data, columns)

# 基础操作
df.show()                     # 打印前 20 行
df.printSchema()              # 打印表结构
df.select("姓名", "分数").show()
df.filter(col("分数") > 85).show()
df.filter((col("分数") > 80) & (col("年龄") > 20)).show()

# 分组聚合（和 SQL 一样，但数据分布在各台机器上并行执行）
df.groupBy("年龄").agg(
    avg("分数").alias("平均分"),
    max("分数").alias("最高分"),
    count("*").alias("人数"),
).orderBy("年龄").show()

# 新增列
df = df.withColumn("等级",
    SparkSession.when(col("分数") >= 90, "优秀")
                .when(col("分数") >= 80, "良好")
                .otherwise("及格")
)

# 排序
df.orderBy(col("分数").desc()).show()

# 转成 pandas（小数据适用）
pdf = df.toPandas()
print(pdf)

# 从 CSV 读取
# df = spark.read.csv("data.csv", header=True, inferSchema=True)

# 写回 CSV
# df.write.csv("output", header=True)

# Spark SQL
df.createOrReplaceTempView("students")
spark.sql("SELECT 年龄, AVG(分数) AS 平均分 FROM students GROUP BY 年龄").show()

spark.stop()







