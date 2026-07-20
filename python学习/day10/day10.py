'''
类型注释  让代码更规范
'''
# 1.基础语法
# 变量注解：变量名：类型=值
# 类型注解只是提示，python不会强制检查，即使传错类型，代码照样跑
name:str="zhangsan"
age:int=22
score:float=98.5
is_student:bool=True
skills:list=["python","SQL"]
# 函数注解：参数和返回值都标注
def add(a:int,b:int)->int:
    return a+b
def greet(name:str)->str:
    return f"您好，{name}"
print(add(1,2))
print(greet("lisi"))

# 2.复合类型
# 列表里装什么类型
nums:list[int]=[1,2,3]
names:list[str]=["zhangsan","lisi","wangwu"]
# 字典的键和值各是什么类型
scores:dict[str,int]={"zhangsan":99,"lisi":100}
# 复杂嵌套
students:list[dict[str,int]]=[
    {"zhangsan":88},
    {"lisi":87}
]

# 可选类型  可能为None
def find_user(user_id:int)->dict|None:
    if user_id==1:
        return {"name":"zhangsan","age":23}
    return None
# 3.用在类里面
class Task:
    total:int=0
    def __init__(self,title:str)->None:
        self.title=title
        self.done=False
        Task.total+=1
    def mark_done(self)->None:
        self.done=True
    def __str__(self)->None:
        status="√"if self.done else "⭕"
        return f"{status} {self.title}"
class TodoList:
    def __init__(self,filename:str)->None:
        self.filename=filename
        self.tasks:list[Task]=[]
    def add(self,title:str)->None:
        self.tasks.append(Task(title))
    def get_task(self,index:int)->None:
        if 0<=index<len(self.tasks):
            return self.tasks[index]
        return None

