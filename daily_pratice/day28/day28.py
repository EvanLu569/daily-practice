'''
pandas是python最常用的数据处理库

Series：带标签的一列数据，像excel的一列，有列名
Dataframe：一张表格，像excel的整个sheet，行列都有标签
'''
from operator import index

import pandas as pd
import numpy as np

# # Series：一维带标签数组
# s=pd.Series([88,92,76,95],index=['小明','小红','小刚','小丽'])
# print(s)
# print(s['小红']) # 按标签取
# print(s.iloc[1]) # 按位置取
# print(s.mean()) # 平均值
#
# # DataFrame：二维表格
# data={
#     'name':['xiaoming','xiaohong','xiaogang','xiaoli'],
#     'chinese':[88,92,76,95],
#     'math':[99,89,79,90],
#     'english':[100,97,95,69]
# }
# df=pd.DataFrame(data)
# print(df)
# print(df.shape) # （行数，列数）
# print(df.columns) # 所有列名
# print(df.dtypes) # 每列的数据类型
#
# print("\n","*"*20,"csv操作","*"*20)
# csv_content="""
#   姓名,语文,数学,英语,班级
#   小明,88,85,78,1班
#   小红,92,96,95,2班
#   小刚,76,70,65,1班
#   小丽,95,90,88,2班
#   小王,80,,75,1班
#   小李,,82,90,2班
# """
# with open('G:\代码\PythonProject\daily_pratice\day28\students.csv','w',encoding='utf-8') as f:
#     f.write(csv_content)
#
# '''
# 读取csv
# '''
# df=pd.read_csv('G:\代码\PythonProject\daily_pratice\day28\students.csv')
# print(df)
# print("*"*50)
# print(df.info()) # 每列类型、非空数量
# print("*"*50)
# print(df.describe()) # 数值列的统计信息
#
# # 缺失值处理
# print("*"*50)
# print(df.isnull().sum()) # 每列缺失值个数
# df['数学']=df['数学'].fillna(df['数学'].mean())
# df['语文']=df['语文'].fillna(df['语文'].mean())
# print("*"*50)
# print(df)
#
# print("*"*50)
# # 分组聚合
# print(df.groupby('班级')['语文'].mean())
#
# print("*"*50)
# print(df.groupby('班级')[['语文','数学','英语']].mean())
#

'''
NumPy核心就一个概念：ndarray（n维数组）
和python list最大的区别：所有元素必须是同一类型，计算是向量化的
'''
arr=np.array([1,2,3,4,5])
print(arr) # 注意看没有逗号
print("*"*50)
print(type(arr))
print("*"*50)
print(arr.dtype) # 元素类型
print("*"*50)

# 和list对比：list存的是python对象，ndarray存的是紧凑的C类型
py_list=[1,2,3,4,5]
print(py_list)
print("*"*50)
print(py_list*2)
print("*"*50)
print(arr*2)
print("*"*50)

print("常用创建函数：")
print(np.zeros(5))  # 全0
print(np.ones((2,3))) # 全1 ，2行3列
print(np.arange(0,10,2))
print(np.linspace(0,1,5))  # 等间距5个点
print(np.random.randn(100)) # 100个标准正态分布随机数

print("*"*50)
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(a @ b)        # 矩阵乘法（或 np.dot(a, b)）
print(a.T)          # 转置
















