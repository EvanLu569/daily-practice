#  字符串操作+lambda匿名函数

# 第一部分：字符串常用操作
# 1.split()  把字符串切成列表
s="苹果，香蕉，橘子，葡萄"
result=s.split("，")
print(result)

# 2.join()  把列表拼成字符串   split()的反操作
fruits=["apple","banana","oranges"]
result1="、".join(fruits)   #"分隔符".join(列表)，注意语法跟split是反过来的
print(result1)

# 3.replace()的反操作
msg="我的手机号是1800000000000"
safe=msg.replace("1800000000000","****")
print(safe)  # 我的手机号是****

# 4.strip()  去掉两端空白  用户输入经常带空格，用strip清理
name="  张三   "
clean=name.strip()
print(f"{clean}")

# 5.find()和in   查找
text="hello world"
print(text.find("world"))  # 6（位置，找不到返回-1）
print("world"in text)  # True（只会告诉你有没有）

# 6.upper()/lower  大小写
name="Evan"
print(name.upper())
print(name.lower())

# 第二部分：lambda匿名函数  lambda就是一个不用写def的一行函数
# 普通写法
def double(x):
    return x*2
# lambda写法
double=lambda y:y*2  # 格式：lambda 参数：返回值
# 单独用lambda没啥意思，它真正的价值是配合下面三个函数：

#1. sorted+lambda  按指定规则排序
students=[
    {"name":"zhangsan","score":90},
    {"name":"lisi","score":99},
    {"name":"wangwu","score":100}
]
ranked=sorted(students,key=lambda s:s["score"],reverse=True)  # 按成绩从高到低排序
print(ranked)

# 2.filter+lambda   筛选
nums=[1,2,3,4,5,6]
evens=list(filter(lambda x:x%2==0,nums))
print(evens)

# 3.map+lambda   批量处理
names=["evan","zhangsan"]
upper=list(map(lambda n:n.upper(),names))
lower=list(map(lambda n:n.lower(),names))
print(upper)
print(lower)



