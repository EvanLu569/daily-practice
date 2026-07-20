'''
@property  让方法像属性一样使用
'''
class Person:
    def __init__(self,first:str,last:str):
        self.first=first
        self.last=last
    @property
    def full_name(self)->str:  #当成属性用，不加括号
        return f"{self.first}{self.last}"
    @property
    def age(self)->int:
        return self._age
    @age.setter
    def age(self,value:int):
        if value<0:
            raise ValueError("年龄不能为负数")
        self._age=value
p=Person("zhang","san")
print(p.full_name)
p.age=22
print(p.age)

# @classmmethod和@staticmethod
class Student:
    school="北大"
    def __init__(self,name:str):
        self.name=name
    def say_hello(self):
        print(f"我是{self.name}")
    @classmethod
    def change_school(cls,new_name:str):
        cls.school=new_name
    @classmethod
    def from_string(cls,text:str):
        name,age,score=text.split(",")
        return cls(name)
    @staticmethod
    def is_valid_name(name:str)->bool:
        return len(name)>=2 and len(name)<=20
# 类方法
Student.change_school("深大")
print(Student.school)

# 工厂方法
s=Student.from_string("张三,20,95")
print(s.name)

# 静态方法
print(Student.is_valid_name("张"))
print(Student.is_valid_name("张三"))

