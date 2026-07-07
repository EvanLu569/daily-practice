# 1. 调用 https://v1.hitokoto.cn/ 获取 5 条名言，存到列表中
import requests
quotes=[]
for i in range(5):
    try:
        resp=requests.get("https://v1.hitokoto.cn/",timeout=5)
        resp.raise_for_status()
        data=resp.json()
        quote=f"{data['hitokoto']}--{data.get('from','未知出处')}"
        quotes.append(quote)
        print(f"第{i+1}条：{quote}")
    except Exception as e:
        print(f"获取第{i+1}条失败：{e}")
print("所有的名言：")
for idx,quote in enumerate(quotes,1):
    print(f"{idx}.{quote}")
# 2. 用 GET + params 参数调用一个搜索 API，处理返回的 JSON
resp=requests.get("https://httpbin.org/get",params={
    "q": "Python编程",
    "page": 1,
    "limit": 10
})
print("请求URL:",resp.url)
print("返回数据",resp.json())
# print("返回数据", resp.text)
# 3. 用 POST + JSON 向 https://httpbin.org/post 发送数据，
# 验证返回的 JSON
resp=requests.post("https://httpbin.org/post",json={
    "username": "zhangsan",
    "password": "123456",
})
print("验证返回的json数据：",resp.json())

# 4. 用 Session 封装一个 GitHub API 客户端（不需要 token，查公开信息即可）
#    查询某个用户的公开仓库列表：GET https://api.github.com/users/{username}/repos
session=requests.Session()
session.headers.update({
    "User-Agent": "MyApp/1.0",  # GitHub API 需要 User-Agent
    "Accept": "application/json"
})
username="Evanlu569"
resp=session.get(f"https://api.github.com/users/{username}/repos")
resp.raise_for_status()
repos=resp.json()
print(f"{username}的公开仓库：")
for repo in repos:
    print(f"{repo['name']}:{repo['stargazers_count']}⭐")

# 5. 写一个带重试和超时的 API 调用函数
import time
def call_api_with_retry(url,method="GET",max_retries=3,timeout=5,**kwargs):
    # 设置默认请求头
    headers=kwargs.get("headers",{})
    headers.setdefault("User-Agent","MyApp/1.0")
    kwargs["kwargs"]=headers

    for attempt in range(1,max_retries+1):
        try:
            print(f"第{attempt}/{max_retries}次尝试")
            if method.upper()=="GET":
                resp=requests.get(url,timeout=timeout,**kwargs)
            elif method.upper()=="POST":
                resp=session.post(url,timeout=timeout,**kwargs)
            else:
                raise ValueError(f"不支持的方法：{method}")
            resp.raise_for_status()
            print("请求成功!")
            return resp.json()
        except requests.exceptions.Timeout:
            print(f"超时 (>{timeout}秒)")
        except requests.exceptions.ConnectionError:
            print(f"连接失败")
        except requests.exceptions.HTTPError as e:
            if e.response and 400 <= e.response.status_code < 500:
                print(f"客户端错误 {e.response.status_code}，不再重试")
                break
            print(f"HTTP错误: {e}")
        except Exception as e:
            print(f"错误: {e}")
            break
        if attempt<max_retries:
            waited_time=attempt*2
            print(f"⏳ 等待 {waited_time} 秒后重试...")
            time.sleep(waited_time)
    return None
result=call_api_with_retry( "https://api.github.com/users/octocat",max_retries=2,timeout=5)
if result:
    print(f"\n✅ 获取成功:")
    print(f"  用户名: {result.get('login')}")
    print(f"  姓名: {result.get('name', '未设置')}")
    print(f"  仓库数: {result.get('public_repos', 0)}")

