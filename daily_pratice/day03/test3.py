#   写一个 IP 归属地查询工具：
#   # 要求：
import requests
#   # 1. 让用户输入一个 IP 地址
ip=input("请输入要查询的IP：\n")
#   # 2. 调用 http://ip-api.com/json/输入的IP
if ip=="":
    url="http://ip-api.com/json/"
else:
    url=" http://ip-api.com/json/"+ip
#   # 3. 打印出城市、国家、运营商
#   # 4. 用 try/except 处理异常
try:
    response=requests.get(url,timeout=10)
    data=response.json()

    if data["status"]=="success":
        print(f"IP:{data['query']}")
        print(f"国家:{data['country']}")
        print(f"城市：{data['city']}")
        print(f"运营商：{data['isp']}")
    else:
        print("查询失败，请检查IP是否正确")
except Exception as e:
    print(f"请求失败:{e}")

#   # 5. 如果用户直接回车不输入，就查本机 IP（请求 http://ip-api.com/json/）