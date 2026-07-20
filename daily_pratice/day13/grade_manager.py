'''
把你学过的所有东西融合在一起：写一个 **命令行学生成绩管理器**。
python grade_manager.py add 张三 计算机 90
python grade_manager.py add 李四 计算机 85
python grade_manager.py add 王五 数学 95
python grade_manager.py list               # 列出所有成绩
python grade_manager.py avg 计算机          # 计算某科目的平均分
python grade_manager.py top 3              # 显示总分前3名

要求
- 用**类**封装 `Student` 和 `GradeManager`
- 用**文件**持久化数据（存到 `grades.txt`）
- 用**类型注解**标注所有函数
- 用**推导式**做数据筛选和统计
- 用 **sorted + lambda** 排序
- 程序拆成两个文件：`models.py`（类定义）和 `grade_manager.py`（主逻辑），互相 **import**
- 主逻辑用 `if __name__ == "__main__"` 保护

数据存储格式:
张三|计算机|90
李四|计算机|85
王五|数学|95
张三|数学|88
'''
import sys
from models import Student,GradeManager
def main():
    if len(sys.argv)<2:
        print("用法：python grade_manager.py <命令>[参数...]")
        return
    gm=GradeManager("grades.txt")
    command=sys.argv[1]
    if command=="add":
        name=sys.argv[2]
        subject=sys.argv[3]
        score=int(sys.argv[4])
        s=Student(name,subject,score)
        gm.add(s)
        print(f"添加成功{s}")
    elif command=="list":
        gm.list_all()
    elif command=="avg":
        subject=sys.argv[2]
        avg_score=gm.avg(subject)
        print(f"{subject}平均分：{avg_score:.2f}")
    elif command=="top":
        n=int(sys.argv[2])
        gm.top(n)

if __name__=="__main__":
    main()