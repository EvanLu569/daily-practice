# 1. 给 BankAccount 类加 @property：balance 变成属性，且不允许直接设负数
import json


class BankAccount:
    def __init__(self,balance:float):
        self.balance=balance
    @property
    def balance(self)->float:
        return self._balance
    @balance.setter
    def balance(self,value:float):
        if value<0:
            raise ValueError("金额不能为负数")
        self._balance=value
# 2. 给 Task 类加 @property：title 只读，done 可读写
class Task:
    def __init__(self,title:str,done:bool=False):
        self._title=title
        self.done=done
    @property
    def title(self)->str:
        return self._title
    @property
    def done(self)->bool:
        return self._done
    @done.setter
    def done(self,value:bool):
        self._done=value
# 3. 给 Rectangle 类加 @property area（面积）和 perimeter（周长），通过宽高自动计算
class Rectangle:
    def __init__(self,width:float,height:float):
        self._width=width
        self._height=height
    @property
    def area(self)->float:
        return self._width*self._height
    @property
    def perimeter(self)->float:
        return (self._width+self._height)*2
# 4. 写一个 @classmethod 工厂方法：User.from_json(json_str: str)
# 从 JSON 字符串创建用户
class User:
    def __init__(self,name:str,age:int,email:str):
        self.name=name
        self.age=age
        self.email=email
    def __str__(self):
        return f"{self.name},{self.age}岁,{self.email}"
    @classmethod
    def from_json(cls,json_str:str):
        data=json.loads(json_str)
        return cls(data["name"],data["age"],data["email"])
json_str = '{"name": "张三", "age": 25, "email":"zhangsan@qq.com"}'
u=User.from_json(json_str)
print(u)
# 5. 写一个 @staticmethod 验证函数：is_valid_password(pwd: str) 返回 True/False
#    密码要求：长度 >= 8，包含数字和字母
@staticmethod
def is_valid_password(pwd: str)->bool:
    if len(pwd)<8:
        return False
    has_digit=any(c.isdigit()for c in pwd)
    has_alpha=any(c.isalpha()for c in pwd)
    return has_digit and has_alpha
print(is_valid_password("abc12345"))
print(is_valid_password("12345678"))
























