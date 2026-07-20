# 1. 用切片反转一个列表
# 输入：[1, 2, 3, 4, 5] → [5, 4, 3, 2, 1]
lst=[1,2,3,4,5]
print(lst[::-1])
# 2. 用解包交换两个变量的值
# a, b = 1, 2 交换成 a=2, b=1
a,b=1,2
a,b=b,a
print(a,b)
# 3. 用 set 对 [3, 1, 2, 3, 1, 2, 3, 1] 去重，再转回列表排序
print(list(set([3, 1, 2, 3, 1, 2, 3, 1])))
# 4. 用 zip 把两个列表合成字典
keys = ["name", "age", "city"]
vals = ["张三", 25, "北京"]
print(dict(zip(keys, vals)))
# 5. 用 * 解包合并 3 个字典
d1 = {"a": 1}; d2 = {"b": 2}; d3 = {"c": 3}
print({**d1,**d2,**d3})

print("\n闭包练习:")
# 1. 写一个 make_power(n) 闭包，返回计算 x 的 n 次方的函数
# pow2 = make_power(2); pow2(5) → 25
def make_power(n):
    def power(x):
        return x**n
    return power
pow2=make_power(2)
print(pow2(5))
# 2. 写一个 password_checker(password) 闭包，返回一个验证函数
# check = password_checker("123456")
# check("abc") → False; check("123456") → True
def passwor_checker(password:str):
    def check(guess:str)->bool:
        return guess==password
    return check
check=passwor_checker("123456")
print(check("123456"))
print(check("abc"))
# 3. 写一个 make_logger(prefix) 闭包，返回带前缀的打印函数
# log = make_logger("[ERROR]")
# log("文件未找到") → 打印 "[ERROR] 文件未找到"
def make_logger(prefix:str):
    def log(message:str):
        print(f"{prefix}{message}")
    return log
log=make_logger("[ERROR]")
print(log("文件未找到"))
# 4. 写一个 make_rate_limiter(max_calls) 闭包，限制函数调用次数
# 超过次数后返回 "已达上限"
def make_rate_limiter(max_calls):
    count=0
    def rate_limiter():
        nonlocal count
        count+=1
        if count>max_calls:
            return "已达上限"
        return f"第{count}次调用"
    return rate_limiter
r=make_rate_limiter(2)
print(r())
print(r())
print(r())













