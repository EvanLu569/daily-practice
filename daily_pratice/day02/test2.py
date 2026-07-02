# #  1. 写一个函数 is_adult(age)，参数是年龄，≥18 返回True，
# #  否则返回 False。然后调用它测试。
# def is_adult(age):
#     if age>=18:
#         return True
#     else:
#         return False
# print(is_adult(19))
# print(is_adult(17))
#
# #  2. 写一个函数 get_bigger(a,b)，接收两个数字，返回较大的那个。
# def get_bigger(a,b):
#     if a>b:
#         return a
#     else:
#         return b
#

# #  写一个程序：简单的日记本
# print("我的日记本")
# #  1. 让用户输入一行文字
# while True:
#     text=input("请输入内容（输入’退出‘结束）：\n")
#     if text=="退出":
#         break
#     #  2. 把文字追加写入 diary.txt（用 "a"模式，之前的日记不丢失）
#     with open("diary.txt","a",encoding="utf-8") as f:
#       f.write(text+"\n")
#     #  3. 输入完后，读取 diary.txt 全部内容并打印出来
#     print("你的日记内容：\n")
#     with open("diary.txt","r",encoding="utf-8") as f:
#       context=f.read()
#     print(context)
#     #  提示：用 while 循环让用户反复输入，输入 "退出" 时结束。

# 新的知识点：break
'''
break 循环到此为止，后面的不跑了
'''




#  把学过的函数和文件读写结合起来：写一个函数
#  save_diary(text)，接收日记内容，负责把内容追加写入文件。然后
#  在主程序里调用这个函数，不要在主程序里直接写 with open。
def save_diary(text):
    with open("diary.txt","w",encoding="utf-8") as f:
        f.write(text+"\n")

print("我的日记本")
while True:
    text=input("请输入内容（输出‘退出’结束）：")
    if text =="退出":
        break
    save_diary(text)

print("\n你的日记：")
with open("diary.txt","r",encoding="utf-8") as f:
    print(f.read())








