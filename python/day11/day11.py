'''
推导式深入+生成器
'''
# 1.推导式回顾+扩展
# 列表推导式
squares=[i**2 for i in range(1,6)]
print(squares)
evan=[x for x in range(1,11) if x%2==0]
print(evan)
# 字典推导式   快速构造字典
word="hello"
char_count={ch:word.count(ch) for ch in set(word)}
print(char_count)
#集合推导式  和列表推导式一样，只是用花括号
nums=[1,2,2,3,3,3]
unique_squares={n**2 for n in nums}
print(unique_squares)
# 2.嵌套推导式
# 展平二维列表
matrix=[[1,2,3],[4,5,6],[7,8,9]]
flat=[num for row in matrix for num in row]
print(flat)
#等价于普通的for循环
for row in matrix:
    for num in row:
        flat.append(num)  # 嵌套推导式的顺序和for循环一样：外层先写，内层后写

# 3.生成器  内存友好版推导式
'''
列表推导式的问题是一次性把所有结果算出来放在内存里。
100万个数据就占100万的内存
'''
# 列表推导式  方括号，结果全在内存里
squares_list=[i**2 for i in range(10_000_000)] # 占大量内存
#生成器表达式  圆括号，用的时候才一个一个算
squares_gen=(i**2 for i in range(10_000_000)) # 几乎不占内存
print(next(squares_gen)) # 0
print(next(squares_gen)) # 1
print(next(squares_gen)) # 4  #每次next()才算一个值，用完就扔

'''
总结：
列表推导式：[...for x in ...] 一次全算出来，占用内存大，能迭代多次，可以取下标
生成器表达式：(...for x in ...)用的时候才算，占用内存小，不能迭代（用完就没了），不能取下标
'''

# 4.yield 用函数写生成器
#斐波那契函数
def fibonacci(n:int):
    a,b=0,1
    for _ in range(n):
        yield a # yield=产出一个值，然后暂停
        a,b=b,a+b
# 遍历生成器
for num in fibonacci(10):
    print(num,end=" ")
# 也可以手动next()
gen=fibonacci(5)
print(next(gen))
print(next(gen))
print(next(gen))
'''
yield和return的区别:
return：函数执行完就结束了
yield：产出一个值，函数暂停，下次next()是从暂停的位置继续
'''











