# # 函数+文件读写
# # 函数 把代码打包成工具
# # 定义一个函数
# def greet():
#     print("你好！")
#     print("欢迎学习python\n")
#
# #调用函数
# greet()
# greet()  #想用几次就调用几次
#
# # 带参数的函数  传数据进去
# def greet_user(name):
#     print(f"你好,{name}!")
#
# greet_user("Evan")
# greet_user("张三")
#
# # 带返回值的函数 把结果丢回来
# def add(a,b):
#     result=a+b
#     return result
# sum_result=add(3,6)
# print((sum_result))

# 第二部分：文件读写 让程序记住数据
# 文件读写能让数据存到硬盘上
# 写入文件
# with open("test.txt","w",encoding="utf-8") as f:
#     f.write("这是第一行\n")
#     f.write("这是第二行\n")
# print("写入完成！")
#
# # 读取文件
# with open("test.txt","r",encoding="utf-8") as f:
#     content=f.read()  #一次性读取全部
# print(content)
#
# # 按行读取
# with open("test.txt","r",encoding="utf-8") as f:
#     for line in f:
#         print(f"读取到：{line.strip()}")  #strip()去掉换行符
#
# # 追加内容
# with open("test.txt","a",encoding="utf-8") as f:
#     f.write("追加内容\n")






