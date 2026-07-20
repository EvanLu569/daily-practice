# 1. 用 lru_cache 优化你的 fibonacci 函数，分别测试 n=35 时有无缓存的耗时差异
from functools import lru_cache
import time

from day14.day14 import count


@lru_cache(maxsize=128)
def fibonacci(n:int)->int:
    if n<=1:
        return n
    return fibonacci(n-1)+fibonacci(n-2)
# 有缓存
start=time.time()
print(fibonacci(35))
print(f"有缓存耗时：{time.time() - start:.4f} 秒")
# 2. 用 reduce 实现自定义的 deep_get(data, keys) 函数
#    data = {"a": {"b": {"c": 42}}}
#    deep_get(data, ["a", "b", "c"]) → 42
from functools import reduce
def deep_get(data,keys):
    return reduce(lambda d,key:d[key],keys,data)
data = {"a": {"b": {"c": 42}}}
print(deep_get(data, ["a", "b", "c"]))
# 3. 用 combinations 列出从 6 个人中选 3 人组成小组的所有方案
from itertools import combinations
print(list(combinations("ABCDEF",3)))
# 4. 用 chain 把三个列表 [1,2,3]、[4,5,6]、[7,8,9] 合并成一个迭代器并遍历
from itertools import chain
print(list(chain([1,2,3],[4,5,6],[7,8,9])))
# 5. 用 islice 从一个无限生成器中截取前 20 个能被 3 整除的数
from itertools import islice,count
result=list(islice((i for i in count()if i%3==0),20))
print(result)














