# Day 8 综合练习：用面向对象重写 TODO 管理器
class Task:
    def __init__(self,title):
        self.title=title
        self.done=False
    def mark_done(self):
        self.done=True
    def undo(self):
        self.done=False
    def __str__(self):
        status="√"if self.done else "⭕"
        return f"{status} {self.title}"
# 任务管理器
class TodoList:
    def __init__(self,filename):
        self.filename=filename
        self.tasks=[]
        self.load()
    def load(self):
        try:
            with open(self.filename,"r",encoding="utf-8") as f:
                for line in f:
                    line=line.strip()
                    if not line:
                        continue
                    parts=line.rsplit("|",1)
                    title=parts[0]
                    is_done=parts[1]=="done"if len(parts)>1 else False
                    task=Task(title)
                    if is_done:
                        task.mark_done()
                    self.tasks.append(task)
        except FileNotFoundError:
            self.tasks=[]

    # 保存任务到文件
    def save(self):
        with open(self.filename,"w",encoding="utf-8") as f:
            for task in self.tasks:
                status="done"if task.done else "todo"
                f.write(f"{task.title}|{status}\n")
    # 增加任务
    def add(self,title):
        task=Task(title)
        self.tasks.append(task)
        print(f"已添加{title}")
    # 标记完成
    def done(self,index):
        if 0<=index<len(self.tasks):
            self.tasks[index].mark_done()
            print(f"已完成：{self.tasks[index].title}")
    # 删除任务
    def delete(self,index):
        if 0<=index<len(self.tasks):
            title=self.tasks[index].title
            self.tasks.pop(index)
            print(f"已删除：{title}")
    # 显示所有任务
    def show(self):
        if not self.tasks:
            print("暂无任务")
            return
        print("*"*10)
        print("待办事项")
        print("*"*10)
        for i,task in enumerate(self.tasks,start=1):
            print(f"{i}.{task}")
        print("*"*10)
# 主程序
if __name__=="__main__":
    import sys
    app=TodoList("tasks.txt")

    if len(sys.argv)<=1:
        app.show()
    elif sys.argv[1]=="add" and len(sys.argv)>2:
        app.add(sys.argv[2])
        app.save()
        app.show()
    elif sys.argv[1]=="done" and len(sys.argv)>2:
        app.done(int(sys.argv[2])-1)
        app.save()
        app.show()
    elif sys.argv[1]=="del" and len(sys.argv)>2:
        app.delete(int(sys.argv[2])-1)
        app.save()
        app.show()
    else:
        print("用法：")
        print('  python todo_oop.py')
        print('  python todo_oop.py add "任务名"')
        print('  python todo_oop.py done 序号')
        print('  python todo_oop.py del 序号')

