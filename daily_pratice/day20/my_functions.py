import re
from urllib.request import proxy_bypass_macosx_sysconf


def clean_text(text:str)->str:
    if not text:
        return ""
    cleaned=' '.join(text.strip().split())
    return cleaned.lower()
# 余额不足异常
class InsufficientBalanceError(Exception):
    pass
class BankAccount:
    def __init__(self,balnace:float=0):
        if balnace<0:
            raise ValueError("初始金额不能为负数")
        self.balance=balnace
    # 存款
    def deposit(self,amount:float)->float:
        if amount<=0:
            raise ValueError("存款金额必须大于0")
        self.balance+=amount
        return self.balance
    # 取款
    def withdraw(self,amount:float)->float:
        if amount<=0:
            raise ValueError("取款金额必须大于0")
        if amount>self.balance:
            raise InsufficientBalanceError(f"余额不足！当前余额：{self.balance}")
        self.balance-=amount
        return self.balance
    # 获取当前金额
    def get_balance(self)->float:
        return self.balance
# 验证邮箱是否正确
def is_valid_email(email:str)->bool:
    if not email:
        return False
    #简单的邮箱验证正则
    pattern=r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern,email))

class TodoList:
    def __int__(self):
        self.tasks=[]
        self._id_counter=1
    #添加任务
    def add(self,title:str)->dict:
        if not title or not title.strip():
            raise ValueError("任务标题不能为空！")
        task={
            "id":self._id_counter,
            "title":title.strip(),
            "done":False
        }
        self.tasks.append(task)
        self._id_counter+=1
        return task
    # 标记完成
    def done(self,task_id:int)->dict:
        task=self._find_task(task_id)
        if task is None:
            raise ValueError(f"任务ID{task_id}不存在")
        task["done"]=True
        return task
    #删除任务
    def delete(self,task_id:int)->bool:
        task=self._find_task(task_id)
        if task is None:
            raise ValueError(f"任务ID{task_id}不存在")
        self.tasks.remove(task)
        return True
    #获取所有任务
    def get_all(self)->list:
        return self.tasks
    #获取未完成的任务
    def get_pending(self)->list:
        return [t for t in self.tasks if not t["done"]]
    #获取已经完成的任务
    def get_done(self)->list:
        return [t for t in self.tasks if t["done"]]
    #查找任务
    def find_task(self,task_id:int):
        for task in self.tasks:
            if task["id"]==task_id:
                return task
        return None


