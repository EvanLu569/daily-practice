#  Day 7：综合复习 — 待办事项管理器（TODO List）
import sys

# 文件读取
def load_tasks(filename):
    try:
        with open(filename,"r",encoding="utf-8")as f:
            lines=f.readlines()
    except FileNotFoundError:
        return []

    tasks=[]
    for line in lines:
        line=line.strip() #去掉换行符
        if not line: # 跳过空行
            continue
        parts=line.rsplit("|",1) # 从右边切一次，得到[标题，状态]
        title=parts[0]
        done=parts[1]=="done" if len(parts)>1 else False
        tasks.append({"title":title,"done":done})
    return tasks

# 保存任务
def save_tasks(tasks,filename):
    with open(filename,"w",encoding="utf-8")as f:
        for task in tasks:
            status="done" if task["done"] else "todo"
            f.write(f"{task["title"]}|{status}\n")
# 显示任务
def show_tasks(tasks):
    if not tasks:
        print("暂无任务")
        return
    print("="*8)
    print("代办事项")
    print("="*8)
    for i,task in enumerate(tasks,start=1):
        status="√" if task["done"] else "⭕"
        print(f"{i}.{status} {task["title"]}")

    print("="*8)

# 添加任务
def add_tasks(tasks,title):
    tasks.append({"title":title,"done":False})
    print(f"已添加：{title}")

# 标记完成
def mark_done(tasks,index):
    if 0<=index<len(tasks):
        tasks[index]["done"]=True
        print(f"已完成：{tasks[index]["title"]}")
    else:
        print(f"任务序号{index+1}不存在。")

# 删除任务
def delete_task(tasks,index):
    if 0<=index<len(tasks):
        title=tasks[index]["title"]
        tasks.pop(index)
        print(f"已删除：{title}")
    else:
        print(f"任务序号{index+1}不存在。")


if __name__=="__main__":
    filename="tasks.txt"
    tasks=load_tasks(filename)

    if len(sys.argv)<=1:
        show_tasks(tasks)
    elif sys.argv[1]=="add":
        if len(sys.argv)>2:
            add_tasks(tasks,sys.argv[2])
            save_tasks(tasks,filename)
            show_tasks(tasks)
        else:
            print("用法：python todo.py add \"任务名\"")
    elif sys.argv[1]=="done":
        if len(sys.argv)>2:
            index=int(sys.argv[2])-1
            mark_done(tasks,index)
            save_tasks(tasks,filename)
            show_tasks(tasks)
        else:
            print("用法：python todo.py done \"任务名\"")
    elif sys.argv[1]=="del":
        if len(sys.argv)>2:
            index=int(sys.argv[2])-1
            delete_task(tasks,index)
            save_tasks(tasks,filename)
            show_tasks(tasks)
        else:
            print("用法：python todo.py del \"任务名\"")

