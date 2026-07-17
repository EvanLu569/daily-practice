# 1. 用 ThreadPoolExecutor 并发下载 10 个网页，统计总耗时（对比串行）
import queue
import threading
import time
import requests
from concurrent.futures.thread import ThreadPoolExecutor

urls = ["https://httpbin.org/delay/1"] * 10
def download(urls,worker=1):
    with ThreadPoolExecutor(max_workers=worker)as executor:
        return list(executor.map(requests.get,urls))
for workers in [1,5,10]:
    start=time.time()
    download(urls,workers)
    print(f"workers={workers:2d}:{time.time()-start:.2f}")

# 2. 实现一个线程安全的计数器（10 个线程各加 100 万次），验证最终结果
counter=0
lock=threading.Lock()
def increment():
    global counter
    for _ in range(1_000_000):
        with lock:
            counter+=1
threads=[threading.Thread(target=increment)for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(f"最终结果”{counter:,}")
# 3. 用 Queue 实现生产者-消费者模型
#    生产者每秒生产一个数字，2 个消费者处理，处理完存到列表中
def producer(q:queue.Queue):
    for i in range(2):
        q.put(f"任务{i}")
        print(f"生产：任务{i}")
        time.sleep(0.5)
    q.put(None)
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
c1=threading.Thread(target=consumer,args=(q,"消费者1"))
c2=threading.Thread(target=consumer,args=(q,"消费者2"))
p.start();c1.start();c2.start()
p.join();c1.join();c2.join()

# 4. 用一个 file_downloader(url, save_path) 函数，10 个线程并发下载文件列表
#    每个线程下载完把结果（成功/失败）放进一个共享列表，用 Lock 保护
results=[]
lock=threading.Lock()
def file_downloader(url:str,save_path:str):
    try:
        response=requests.get(url,timeout=10)
        response.raise_for_status()
        with open(save_path,'wb')as f:
            f.write(response.content)
        with lock:
            results.append({
                'url':url,
                'path':save_path,
                'status':'成功',
                'size':len(response.content)
            })
            return True
    except Exception as e:
        with lock:
            results.append({
                'url':url,
                'path':save_path,
                'status':'失败',
                'error':str(e)
            })
            return False

files = [
    ("https://picsum.photos/200/300", "img1.jpg"),
    ("https://picsum.photos/200/300", "img2.jpg"),
    ("https://picsum.photos/200/300", "img3.jpg"),
    ("https://picsum.photos/200/300", "img4.jpg"),
    ("https://picsum.photos/200/300", "img5.jpg"),
    ("https://picsum.photos/200/300", "img6.jpg"),
    ("https://picsum.photos/200/300", "img7.jpg"),
    ("https://picsum.photos/200/300", "img8.jpg"),
    ("https://picsum.photos/200/300", "img9.jpg"),
    ("https://picsum.photos/200/300", "img10.jpg"),
]
with ThreadPoolExecutor(max_workers=10)as executor:
    executor.map(lambda f:file_downloader(*f),files)
for r in results:
    print(r)
print(f"\n共下载{len(results)}个文件")


















