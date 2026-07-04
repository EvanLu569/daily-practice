# 题1：给定一个单词列表，筛选出长度 >= 5 的单词，转成大写
words = ["hello", "world", "python", "is", "awesome", "code"]
# 期待：['HELLO', 'WORLD', 'PYTHON', 'AWESOME']
result=[w.upper() for w in words if len(w)>=5]
print(result)
# 题2：给定一个句子，统计每个字符出现的次数（用字典推导式）
sentence = "hello world"
# 期待：{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r':1, 'd': 1}
result={ch:sentence.count(ch)for ch in sentence}
print(result)
# 题3：两个列表，找出所有两个字母组成的组合（用嵌套推导式）
letters = ["a", "b", "c"]
nums = ["1", "2"]
# 期待：['a1', 'a2', 'b1', 'b2', 'c1', 'c2']
result=[a+b for a in letters for b in nums]
print(result)
# 题4：用生成器表达式计算 1 到 100 万中所有偶数的平方和
# 提示：sum((x**2 for x in range(2, 1_000_001, 2)))
result=sum(x**2 for x in range(2,1_000_001,2)) #从2开始，步长为2，就是偶数
print(result)
# 题5：写一个生成器函数，无限产出从 1 开始的奇数
# 然后用 next() 取前 5 个验证
def gen():
    n=1
    while True:
        yield n
        n+=2
g=gen()
print([next(g)for _ in range(5)])