'''
  练习：写一个完整的银行取款程序。
  # 要求：
  # 1. 定义自定义异常
  InsufficientBalanceError（余额不足）
  # 2. 定义自定义异常
  NegativeAmountError（金额不能为负数）
  # 3. 写 BankAccount 类：
  #    - __init__(owner, balance)
  #    - withdraw(amount) → 可能抛出上面两种异常
  #    - __str__ → 返回 "xxx 的余额：xxx 元"
  # 4. 写测试代码，依次触发两种异常并捕获
'''
import math


# 要求：
# 1. 定义自定义异常
class InsufficientBalanceError(Exception):
    def __init__(self,balance:float,amount:float):
        self.balance=balance
        self.amount=amount
        super().__init__(f"余额{balance}元，无法取出{amount}元")
# 2. 定义自定义异常
class NegativeAmountError(Exception):
    pass
# 3. 写 BankAccount 类：
#    - __init__(owner, balance)
#    - withdraw(amount) → 可能抛出上面两种异常
#    - __str__ → 返回 "xxx 的余额：xxx 元"
class BankAccount:
    def __init__(self,owner:str,balance:float=0):
        self.owner=owner
        self.balance=balance
    def withdraw(self,amount:float):
        if amount<0:
            raise NegativeAmountError(f"取款余额不能为负数：{amount}")
        if amount>self.balance:
            raise InsufficientBalanceError(self.balance,amount)
        self.balance-=amount
        return self.balance
    def __str__(self):
        return f"{self.owner}的余额：{self.balance}元"
# 4. 写测试代码，依次触发两种异常并捕获
acc = BankAccount("张三", 1000)
print(acc.withdraw(300))
try:
    acc.withdraw(-100)
except NegativeAmountError as e:
    print(f"捕获异常：{e}")
try:
  acc.withdraw(2000)
except InsufficientBalanceError as e:
  print(f"捕获异常：{e}")

# 1. 用 Counter 统计一个字符串中出现次数前三的字符
from collections import Counter
text = "abracadabra"
count=Counter(text)
print(count.most_common(3))
# 2. 用 defaultdict 实现分组：把 ["apple", "ant", "banana", "cat", "bird", "bear"]
#    按首字母分组 → {"a": ["apple", "ant"], "b": ["banana", "bird", "bear"], "c": ["cat"]}
from collections import defaultdict
ch=["apple", "ant", "banana", "cat", "bird", "bear"]
group_ch=defaultdict(list)
for word in ch:
    group_ch[word[0]].append(word)
print(dict(group_ch))
# 3. 用 namedtuple 表示坐标点 (x, y)，写一个函数计算两点距离
from collections import namedtuple
import math
Point=namedtuple("Point",["x","y"])
p1=Point(0,0)
p2=Point(3,4)
def distance(a,b):
    return math.sqrt((b.x-a.x)**2+(b.y-a.y)**2)
print(distance(p1,p2))
# 4. 用 deque 模拟浏览器前进后退（只保留最近 5 个页面）
from collections import deque
history=deque(maxlen=5)
history.append("百度")
history.append("知乎")
history.append("B站")
history.append("抖音")
history.append("小红书")
history.append("番茄")
print(history)
# 5. 用 Counter 的加减运算，找出两个字符串的共同字符和差异字符
from collections import Counter
text_a = "hello"
text_b = "world"
t1=Counter(text_a)
t2=Counter(text_b)
print(t1+t2)
print(t1-t2)
print(t1&t2)








