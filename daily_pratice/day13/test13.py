# 1. 用 map() 把 ["1", "2", "3", "4"] 转成整数列表 [1, 2, 3, 4]
nums=["1", "2", "3", "4"]
result=list(map(int,nums))
print(result)
# 2. 用 filter() 从 [15, 22, 8, 37, 41, 10] 中筛选 >= 20 的数
nums=[15, 22, 8, 37, 41, 10]
result=list(filter(lambda n:n>=20,nums))
print(result)
# 3. 用 zip() 把 ["张三", "李四", "王五"] 和 [95, 87, 72] 合并成字典
students=["张三", "李四", "王五"]
scores=[95, 87, 72]
paired=list(zip(students,scores))
print(paired)
# 4. 用 enumerate() 打印列表，格式为 "第1名：张三"、"第2名：李四"...
names = ["张三", "李四", "王五"]
for i,n in enumerate(names,start=1):
    print(f"第{i}名：{n}")
# 5. 用 any() 判断列表中是否存在负数
result=any(map(lambda x:x<0,nums))
print(result)

# 1. 用 map + lambda 把列表中所有数平方
nums = [1, 2, 3, 4, 5]
square=list(map(lambda x:x**2,nums))
print(square)
# 2. 用 filter + lambda 筛选出所有以 "py" 开头的字符串
modules = ["pytest", "numpy", "pandas", "requests", "python"]
print(list(filter(lambda ch:ch.startswith("py"),modules)))
# 3. 用 sorted + lambda 按分数降序排列学生
students = [("张三", 85), ("李四", 92), ("王五", 78)]
result=sorted(students,key=lambda x:x[1],reverse=True)
print(result)
# 4. 用 map + lambda 提取上面列表中的所有名字
# 期待：["张三", "李四", "王五"]
result=list(map(lambda x:x[0],students))
print(result)
# 5. 用 any + 生成器表达式 判断列表中是否存在长度 > 10 的字符串
words = ["hello", "world", "python programming", "code"]
result=any(len(w)>10 for w in words)
print(result)

