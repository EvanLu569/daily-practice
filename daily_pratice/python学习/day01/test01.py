# #   1. 写一个程序：输入你的年龄，判断是否成年（≥18），
# #   输出"已成年"或"未成年"
# age=int(input("请输入你的年龄：\n"))
# if age>=18:
#     print("你已成年")
# else:
#     print("你是未成年")
#
# #  2. 写一个程序：输入两个数字，输出其中较大的那个
# num1=int(input("please enter num1:\n"))
# num2=int(input("please enter num2:\n"))
# if num1>num2:
#     print(num1)
# else:
#     print(num2)
#
# # 1. 用 for 循环输出 1 到 100 之间所有的偶数
# for i in range(1,101):
#     if(i%2==0):
#         print(i)
#
# #   2. 用 while 循环：让用户反复输入数字，输入0时退出，否则打印"继续输入"
# num1=int(input("请输入数字（输入0时退出）:\n"))
# while num1!=0:
#     print("继续输入")
#     num1=int(input("请输入数字（输入0时退出）:\n"))
#

# # 1. 创建一个列表，放 5 个数字，用 for 循环求出它们的总和
# num=[1,2,3,4,5]
# sum =0
# for i in num:
#     sum=sum+i
# print(sum)
#
# # 2. 创建一个字典，存一个人的信息（姓名、年龄、城市），然后循环
# # 遍历字典，把每一项打印出来
# info={
#     "name":"Evan",
#     "age":18,
#     "city":"shanghai"
# }
# for key in info:
#     print(f"{key}:{info[key]}")


'''
  程序功能：学生成绩管理器
  1. 创建一个列表，里面放 5 个学生的成绩（数字）
  2. 用 for 循环计算平均分
  3. 判断每个人是否及格（≥60），输出每个人的成绩和是否及格
  4. 用字典存最高分同学的信息（姓名、成绩、城市），打印出来
'''

# 1. 创建一个列表，里面放 5 个学生的成绩（数字）
scores=[98,100,88,97,99]
#2. 用 for 循环计算平均分
sum=0
for i in scores:
    sum=sum+i
print(sum/len(scores))
#  3. 判断每个人是否及格（≥60），输出每个人的成绩和是否及格
for s in scores:
    if s>60:
        print(f"成绩{s}:及格")
    else:
        print(f"成绩{s}:不及格")
#  4. 用字典存最高分同学的信息（姓名、成绩、城市），打印出来
info={
    "name":"lisi",
    "city":"shanghai",
    "score":max(scores)
}
print(f"最高分：姓名{info['name']},城市{info['city']},{info['score']}分")
