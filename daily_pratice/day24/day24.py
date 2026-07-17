# Union联合类型注解
# 基础回顾+深入
# python3.10+写法（推荐）
from day13.models import Student


def process(data:int|str)->str:
    if isinstance(data,int):
        return f"数字：{data}"
    return f"字符串：{data}"

# python3.9及以前写法
# from typing import Union
# def process(data:Union[int,str]) -> str:
#     ...

# 类型守卫  拿到来拟合类型后，用isinstance缩窄类型
def describe(value:int|str|list[int])->str:
    if isinstance(value,int):
        return f"整数{value}"
    elif isinstance(value,str):
        return f"字符串，长度{len(value)}"
    else:
        return f"列表，共{len(value)}项"

# typing模块常用类型
from typing import(
Any, #任意类型
Optional, # Optional[int]=int|None
Union, # Union[int,str]=int|str
Literal, # 字面量（只能取特定值）
TypeVar, # 泛型变量
Callable, # 可调用对象（函数类型）
Sequence, # 序列（list、tuple等）
Iterable, # 可迭代对象
TypedDict # 带类型的字典
)

# def set_theme(mode:Literal["light","dark"])->None:
#     ...
# set_theme("dark")
# set_theme("blue") # 类检查器会报错
# # TypedDict 指定字典里每个键的类型
# from typing import TypedDict
# class Student(TypedDict):
#     name:str
#     age:int
#     score:float
# def print_student(s:Student)->None:
#     print(s["name"])
#
# # Callable 函数类型
# # Callable[[参数类型],返回值类型]
# def apply(func:Callable[[int,int],int],a:int,b:int)->int:
#     return func(a,b)

# 类型别名
# 复杂类型起个短名
UserId=int
JsonDict=dict[str,Any]
Callback=Callable[[],None]
StudentList=list[tuple[str,int]]
users:dict[UserId,JsonDict]={
    1:{"name":"张三","age":22},
}

# 设计模式
# 单例模式  全局只有一个实例   数据库连接、日志器、配置对象都应该是单例
class Singleton:
    _instance=None
    def __new__(cls,*args,**kwargs):
        if cls._instance is None:
            cls._instance=super().__new__(cls)
        return cls._instance
class Database(Singleton):
    def __init__(self):
        if not hasattr(self,"connected"):
            self.connected=True
            print("建立数据库连接")
    def query(self,sql:str):
        return f"执行：{sql}"
db1=Database()
db2=Database()
print(db1 is db2)

# 更Pythonic的单例：直接用模块级变量
class Config:
    def __init__(self):
        self.db_host="localhost"
        self.db_port=3306
config=Config() #全局唯一实例

# 工厂模式  根据条件创建不同对象
class Payment:
    def pay(self,amount:float)->str:
        raise NotImplementedError
class AliPay(Payment):
    def pay(self,amount:float)->str:
        return f"支付宝支付{amount}元"
class WeChatPay(Payment):
    def pay(self,amount:float)->str:
        return f"微信支付{amount}元"
def create_payment(method:str)->Payment:
    if method=="alipay":
        return AliPay()
    elif method=="wechat":
        return WeChatPay()
    raise ValueError(f"不支持的支付方式：{method}")
# 使用
p=create_payment("wechat")
print(p.pay(100))

# 观察者模式  事件通知
class EventBus:
    def __init__(self):
        self._handlers:dict[str,list[Callable]]={}
    def on(self,event:str):
        def decorator(handler:Callable)->Callable:
            self._handlers.setdefault(event,[]).append(handler)
            return handler
        return decorator
    def emit(self,event:str,*args,**kwargs):
        for handler in self._handlers.get(event,[]):
            handler(*args,**kwargs)
bus=EventBus()
@bus.on("user_registered")
def send_welcome_email(user):
    print(f"发送欢迎邮件给{user}")
@bus.on("user_registered")
def log_register(user):
    print(f"[日志]新用户注册：{user}")
bus.emit("user_registered","张三")


