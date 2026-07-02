# # 第一步：变量  存储数据的盒子
# name="张三"
# age=22
# height=1.66
# is_student=True
#
# print(name)
# print(age)
# print(height)
# print(is_student)
#
# # 第二步：输入  让用户告诉你信息
# name=input("你叫什么名字？\n")
# print("你好，"+name)
#
# age=input("你多大了？\n")
# print("你明年"+str(int(age)+1)+"岁")
#
# #第三步：判断  让程序做选择
#
# score=int(input("请输入你的分数："))
# if score>=90:
#     print("优秀")
# elif score>=60:
#     print("及格")
# else:
#     print("不及格")
#

# # #第四步：for循环  做固定次数的事情
# for i in range(1,6):
#     print(f"这是第{i}次") #从1到5，不包含6
#
# # 第五步：while循环 条件满足就一直做
# count=0
# while count<3:
#     print(f"倒计时：{count}")
#     count=count+1
# print("结束")

# # 第六步：列表  存一堆东西的盒子 用[]包起来，东西用逗号隔开
# fruits=["苹果","香蕉","橘子","葡萄"]
# print(fruits[0])
# print(fruits[2])
# print(len(fruits))
#
# # 往列表里面添加东西
# fruits.append("西瓜")
# print(fruits)
#
# #遍历循环列表
# for fruits in fruits:
#     print(f"水果：{fruits}")
#
# #第七步：字典  给数据贴标签的盒子 用{}包起来，每个东西都有名字
# student={
#     "姓名":"张三",
#     "年龄":22,
#     "分数":100
# }
# print("\n")
# print(student["姓名"])
# print(student["年龄"])
#
# # 修改和新增
# student["分数"]=98
# student["城市"]="上海"
# print(student)

#两种容器的区别
'''
列表：按编号[0][1]...找东西，使用场景：有顺序的一堆东西
字典：按名字的键值对找东西 ["姓名"]  使用场景：有名字的键值对
'''







