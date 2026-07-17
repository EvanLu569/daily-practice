# 1. 写一个 @repeat(n) 装饰器，让函数自动执行 n 次
import functools
import time
from typing import get_type_hints


def repeat(n:int):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result=None
            for _ in range(n):
                result=func(*args, **kwargs)
            return result
        return wrapper
    return decorator
@repeat(3)
def say_hello():
    print("hello")
    return "done"
print(say_hello())
# 2. 写一个 @cache_result 装饰器，缓存函数调用结果（相同输入直接返回缓存）
def cache_result(func):
    cache={}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key=(args,tuple(kwargs.items()))
        if key in cache:
            return cache[key]
        print(f"第一次计算：{key}")
        result=func(*args, **kwargs)
        cache[key]=result
        return result
    return wrapper
@cache_result
def expensive_functionn(x,y):
    return x+y
print(expensive_functionn(1, 2))
print(expensive_functionn(1, 2))
print(expensive_functionn(2,1))
print(expensive_functionn(x=1,y=2))

# 3. 写一个 @validate_types 装饰器，用类型注解检查函数参数类型
#    @validate_types
#    def add(a: int, b: int) -> int: ...
#    调用 add("a", 3) 时抛出 TypeError
def validate_types(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        hints=get_type_hints(func)
        all_args={**dict(zip(func.__code__.co_varnames,args)),**kwargs}
        for name,value in all_args.items():
            if name in hints and name!='return':
                if not isinstance(value,hints[name]):
                    raise TypeError(f"参数{name}应为{hints[name].__name__}，实际为{type(value).__name__}")
        result=func(*args,**kwargs)
        if 'return' in hints and not isinstance(result,hints['return']):
            raise TypeError(f"返回值应为{hints['return'].__name__}，实际为{type(result).__name__}")
        return result
    return wrapper

@validate_types
def add(a:int,b:int)->int:
    return a+b
@validate_types
def greet(name:str,age:int)->str:
    return f"{name} is {age} years old"
print(add(1,2))
print(greet("Evan",26))
# 4. 叠加 @timer 和 @logger，观察执行顺序
def timer(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        print(f"调用{func.__name__}耗时{time.time()-start:.4f}秒")
        return result
    return wrapper
def logger(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)
        print(f"调用{func.__name__}返回{result}")
        return result
    return wrapper
@timer
@logger
def add(a,b):
    time.sleep(0.1)
    return a+b
print(add(1,2)) #logger在内，timer在外，先logger在timer

print("\n")
print("递归练习：")
# 1. 用递归求列表所有元素的和
# sum_list([1, 2, 3, 4, 5]) → 15
def sum_list_test(lst):
    if not lst:
        return 0
    return lst[0]+sum_list_test(lst[1:])
sum_list=([1,2,3,4,5])
print(sum_list_test(sum_list))
# 2. 用递归判断一个字符串是否是回文
# is_palindrome("racecar") → True
def is_palindrome(s):
    return True if len(s)<=1 else s[0]==s[-1]and is_palindrome(s[1:-1])
s="racecar"
print(is_palindrome(s))
# 3. 用递归展平嵌套列表
# flatten([1, [2, [3, 4], 5], 6]) → [1, 2, 3, 4, 5, 6]
def flatten(t):
    result=[]
    for i in t:
        result+=flatten(i) if isinstance(i,list) else [i]
    return result
print(flatten([1,[2,[3,4],5],6]))
# 4. 用递归实现汉诺塔（打印移动步骤）
# hanoi(3, "A", "B", "C") → 打印所有移动步骤
def hanoi(n,source,target,anxiliary):
    if n==1:
        print(f"{source}->{target}")
        return
    hanoi(n-1,source,anxiliary,target)
    print(f"{source}->{target}")
    hanoi(n-1,anxiliary,target,source)
print(hanoi(2,"A","B","C"))
# 5. 用带缓存的递归计算第 50 个斐波那契数（@lru_cache）
from functools import lru_cache
@lru_cache(maxsize=None)
def fib(n):
    return n if n<=1 else fib(n-1)+fib(n-2)
print(fib(50))









