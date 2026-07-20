'''
functools.lru_cache   函数结果缓存
递归或重复计算时，缓存中间结果，极大加速
'''
from functools import lru_cache
import time
@lru_cache(maxsize=128)
def fibonacci(n:int)->int:
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
stat=time.time()
print(fibonacci(40))
print(f"耗时：{time.time()-stat:.4f}秒")

# functools.reduce  累计计算
from functools import reduce
result=reduce(lambda x,y:x*y,[1,2,3,4,5])
print(result) # 过程 （（（1*2）*3）*4）*5

# 实际应用:嵌套字典取值（项目常用）
data={"user":{"profile":{"name":"zhangsan"}}}
name=reduce(lambda d,key:d.get(key,{}),["user","profile","name"],data)
print(name)

# itertools  迭代器工具箱
from itertools import chain,groupby,combinations,permutations,islice
# chain  把多个可迭代对象串在一起
all_items=list(chain([1,2],[3,4],[5,6]))
print(all_items)

# combinations 所有可能的组合（顺序不重要）
print(list(combinations("ABC",2)))

# permutations  所有可能的排列（顺序重要）
print(list(permutations("ABC",2)))

# islice 从生成器中截取（不需要全部算出来）
from itertools import count
first_10_odds=list(islice((i for i in count()if i%2==1),10))
print(first_10_odds)

# groupby  按条件分组（需要先排序)
data=[("张三","A"),("李四","B"),("王五","A"),("赵六","B")]
data.sort(key=lambda x:x[1])
for key,group in groupby(data,lambda x:x[1]):
    print(f"成绩{key}：",list(group))



