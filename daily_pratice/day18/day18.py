'''
JSON/CSV数据处理
'''
# JSON
import json
# 字典  JSON字符串（序列化）
data={
    "name":"zhangsan",
    "age":22,
    "skills":["python","SQL"],
    "address":{"city":"beijing","district":"haiding"}
}
# dumps()：把python对象变成字符串，末尾的s是string
json_str=json.dumps(data,ensure_ascii=False,indent=2)  # ensure_ascii：直接显示汉字  indent：缩进为2
print(json_str)

# JSON 字符串   字典（反序列化）
parsed=json.loads(json_str) # load()把字符串解析成python对象
print(parsed["skills"][0])

# 读写JSON文件
with open("data.json","w",encoding="utf-8") as f:
    json.dump(data,f,ensure_ascii=False,indent=2)  # dump()末尾没有s，写入的是文件
with open("data.json","r",encoding="utf-8") as f:
    loaded=json.load(f)
print(loaded)

'''
CSV  纯文本表格，用逗号分隔每列，excel能直接打开，python用csv模块读写
'''
import csv
# 写入csv
with open("students.csv","w",newline="",encoding="utf-8-sig")as f:  # newline必须加，不然每行之间会多一个空行，utf-8-sig：比utf-8多一个BOM头，这样excel打开不会乱码
    writer=csv.writer(f) # 创建一个“写手”对象，它知道怎么把数据写成csv格式
    writer.writerow(["name","age","score"]) # 表头  writerow：写一行
    writer.writerows([ # writerows：写多行，传一个嵌套列表，外层每个元素是一行
        ["zhangsan",20,99],
        ["lisi",23,98],
        ["wangwu",24,100]
    ])
# 读取CSV
with open("students.csv","r",newline="",encoding="utf-8-sig") as f:
    reader=csv.DictReader(f)  # 每行变成字典，键是表头  DictReader自动把第一行当表头，后续每行用表头做key，读出来的是字典  reader()读出来的是列表
    for row in reader:
        print(f"{row['name']}-{row['score']}分")

print("\n")
'''
pathlib  现代化的路径处理  
告别os.path.join()和字符串拼接，pathlib更直观
'''
from pathlib import Path
#创建路径
base=Path("G:/代码/PythonProject/daily_pratice")
day18=base
print(day18)

#创建目录
day18.mkdir(parents=True,exist_ok=True)

#在目录下创建文件
file=day18/"text.txt"
file.write_text("hello pathlib!",encoding="utf-8")

#读取文件
content=file.read_text(encoding="utf-8")
print(content)

#常用操作
print(file.name) #text.txt 文件名
print(file.stem) #text 不含后缀
print(file.suffix) #.txt 后缀
print(file.parent) #G:\代码\PythonProject\daily_pratice 父目录
print(file.exists()) #True 是否存在

# 遍历目录
for py_file in Path(".").glob("*.py"): #当前目录下所有.py文件
    print(py_file)
#遍历目录（递归）
for py_file in Path(".").rglob("*.py"):
    print(py_file)
# 读写和写入（不用with open）了
data=Path("data.txt").read_text(encoding="utf-8")
lines=Path("data.txt").read_text(encoding="utf-8").splitlines()
Path("output.txt").write_text("Hello",encoding="utf-8")

