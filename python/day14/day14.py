'''
自定义异常  当内置异常不够用时，自己定义异常类型
'''
from day13.models import Student


# 余额不足异常
class InsufficientBalanceError(Exception):
    def __init__(self,balance:float,amount:float)->None:
        self.balance=balance
        self.amount=amount
        super().__init__(f"余额{balance}元，无法取出{amount}元")

# 邮箱格式错误
class InvalidEmailError(ValueError):
    pass

# 使用自定义异常
def withdraw(balance:float,amount:float)->None:
    if amount>balance:
        raise InsufficientBalanceError(balance,amount) # raise抛异常
    return balance-amount

# finally  无论是否异常都会执行的代码块，用于清理资源（关闭文件、断开连接等）
f=None
try:
    f=open("data.txt","r")
    content=f.read()
except FileNotFoundError:
    print("文件不存在")
finally:
    if f:
        f.close()

# with语句：上下文管理器  with open(...)自动帮助关闭文件，你也可以给自己的类加上这个能力
class Database:
    def __init__(self,name:str):
        self.name=name
    def __enter__(self):
        print(f"连接数据库{self.name}...")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"断开数据库 {self.name}。")
        return False
    def query(self,sql:str)->str:
        return f"执行了：{sql}"
# 使用
with Database("学生库") as db:
    print(db.query("SELECT * FROM students"))

# collections模块  高级数据机构
# 面试和刷题里，collections模块里的数据机构能省掉大量代码
# namedtuple  有名字的元组
from collections import namedtuple
# 定义一个轻量级”类“
Student=namedtuple("Student",["name","age","score"])
s1=Student("张三",20,99)
print(s1.name)
print(s1[0])
print(s1.score)

# defaultdict 有默认的字典
# 普通字典访问不存在的key会报错，defaultdict自动给默认值
from collections import defaultdict
# 普通字典的痛点
word_count={}
for word in ["a","b","a","c","b","a"]:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1
# defaultdict一步到位
word_count=defaultdict(int)  # 不存在的key默认为0
for word in ["a","b","a","c","b","a"]:
    word_count[word]+=1
print(dict(word_count))

# 分组常用
students_by_grade=defaultdict(list)
for name,grade in  [("张三", "A"), ("李四", "B"), ("王五", "A")]:
    students_by_grade[grade].append(name)
print(dict(students_by_grade))

# counter 计数器  统计频率的专用工具
from collections import Counter
words=["a", "b", "a", "c", "b", "a"]
count=Counter(words)
print(count)

# 最常用的3个方法
print(count.most_common(2))
print(count["z"])
print(list(count.elements()))

# 数学运算
c1=Counter(a=3,b=1)
c2=Counter(a=2,b=2)
print(c1+c2)
print(c1-c2)

# deque 双端队列
# 列表在头部插入很慢（O(n)），deque 头部和尾部插入删除都是 O(1)
from collections import deque
q=deque([1,2,3])
print(q)
q.append(4)
print(q)
q.appendleft(0)
print(q)
q.pop()
print(q)
q.popleft()
print(q)
# 限制长度 超出时自动扔掉旧的
history=deque(maxlen=3)
history.append("第1条")
history.append("第2条")
history.append("第3条")
history.append("第4条")
print(history)
