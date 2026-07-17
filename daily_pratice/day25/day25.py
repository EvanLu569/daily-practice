'''
多线程编程
python默认是单线程，但IO密集型任务（网络请求、文件读写、数据库查询）可以用多线程加速
线程：程序里独立的执行流，同一进程内的线程共享内存
GIL：全局解释器锁，python同一时刻只能有一个线程执行python代码
结论：多线程适合IO密集型，不适合CPU密集型（CPU）密集型多用进程
'''
# 基础用法
import threading
import time
def download(url:str,index:int):
    print(f"开始下载{index}:{url}")
    time.sleep(2)
    print(f"下载完成{index}:{url}")
# 创建线程
threads=[]
for i,url in enumerate(["url1","url2","url3"]):
    t=threading.Thread(target=download,args=(url,i,))
    threads.append(t)
    t.start()
# 等待所有线程完成
for t in threads:
    t.join()
print("全部下载完成")  # 如果不用线程，3个url串行要下载6秒；用线程并行，只有大概2秒

# 线程池  控制并发数
from concurrent.futures import ThreadPoolExecutor,as_completed
import time
def download(url:str)->str:
    time.sleep(2)
    return f"{url}下载完成"
urls=[f"url_{i}"for i in range(10)]
# 方式1:map（保持输入顺序）
with ThreadPoolExecutor(max_workers=3)as executor:
    results=executor.map(download,urls)
    for r in results:
        print(r)
# 方式2：submit（哪个先完成先处理哪个）
with ThreadPoolExecutor(max_workers=3)as executor:
    futures={executor.submit(download,url):url for url in urls}
    for future in as_completed(futures):
        print(future.result())


# 线程安全  Lock锁  多线程同时修改共享数据会出事，用锁保护
import threading
counter=0
lock=threading.Lock()
def increment():
    global counter
    for _ in range(1_000_000):
        with lock:
            counter+=1
threads=[threading.Thread(target=increment)for _ in range(5)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(counter)  # 不用锁时，5个线程可能同时读counter、各自加1、再写回去--->写了5次，但实际只加了2~3

# Queue  线程间通信
import threading
import queue
import time
def producer(q:queue.Queue):
    for i in range(10):
        q.put(f"任务{i}")
        print(f"生产：任务{i}")
        time.sleep(0.5)
    q.put(None) # 结束信号
def consumer(q:queue.Queue,name:str):
    while True:
        item=q.get()
        if item is None:
            q.put(None)
            break
        print(f"{name}处理：{item}")
        time.sleep(1)
q=queue.Queue()
p=threading.Thread(target=producer,args=(q,))
c1=threading.Thread(target=consumer,args=(q,"消费者A"))
c2=threading.Thread(target=consumer,args=(q,"消费者B"))
p.start();c1.start();c2.start()
p.join();c1.join();c2.join()



