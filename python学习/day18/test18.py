# # 1. 读取一个 JSON 文件（自己创建），筛选出 score > 80 的学生
# import json
# students={
#     "name":"lisi",
#     "subject":"English",
#     "score":100
# }
# try:
#     with open("students.json","w",encoding="utf-8")as f:
#         json.dump(students,f,ensure_ascii=False,indent=2)
#     with open("students.json","r",encoding="utf-8")as f:
#         content=json.load(f)
#         if content.get("score",0)>80:
#             print(f"{content['name']}-{content['score']}  超过了80分")
# except FileNotFoundError:
#     print("文件不存在，请检查路径")
# except json.JSONDecodeError:
#     print("JSON格式错误，请检查文件内容")
# # 2. 把之前的 TODO 任务保存为 JSON 格式，读写都要实现
# import json
# tasks=[
#     {"id":1,"title":"reading","done":False},
#     {"id":2,"title":"writing","done":False},
#     {"id":3,"title":"dancing","done":True}
# ]
# try:
#     with open("tasks.json","w",encoding="utf-8")as f:
#         json.dump(tasks,f,ensure_ascii=False,indent=2)
#     print("已保存")
#     with open("tasks.json","r",encoding="utf-8")as f:
#         loaded=json.load(f)
#         for t in loaded:
#             print(f"[{'√'if t['done']else ' '}]{t['title']}")
# except FileNotFoundError:
#     print("文件不存在，请检查路径")
# except json.JSONDecodeError:
#     print("JSON格式错误，请检查文件内容")
# # 3. 把 CSV 数据中的 "分数" 列取出来，计算平均值、最大值、最小值
# import csv
# scores=[]
# try:
#     with open("students.csv","r",newline="",encoding="utf-8-sig")as f:
#         reader=csv.DictReader(f)
#         for row in reader:
#             score = float(row["score"])
#             scores.append(score)
#     if scores:
#         avg=sum(scores)/len(scores)
#         maximum=max(scores)
#         minimum=min(scores)
#         print(f"平均分{avg}")
#         print(f"最高分{maximum}")
#         print(f"最低分{minimum}")
# except FileNotFoundError:
#     print("文件不存在，请检查路径")
# except json.JSONDecodeError:
#     print("JSON格式错误，请检查文件内容")
# # 4. 模拟 API 返回：把 requests.get() 获取的 JSON 数据解析后存为 CSV
# import json
# import csv
# import requests
# from datetime import datetime
# def get_api_data():
#     try:
#         responses=requests.get("https://api.github.com/users/zhang san")
#         return responses.json()
#     except:
#         print("API请求失败，使用模拟数据")
#         return [
#             {"id": 1, "name": "张三", "age": 25, "score": 85},
#             {"id": 2, "name": "李四", "age": 23, "score": 92},
#             {"id": 3, "name": "王五", "age": 24, "score": 78},
#             {"id": 4, "name": "赵六", "age": 22, "score": 95},
#             {"id": 5, "name": "孙七", "age": 26, "score": 88}
#         ]
# def save_json_to_csv(json_data,csv_filename="output.csv"):
#     if not json_data:
#         print("没有数据！")
#         return
#     fieldnames=json_data[0].keys()
#     with open(csv_filename,"w",newline="",encoding="utf-8-sig")as f:
#         writer=csv.DictWriter(f,fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(json_data)
#     print(f"已保存{len(json_data)}条数据到{csv_filename}")
# if __name__=="__main__":
#     data=get_api_data()
#     print(f"获取到{len(data)}条数据")
#     save_json_to_csv(data)
#
#
# 1. 用 pathlib 创建目录结构 project/src、project/tests、project/data
from pathlib import Path
base_dir=Path("project")
subdirs=["src","tests","data"]
# 法一：逐一创建
for subdir in subdirs:
    (base_dir/subdir).mkdir(parents=True, exist_ok=True)
# 法二：一次性创建多个
roads=[base_dir/subdir for subdir in subdirs]
for road in roads:
    road.mkdir(parents=True, exist_ok=True)
print("创建的目录：")
for subdir in subdirs:
    path=base_dir/subdir
    print(f"{path}(存在：{path.exists()})")
# 2. 用 glob 找出当前目录下所有 .txt 文件，打印文件名和大小
from pathlib import Path
for text_file in Path(".").glob("*.txt"):
    size=text_file.stat().st_size
    print(f"{text_file} -{size}字节（{size/1024:.2f}）KB")
# 3. 用 rglob 递归找出所有 .py 文件，统计总行数
from pathlib import Path
total_lines=0
py_files_list=[]
for py_files in Path(".").rglob("*.py"):
    if any(part in py_files.parts for part in ["venv","env","__pycache__",".git"]):
        continue
    py_files_list.append(py_files)
    try:
        with open(py_files,"r",encoding="utf-8") as f:
            lines=f.readlines()
            line_count=len(lines)
            total_lines+=line_count
            print(f"{py_files}-{line_count}行")
    except(UnicodeDecodeError,PermissionError)as e:
        print(f"{py_files}-读取失败：{e}")
print(f"\n找到{len(py_files_list)}个.py文件，总行数：{total_lines}行")



