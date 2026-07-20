'''
常用内置函数  map  filter  zip enumerate  any  all  max  min  sum  sorted
map(func,iterable)  对每个元素应用func，返回迭代器  list(map(str.upper,["a","b"]))
filter(func,iterable)  筛选出func返回True的元素 list(filter(lambda x:x>5,[1,2,3,4]))
zip(a,b)  把多个可迭代对象“拉链”成一对对 list(zip(["a","b"],[1,2]))  --->[("a",1),("b",2)]
enumerate(seq,start) 遍历时同时拿下标和元素 for i,v in enumerate(["a","b"],1):
any(iterable) 有一个True就返回True
all(iterable) 全部True才返回True
max/min/sum  最大值/最小值/求和
sorted(seq,key=,reverse=) 排序
'''
# 重点学习前三个
# 1.map
nums=[1,2,3,4,5]
squares=list(map(lambda n:n**2,nums))
print(squares)

# 2.filter
evens=list(filter(lambda x:x%2==0,nums))
print(evens)

# 3.zip
names = ["张三", "李四", "王五"]
scores = [95, 87, 72]
paired=list(zip(names,scores))
print(paired)












