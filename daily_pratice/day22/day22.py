'''
数据容器的通用操作
python的数据容器（list,tuple,set,dict,str）共享一套操作模式。
'''
# 五大容器对比
#列表  有序、可变、可重复
lst=[1,2,3]
# 元组  有序、不可变、可重复
tup=(1,2,3)
# 集合  无序、可变、不重复
st={1,2,3}
# 字典 键值对、键不可重复
dic={"a":1,"b":2}
# 字符串  有序、不可变、字符序列
txt="hello"

# 通用操作
# 1.长度
len([1,2,3]) # 3
len("hello") # 5
len({"a":1}) # 1
# 2.成员判断
3 in [1,2,3] # True
"h" in "hello" # True
"a" in {"a":1} # True
# 3.遍历
for item in [1,2,3]:
    print(item)
for ch in "hello":
    print(ch)
for key in {"a":1}:
    print(key)
# 4.索引
lst[0] #下标
lst[-1] # 反向
lst[1:3] # 切片

# 5.解包
a,b,c=[1,2,3] # a=1,b=2,c=3
x,*rest=[1,2,3,4] # x=1,rest=[2,3,4]
first,*_,last=[1,2,3,4] # 中间丢掉2，3,first=1,last=4
# 6.合并
# [1,2]+[3,4] # [1,2,3,4]
# "hello "+"world" # "hello world"
# {1,2}+{2,3} # {1,2,3}
# {**{"a":1},**{"b":2}} # {"a":1,"b":2}
# 7.复制
lst[:],lst.copy()
"hello"[:]
# 8.最值/求和
max([1,2,3])
min([1,2,3])
sum([1,2,3])
max("hello")

# 容器互转
list("hello")
['h','e','l','l','o']
list((1,2,3))
tuple([1,2,3])
set([1,2,2,3])
list({"a":1,"b":2})
dict([("a",1),("b",2)])
str([1,2,3])
",".join(["a","b","c"])
"hello world".split()

'''
闭包  是装饰器的基础  内层函数记住了外层函数的变量
闭包的三个条件
1.外层函数里定义了内层函数
2.内层函数引用了外层函数的变量
3.外层函数返回内层函数本身
'''
# 普通函数：调用完变量就没了
def outer():
    x=10
    return x+1
# 闭包：内部函数“记得”外部变量
def outer(x):
    def inner(y):
        return x+y # inner记住了x
    return inner # 返回的是函数本身，不是计算结果
add_10=outer(10)  # x=10被inner记住了
print(add_10(5))
print(outer(20))

# 闭包的实际用途
# 1.工厂函数  生成特定配置的函数
def make_multiplier(n):
    def multiplier(x):
        return x*n
    return multiplier
double=make_multiplier(2)
triple=make_multiplier(3)
print(double(5)) # 10
print(triple(5)) # 15

# 2.带“记忆”的计数器
def make_counter():
    count=0
    def counter():
        nonlocal count # 声明要修改外层变量
        count+=1
        return count
    return counter
c=make_counter()
print(c()) # 1
print(c()) # 2
print(c()) # 3
print(c()) # 4  每次调用c(),count保持上一次的值，不会被重置
# 3.简易缓存（不用lru_cache时的代替）
def make_cacher():
    cache={}
    def cacher(key,value=None):
        if value is not None:
            cache[key]=value
        return cache.get(key)
    return cacher
memo=make_cacher()
memo("name","zhangsan")
print(memo("name"))

# nonlocal关键字
def outer():
    x=10
    def inner():
        nonlocal x  # 告诉python，我要改外层的x，别把它当局部变量
        x+=1
        return x
    return inner




