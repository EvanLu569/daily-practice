# 集合（set）+列表推导式
# 第一部分：集合set  集合和列表长的像，但有三个关键区别
#集合的特点：无序，不重复，自动去重
# 创建集合
fruits={"苹果","香蕉","橘子"}
print(fruits) #每次结果的顺序可能不一样

# 自动去重
nums={1,2,3,4,5,5,5,5,5}
print(nums)

# 集合运算
a={1,2,3,4}
b={3,4,5,6}
print(a&b) #交集
print(a|b) #并集，合起来有去重
print(a-b) #差集，a有b没有

# 面试常考去重题
lst=[1,2,2,3,3,3]
unique=list(set(lst))
print(unique) # 结果[1,2,3]

# 增删操作
s={1,2,3}
s.add(4) #增
s.remove(2) #删
print(2 in s) # 2是否在集合内

# 第二部分：列表推导式  作用：一行代码生成列表，代替for循环
# 普通写法：把1-5的平方放进列表
squares=[]
for i in range(1,6):
    squares.append(i**2)
print(squares)

# 列表推导式
squares=[i**2 for i in range(1,6)] # 格式：[表达式 for 变量 in 可迭代对象]
print(squares)

# 只要偶数
evens=[x for x in range(1,11)if  x%2==0]
print(evens)

# 处理+筛选一起
nums=[1,2,3,4,5]
doubled=[n*2 for n in nums if n>2]
print(doubled)

# 字典推导式  快速构造一个字典
squares_dict={x:x**2 for x in range(1,6)}
print(squares_dict)







