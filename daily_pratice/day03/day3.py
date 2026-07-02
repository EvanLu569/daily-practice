# 第三方库+网络请求+JSON
# 第一部分：pip  安装别人的代码
# python自带的叫标准库，别人写的叫第三方库。pip install就是下载安装

'''
操作步骤：
1.打开终端输入pip install requests
'''

# 第二部分：requests  发HTTP请求
# 浏览器打开网页就是发了一个http请求。requests让python也能发

# import requests
#
# # 发一个Get请求（就像浏览器打开网页）
# response=requests.get("http://www.baidu.com")
# print(response.status_code)  # 200表示成功，404表示找不到
# print(response.text[:200])   # 返回的内容，只打印前200个字符


# 第三部分：JSON  数据交换格式
# 上一个例子里返回的就是JSON。它是前后端沟通的语言
# import requests
# response=requests.get("https://api.github.com")
# data=response.json()  # 把返回内容转成Python字典
# print(data["current_user_url"])  # 像操作字典一样取值

# # 第四部分：异常处理  让程序不崩
# # 网络请求可能失败（断网、服务器不佳），用try/except兜住
# import requests
# try:
#     response=requests.get("http://111.com",timeout=5)
#     print("请求成功")
# except:
#     print("网络出问题了，请检查连接")

'''
总结：
python程序发送HTTP请求出去，某个网站的服务器返回数据给python程序，返回数据的格式有两种（JSON、HTML）
JSON：给程序读的结构化数据，用response.json()解析
HTML：给浏览器看的网页源码，用response.text读取

用.json()之前，先确认返回的是JSON，不确定就先用.text看一下
'''