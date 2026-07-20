import pandas as pd
import numpy as np

# data={
#     'name':['xiaoming','xiaohong','xiaogang','xiaoli'],
#     'chinese':[88,92,76,95],
#     'math':[99,89,79,90],
#     'english':[100,97,95,69]
# }
# df=pd.DataFrame(data)
# # 练习1：用df['语文']取出语文成绩列，算出语文的平均分、最高分、最低分。
# print(df['chinese'])
# print(df['chinese'].mean())
# print(df['chinese'].max())
# print(df['chinese'].min())
#
# # 练习2：添加一列总分 = 语文 + 数学 + 英语。提示：直接df['总分'] = df['语文'] + df['数学'] + df['英语']
# df['sum']=df['chinese']+df['math']+df['english']
# print(df['sum'])
# # 练习3：用df[df['数学'] >= 90]筛选出数学成绩 >= 90的学生。
# print(df[df['math']>=90])
# # 练习4：用df.sort_values('总分', ascending=False)按总分降序排列。
# print(df.sort_values('sum',ascending=False))
#
# '''
# 问题1：df.info() 和 df.describe()的区别是什么？分别在什么场景用？
# df.info()的作用是查看数据结构，适用于数据探索和数据清洗
# df.describe()的作用是查看统计信息，适用于数据分析和异常检测
#
# 问题2：小王数学和小李语文是 NaN。用df['数学'].fillna(df['数学'].mean())试试，看看什么效果？.fillna() 是干嘛的？
# .fillna()的作用是填充缺失值，将NaN替换成指定的值。
# df['数学'].fillna(df['数学'].mean())的意思是将数学平均分填充进小王数学成绩中
#
# 问题3：用 df.groupby('班级')['语文'].mean()算出每个班的语文平均分。.groupby()的语法逻辑你能描述出来吗——先按什么分，再对什么做计算？
# .groupby是先按班级分组，选择语文列，计算平均值
#
# 问题4：对比 df[df['数学'] >= 90] 和 df.query('数学 >=90')，两种筛选写法你觉得哪个更可读
# df[df['数学'] >= 90]：返回布尔值，用布尔Series作为索引筛选行
# df.query('数学 >=90')：直接写SQL风格的字符串表达式，更可读
# '''
# print("*"*50)
# # 练习：用你现有的学生DataFrame，加一列'等级'：
# # - 成绩 >= 90 → '优秀'
# # - 成绩80~89 → '良好'
# # - 成绩 < 80 → '及格'
# df['成绩等级']=df['chinese'].apply(lambda x:'优秀'if x>=90 else '良好'if x>=80 else '及格')
# # print(df)


# 1. 创建一个 DataFrame，包含 20 条学生成绩数据（姓名、语文、数学、英语），计算总分和平均分
names = np.random.choice(['张三', '李四', '王五', '赵六','刘七'], 20)
chinese = np.random.randint(50, 100, 20)   # 50~99随机整数
math = np.random.randint(50, 100, 20)
english = np.random.randint(50, 100, 20)
df = pd.DataFrame({
  '姓名': names,
  '语文': chinese,
  '数学': math,
  '英语': english,
})
print(df)
print("*"*50)
df['总分'] = df['语文'] + df['数学'] + df['英语']
df['平均分'] = (df['总分'] / 3).round(1)  # 保留一位小数
print(df)
print("*"*50)

# 2. 找出总分前 5 名和单科不及格（< 60）的学生
print("总分前5名")
print(df.nlargest(5, '总分')[['姓名', '总分']])
print("单科不及格（< 60）")
print("语文不及格：")
print(df[df['语文'] < 60][['姓名', '语文']])
print("数学不及格：")
print(df[df['数学'] < 60][['姓名', '数学']])
print("英语不及格：")
print(df[df['英语'] < 60][['姓名', '英语']])
# 3. 分析每科的均分、最高分、最低分、标准差
print("*"*50)
print("每科统计")
stats = df[['语文', '数学', '英语']].agg(['mean', 'max','min', 'std']).round(2)
print(stats)

# 4. 用 numpy 生成 1000 个正态分布随机数，计算均值、标准差，找出分布在 (均值 ± 1标准差) 内的比例
print("*"*50)
arr = np.random.randn(1000)
mean = arr.mean()
std = arr.std()
print(f"均值：{mean:.4f}，标准差：{std:.4f}")
# 均值 ± 1 标准差内的比例
in_range = np.sum((arr > mean - std) & (arr < mean + std))
ratio = in_range / 1000
print(f"在 (均值±1标准差)内的个数：{in_range}，比例：{ratio:.2%}")
print("（正态分布理论值约为 68.27%）")
# 5. 从 CSV 读取数据，做数据清洗（去空值、去重），按某列分组统计，导出结果
print("*"*50)
df.to_csv('G:\代码\PythonProject\daily_pratice\day28\students02.csv', index=False,encoding='utf-8-sig')
df2 = pd.read_csv('G:\代码\PythonProject\daily_pratice\day28\students02.csv')
print(f"读取成功，共 {len(df2)} 行")

#故意加两条重复行和带空值的行（模拟脏数据）
dirty_rows = pd.DataFrame({
    '姓名': ['张三', '新同学'],
    '语文': [df['语文'].iloc[0], np.nan],  #一条重复，一条有空值
    '数学': [df['数学'].iloc[0], 88],
    '英语': [df['英语'].iloc[0], 76],
    '总分': [df['总分'].iloc[0], np.nan],
    '平均分': [df['平均分'].iloc[0], np.nan],
})
df2 = pd.concat([df2, dirty_rows], ignore_index=True)
print(f"加脏数据后：{len(df2)}行，空值数：{df2.isnull().sum().sum()}")

# 清洗
df2 = df2.dropna()  # 删有空值的行
df2 = df2.drop_duplicates()  # 删重复行
print(f"清洗后：{len(df2)} 行")

# 按姓名分组统计（每人可能出现多次，取平均）
print("每人平均分")
result = df2.groupby('姓名')[['语文', '数学', '英语',
                              '总分']].mean().round(1)
print(result)

# 导出结果
result.to_csv('G:\代码\PythonProject\daily_pratice\day28\students02.csv', encoding='utf-8-sig')
print("\n结果已导出到 G:\代码\PythonProject\daily_pratice\day28\students02.csv")





