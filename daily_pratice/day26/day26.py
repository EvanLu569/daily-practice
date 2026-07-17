'''
多进程并行
GIL让多线程在CPU密集型任务上无效。真正的并行要用多进程   每个进程有独立的python解释器和GIL
'''
# import random
# import time
# from concurrent.futures import as_completed
# from concurrent.futures import ProcessPoolExecutor
#
#
# def cpu_intensive(n:int)->int:
#     total=0
#     for i in range(n):
#         total+=i**2
#     return total
# # 收集多进程结果
# def heavy_computation(task_id:int)->tuple[int,float]:
#     duration=random.uniform(1,5)
#     time.sleep(duration)
#     result=task_id**10
#     return task_id,result
#
# # 单进程
# if __name__=='__main__':
#     start=time.time()
#     with ProcessPoolExecutor(max_workers=4)as executor:
#         results=list(executor.map(cpu_intensive,[10_000_000]*4))
#     print(f"并行耗时{time.time()-start:.2f}")
#
#     start=time.time()
#     with ProcessPoolExecutor(max_workers=4) as executor:
#         futures = {
#             executor.submit(heavy_computation, i): i for i in range(8)
#         }
#         for future in as_completed(futures):
#             task_id, results = future.result()
#             print(f"任务{task_id}完成，结果的前5位：{str(results)[:5]}...")

'''
Socket网络编程
Socket是网络通信的底层接口，HTTP、数据库连接都基于它。
客户端                           服务端
socket()                        socket()
connect()  ──────连接────────→  bind() + listen()
send()     ──────数据────────→  recv()
recv()     ←─────响应────────  send()
close()                        close()
'''
# 简易TCP服务端
import socket
def start_server(host:str="127.0.0.1",port:int=8080):
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(host,port)
    server.listen(5)
    print(f"服务端启动：{host}:{port}，等待连接。。。")
    while True:
        client,addr=server.accept()
        print(f"客户端{addr}已连接")
        data=client.recv(1024)
        print(f"收到：{data.decode('utf-8')}")
        response="HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello from server!"
        client.send(response.encode("utf-8"))
        client.close()
# 简易TCP客户端
def send_request(host:str="127.0.0.1",port:int=8080,message:str="Hello!"):
    client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    client.connect((host,port))
    client.send(message.encode("utf-8"))
    response=client.recv(4096)
    print(f"收到响应：{response.decode('utf-8')}")
    client.close()
send_request(message="你好，服务器！")

# 简易HTTP服务器
def http_server(host:str="127.0.0.1",port:int=8080):
    server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server.bind(host,port)
    server.listen(5)
    print(f"简易HTTP服务器：http://{host}:{port}")
    while True:
        client,addr=server.accept()
        request=client.recv(4096).decode("utf-8")

        first_line=request.split("\r\n")[0]
        method,path,*_=first_line.split(" ")

        if path=="/":
            body="<h1>首页</h1>"
        elif path=="/hello":
            body="<h1>Hello world!</h1>"
        else:
            body=("<h1>404 Not Found</h1>")
        response = (
            "HTTP/1.1 200 OK\r\n"
            "Content-Type: text/html; charset=utf-8\r\n"
            f"Content-Length: {len(body.encode('utf-8'))}\r\n"
            "\r\n"
            f"{body}"
        )
        client.send(response.encode("utf-8"))
        client.close()

# UDP通信
# UDP 客户端发送
udp_client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
udp_client.sendto("Hello UDP".encode(), ("127.0.0.1", 9999))
data, addr = udp_client.recvfrom(1024)
print(data.decode())



