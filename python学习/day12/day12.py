'''
def 装饰器名(func):
    def wrapper(*args,**kwargs):
        # 执行前做点什么
        result=func(*args,**kwargs)
        # 执行后做点什么
        return result
    return wrapper
@装饰器名
def 某函数():
    ...
'''
import time  # 导入时间模块，用来计算耗时


# 定义装饰器：timer 是一个“工厂函数”，它接收被装饰的函数作为参数
def timer(func):
    # wrapper 是“包装函数”，它会在原函数调用前后插入额外代码
    def wrapper(*args, **kwargs):
        # *args 和 **kwargs 用来接收任意参数，确保能传给任何原函数
        start = time.time()  # 记录开始时间
        result = func(*args, **kwargs)  # 真正调用原函数，并保存返回值
        end = time.time()  # 记录结束时间
        # 打印运行耗时，{func.__name__} 是原函数的名字
        print(f"函数 {func.__name__} 运行耗时: {end - start:.4f}秒")
        return result  # 必须返回原函数的返回值，否则调用者拿不到结果
    return wrapper  # 装饰器必须返回包装函数
# @timer 相当于执行 sleep_demo = timer(sleep_demo)
@timer
def sleep_demo():
    time.sleep(1)  # 模拟耗时操作，暂停1秒
    print("我睡醒了")
# 调用时，实际执行的是 wrapper，但看起来就像直接调用原函数
sleep_demo()

# 日志装饰器
def log(func):
    def wrapper(*args, **kwargs):
        print(f"日志正在调用{func.__name__}")
        print(f"参数：args={args},kwargs={kwargs}")
        # 执行原函数，拿到结果
        result = func(*args, **kwargs)
        # 调用后打印返回结果
        print(f"日志{func.__name__}执行完毕，返回：{result}")
        return result
    return wrapper
@log
def add(a:int, b:int):
    return a + b
@log
def greet(name, msg="您好"):
    return f"{msg},{name}！"
# 调用调试
add(1,2)
greet("evan", msg="欢迎")

