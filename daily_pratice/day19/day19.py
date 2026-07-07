'''
requests进阶  调用真实API
'''
# Session 保持连接和Cookie
'''
Q:为什么要用session？
A:
保持cookie：登录后，后续请求自动带上登录状态
复用配置：一次设置headers，所有请求都自动带上
连接池：复用TCP连接，速度快
'''
import requests
session=requests.Session()
session.headers.update({  # 设置全局请求头，所有使用这个session的请求都会带上
    "user-Agent":"MyAPP/1.0",
    "Accept":"application/json",
})
# 之后所有请求都用这个session，自动带上headers
resp=session.get("https://httpbin.org/headers")
print(resp.json()) # 打印返回的JSON数据

# GET 请求传参数
'''
GET请求的参数是放在URL后面的
params会自动帮你把字典转换成URL参数格式
比手拼更安全
'''
# 方式1：直接拼URL
# resp=requests.get("https://api.example.com/search?q=python&page=1")
# 方式2：用params参数
resp=requests.get("https://httpbin.org/get",params={
    "q":"python",
    "page":1,
})
print(resp.url)

# POST请求发送数据
'''
用于提交数据，有三种常见方式
'''
# 1.发送JSON  自动将字典转为JSON字符串，自动设置content-Type:application/json  用于RESTful API
resp=requests.post("https://httpbin.org/headers",json={
    "username":"zhangsan",
    "password":"123456",
} )
# 2.发送表单  以key1=value&key2=value2格式发送  自动设置content-Type:application/x-www-form-urlencoded  用于传统HYML表单提交
resp=requests.post("https://httpbin.org/post",data={
    "username": "zhangsan",
    "password": "123456",
})
# 3.上传文件  自动设置content-Type:multipart/form-data  用于上传图片、PDF等文件
with open("report.pdf","rb")as f:
    resp=requests.post("https://httpbin.org/post", files={"file":f})

# 超时、错误处理
try:
    resp=requests.get("https://api.example.com/data",timeout=5)
    resp.raise_for_status() #状态码不是200就抛异常
    data=resp.json() #解析JSON数据
except requests.exceptions.Timeout:
    print("请求超时，请检查网络")
except requests.exceptions.HTTPError as e:
    print(f"HTTP错误：{e}")
except requests.exceptions.ConnectionError:
    print("连接失败，api可能挂了")
except requests.exceptions.RequestException as e:
    print(f"请求出错：{e}")

# 调用免费API实战
# 1.天气API（和风天气免费版）
# 2.随即一言API
import requests
def get_random_quote()->str:
    resp=requests.get("https://v1.hitokoto.cn/",timeout=5)
    resp.raise_for_status()
    data=resp.json()
    return f"{data['hitokoto']}--{data['from']}"  # 返回格式：句子+出处
def get_joke()->str:
    resp=requests.get("https://v2.jokeapi.dev/joke/Programming?lang=zh",timeout=5)
    data=resp.json()
    # 笑话有两种格式
    if data.get("type")=="single": #单段式笑话
        return data["joke"]
    else: # 双段式笑话（有铺垫和包袱）
        return f"{data['setup']}\n{data['deliver']}"
print(get_random_quote())
print(get_joke())





