# 1. 用 dataclass 重写 Book 类（title, author, year, isbn）
from dataclasses import dataclass
@dataclass
class Book:
    title:str
    author:str
    year:int
    isbn:str
b1=Book("活着","余华",2000,"xxxxxxxxx")
print(b1)
# 2. 用 dataclass 写一个 Point 类（x, y），写函数计算两点距离
from dataclasses import  dataclass
@dataclass
class Point:
    x:int
    y:int
def distance(a:Point,b:Point):
    import math
    return math.sqrt((a.x-b.x)**2+(a.y-b.y)**2)
p1=Point(0,0)
p2=Point(3,4)
print(distance(p1,p2))
# 3. 用 dataclass + field(default_factory) 写一个 ShoppingCart 类（owner, items）
#    items 默认为空列表，添加 add_item(商品名, 价格) 方法
from dataclasses import dataclass,field
@dataclass
class ShoppingCart:
    owner:str
    items:list[str]=field(default_factory=list)
    def add_item(self,name:str,price:float):
        self.items.append((name,price))
    def total(self)->float:
        return sum(price for _,price in self.items)
cart=ShoppingCart("张三")
cart.add_item("书包",199.9)
print(cart)
print(cart.total())


# 1. 验证是否是合法的中国大陆手机号（1 开头，11 位数字）
import re
def is_valid_phone(phone: str) -> bool:
  pattern = r"1\d{10}"
  return bool(re.fullmatch(pattern, phone))
print(is_valid_phone("13812345678"))   # True
print(is_valid_phone("123"))           # False（太短）
print(is_valid_phone("23812345678"))   #
# 2. 从 "价格：¥99.99 元，优惠价：¥79.00 元" 中提取所有金额数字
import re
text = "价格：¥99.99 元，优惠价：¥79.00 元"
prices = re.findall(r"¥(\d+\.\d{2})", text)
print(prices)  # ['99.99', '79.00']
# 3. 验证密码强度：至少8位，包含大小写字母和数字，用正则判断
import re
def is_strong_password(pwd: str) -> bool:
    if len(pwd) < 8:
        return False
    if not re.search(r"[a-z]", pwd):
        return False
    if not re.search(r"[A-Z]", pwd):
        return False
    if not re.search(r"\d", pwd):
        return False
    return True
print(is_strong_password("Abc12345"))
print(is_strong_password("abc12345"))
print(is_strong_password("ABCDEFGH"))
print(is_strong_password("Ab1"))
# 4. 把 "2024-01-15" 批量替换成 "15/01/2024" 格式
import re
text = "发布于 2024-01-15，截止 2024-06-30"
result = re.sub(r"(\d{4})-(\d{2})-(\d{2})",r"\3/\2/\1", text)
print(result)
# 5. 从网页源码 <a href="/article/123">标题</a> 中提取所有链接的路径（/article/123）
import re
html = '<a href="/article/123">标题1</a> <ahref="/article/456">标题2</a> <ahref="/news/789">新闻</a>'
paths = re.findall(r'href="([^"]+)"', html)
print(paths)   # ['/article/123', '/article/456','/news/789']

