'''
面向对象（一）  类和对象是什么
类（class）：造车的图纸   模板
对象（object）：按图纸造出来的真车  具体的东西
'''
# 1.定义一个最简单的类
class Dog:
    def bark(self): #self代表当前这个对象本身，必须写，但调用时不用管它
        print("汪汪！")
# 用这个类创造对象
my_dog=Dog() # 实例化
print(type(my_dog))
my_dog.bark()

# 2.加属性  __init__构造函数   __init__就是初始化函数
# 每只狗都有不同的名字和年龄，要在创建对象时传进去
class Dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def bark(self):
        print(f"我是{self.name},今年{self.age}岁。")
    def birthday(self):
        self.age+=1
        print(f"{self.name}长了一岁，现在{self.age}岁了！")
#创建对象是传入参数
dog1=Dog("旺财",3)
dog2=Dog("小白",1)

dog1.bark()
dog2.bark()

dog1.birthday()
dog1.bark()

# 3.给类加更多方法  模拟一个待办任务
# 把之前TODO里的任务变成类，让逻辑更清晰
class Task:
    def __init__(self,title):
        self.title=title
        self.done=False
    def mark_done(self):
        self.done=True
    def undo(self):
        self.done=False
    def show(self,number):
        status="√" if self.done else "⭕"
        print(f"{number}.{status} {self.title}")
t1=Task("背书")
t2=Task("刷题")
t3=Task("写作业")

t2.mark_done()
tasks=[t1,t2,t3]
for i,t in enumerate(tasks,start=1):
    t.show(i)

# 4.类变量VS实例变量
class Task:
    total=0 # 类变量 所有对象共享，统计创建了多少个任务
    def __init__(self,title):
        self.title=title
        self.done=False
        Task.total+=1
t4=Task("写代码")
t5=Task("背八股文")
print(Task.total) # 用类名也能访问
print(t4.total)   # 用对象也能访问

# 5. __str__  让print对象更有意义
# __str__的作用：当print(对象)时，python自动调用这个方法，当它返回的字符串打印出来，不用再手动写show()这些方法了
class Task:
    total=0 # 类变量 所有对象共享，统计创建了多少个任务
    def __init__(self,title):
        self.title=title
        self.done=False
        Task.total+=1
    def mark_done(self):
        self.done=True
    def __str__(self):
        status="√" if self.done else "⭕"
        return f"{status} {self.title}"
t1 = Task("背八股文")
t2 = Task("刷力扣5题")
print(Task.total)

# 6.继承  子类复用父类代码
# 面向对象最重要的特性，FastAPI，SQLAlchemy全在用它
# 父类:普通任务
class Task:
    def __init__(self,title):
        self.title=title
        self.done=False
    def mark_done(self):
        self.done=True
    def __str__(self):
        status="√"if self.done else "⭕"
        return f"{status} {self.title}"

# 子类：带优先级的任务  继承Task的全部功能，再加新东西
class PriorityTask(Task):
    def __init__(self,title,priority):
        super().__init__(title) #调用父类的__init__，设置title和done
        self.priority=priority #新增：优先级属性
    def __str__(self):
        stars="*"*self.priority
        return f"{super().__str__()} {stars}" #复用父类的__str__，再拼上星星
t1 = Task("背八股文")
t2=PriorityTask("一个小时背书",3)
print(t1)
print(t2)
t2.mark_done()
print(t2)

print(isinstance(t2,Task))
print(isinstance(t2,PriorityTask))

