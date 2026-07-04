'''
模块和包
为什么要分文件？  不可能把所有的代码都写到一个文件里面，真正的项目里面有几十几百个文件
'''
# 从文件读取任务列表
def load_tasks(filename):
    tasks=[]
    try:
        with open(filename,"r",encoding="utf-8") as f:
            for line in f:
                line=line.strip()
                if not line:
                    continue
                parts=line.rsplit("|",1)
                title=parts[0]
                done=parts[1]=="done"if len(parts)>1 else False
                tasks.append({"title":title,"done":done})
    except FileNotFoundError:
        pass
    return tasks
#保存任务列表到文件
def save_tasks(tasks,filename):
    with open(filename,"w",encoding="utf-8") as f:
        for task in tasks:
            status="done"if task["done"]else "todo"
            f.write(f"{task['title']}|{status}\n")
#打印所有任务
def show_tasks(tasks):
    if not tasks:
        print("暂无任务")
    print("*"*10)
    for i,task in enumerate(tasks,start=1):
        status="√"if task["done"]else "⭕"
        print(f"{i}.{status} {task['title']}")
    print("*"*10)









