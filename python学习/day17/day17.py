'''
dataclass 少写样板代码
python3.7+引入，定义一个数据类只需要写属性，省掉__init__、__str__、__eq__这些固定套路
'''
from dataclasses import dataclass,field
# 普通类写法
class StudentOld:
    def __init__(self,name:str,age:int,score:int=0):
        self.name=name
        self.age=age
        self.score=score
# dataclass写法，自动生成__init__、__str__、__eq__
@dataclass
class Student:
    name:str
    age:int
    score:int=0
s1=Student("zhangsan",20,98)
s2=Student("zhangsan",20,98)
print(s1)
print(s1==s2)
print(s1.name)

# filed 控制字段行为
from dataclasses import dataclass,field
@dataclass
class TodoList:
    title:str
    tasks:list[str]=field(default_factory=list)
    created_at:str=""
    def __post_init__(self):
        from datetime import datetime
        if not self.created_at:
            self.created_at=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
t1=TodoList("学习计划")
t1.tasks.append("背书")
print(t1)

print("\n")

'''
正则表达式基础
正则表达式是文本处理的终极武器，表单验证、日志分析、数据清洗全用它
'''
import re
text = "我的电话是 13812345678，备用 18900001111。"
# 查找所有匹配
phones=re.findall(r"\d{11}",text)
print(phones)

# 查找第一个匹配
match=re.search(r"\d{11}",text)
print(match.group())

#替换
masked=re.sub(r"\d{11}","***隐藏***",text)
print(masked)

# 判断是否完全匹配（用于表单验证）
if re.fullmatch(r"\d{11}","13812345678"):
    print("合法的手机号")
if not re.fullmatch(r"\d{11}","13812345678"):
    print("不合法的手机号")

'''
\d 数字
\w 字母/数字/下划线
\s 空白字符
.  任意字符
+  1个或多个
*  0个或多个
？ 0或1个
[abc] a或b或c
[^abc] 不是a/b/c
^  开头
$ 结尾
() 分组提取
| 或
'''
import re
# 1.验证邮箱
def is_valid_email(email:str)->bool:
    pattern=r"[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return bool(re.fullmatch(pattern,email))
print(is_valid_email("test@qq.com"))
print(is_valid_email("not-an-email"))

# 2.提取URL
text = "官网 https://www.baidu.com 和 https://github.com 都可以访问"
urls = re.findall(r"https?://[\w\./-]+", text)
print(urls)

# 3. 提取日期并转换格式
text = "2024-01-15 发布，2024-06-30 到期"
dates = re.findall(r"(\d{4})-(\d{2})-(\d{2})", text)
for year, month, day in dates:
    print(f"{year}年{month}月{day}日")


