'''
装饰器进阶
带参数装饰器
类装饰器
叠加装饰器
'''
# 带参数的装饰器（如 @retry(max_attempts=3)  装饰器
# 装饰器本身是函数，@decorator(arg)等价于func=decorator(arg)(func)。所以需要三层嵌套
import time
import functools

#带参数的重试装饰器
def retry (max_attempts:int,delay:float=1.0):
    def decortator(func):
        @functools.wraps(func) # 保留原函数的__name__和__doc__
        def wrapper(*args,**kwargs):
            for attempt in range(1,max_attempts+1):
                try:
                    return func(*args,**kwargs)
                except Exception as e:
                    if attempt==max_attempts:
                        raise #最后一次了，直接抛出
                    print(f"第{attempt}次失败：{e},{delay}秒后重试。。。")
                    time.sleep(delay)
            return None
        return wrapper
    return decortator

@retry(max_attempts=3,delay=0.5)
def unstable_api():
    import random
    if random.random()<0.7:
        raise ConnectionError("网络不稳定")
    return "数据获取成功"
print(unstable_api())

# functools.wraps  保留原函数信息
# 不加@functools.wraps(func)时，unstable_api.__name__会变成"wrapper"，文档和函数名都丢了。加了后就保留原名
import functools
def my_decorator(func):
    @functools.wraps(func) # 规则：写装饰器永远加@functools.wraps(func)
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)
    return wrapper
@my_decorator
def say_hello():
    print("hello")
print(say_hello.__name__)
print(say_hello.__doc__)

# 叠加多个装饰器
# @decorator_a
# @decorator_b
# def my_func():
#     pass

import time
import functools
def timer(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        print(f"{func.__name__}耗时{time.time()-start:.4f}s")
        return result
    return wrapper
def logger(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print(f"调用{func.__name__}({args},{kwargs})")
        result=func(*args,**kwargs)
        print(f"{func.__name__}返回{result}")
        return result
    return wrapper

@timer
@logger
def add(a,b):
    return a+b
print(add(1,2))

# 类装饰器
class CountCalls:
    def __init__(self,func):
        functools.update_wrapper(self,func)
        self.func=func
        self.count=0
    def __call__(self, *args, **kwargs):
        self.count+=1
        print(f"{self.func.__name__}被调用了{self.count}次")
        return self.func(*args, **kwargs)
@CountCalls
def say_hello():
    print("hello")
print(say_hello())
print(say_hello())
print(say_hello())

print("\n")
print("阶乘学习：")
# 递归  函数自己调用自己  核心公式：递归=终止条件+分解问题+自我调用
# 阶乘
def factorial(n:int)->int:
    if n<=1:
        return 1
    return n*factorial(n-1)
print(factorial(5))

# 执行过程可视化
def factorial_trace(n:int,depth:int=0)->int:
    indent=" "*depth
    print(f"{indent}→factorial({n})")
    if n<=1:
        return 1
    result=n*factorial_trace(n-1,depth+1)
    print(f"{indent}⬅返回{result}")
    return result
print(factorial_trace(4))

# 递归 VS 迭代
# 递归 代码简洁，但深了会栈溢出
def sum_recursive(n):
    if n<=1:
        return 1
    return n+sum_recursive(n-1)
print(sum_recursive(5))
# 迭代 代码长一点，但不会溢出
def sum_iterative(n):
    total=0
    for i in range(1,n+1):
        total+i
    return total
print(sum_iterative(5))

# 尾递归优化 python默认不支持尾递归优化
# 普通递归（每次都等返回值）
def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)
# 尾递归（计算结果以参数传递，最后一步就是递归调用）
def factorial_tail(n,acc=1):
    if n<=1:
        return acc
    return factorial_tail(n-1,acc*n) # 最后一步就是递归

# python没有尾递归优化，深度递归用迭代或sys.setrecursionlimit


