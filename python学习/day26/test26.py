# # 1. 用多进程计算 1-1_000_000 范围内所有质数（分别用单进程和多进程测速）
# import time
# from concurrent.futures import ThreadPoolExecutor
#
#
# def is_prime(n):
#     if n<2:
#         return False
#     for i in range(2,int(n**0.5)+1):
#         if n%i==0:
#             return False
#         return True
# def count_primes(start,end):
#     return sum(1 for i in range(start,end)if is_prime(i))
# if __name__=="__main__":
#     n=1_000_000
#     # 单进程
#     start=time.time()
#     single=count_primes(2,n)
#     print(f"单进程：{time.time()-start:.2f}秒，质数{single}个")
#
#     # 多进程
#     start=time.time()
#     chunk=n//4
#     ranges=[(2,chunk),(chunk,chunk*2),(chunk*2,chunk*3),(chunk*3,n)]
#     with ThreadPoolExecutor(max_workers=4) as executor:
#         results=executor.map(lambda r:count_primes(*r),ranges)
#     print(f"多进程：{time.time()-start:.2f}秒，质数{sum(results)}个")
#
# # 2. 用 ProcessPoolExecutor 并行处理 100 张"图片"的文件名重命名
# #    模拟：每个任务 sleep(0.1) 然后返回新文件名
# def rename_image(filename):
#     time.sleep(0.1)
#     new_name=filename.replace("img_","photo_")
#     return new_name
# if __name__=="__main__":
#     files=[f"img_{i:03d}.jpg"for i in range(100)]
#
#     # 单进程
#     start=time.time()
#     single=[rename_image(f)for f in files]
#     print(f"单进程：{time.time()-start:.2f}秒")
#     # 多进程
#     start=time.time()
#     with ThreadPoolExecutor(max_workers=8) as executor:
#         multi=list(executor.map(rename_image,files))
#     print(f"多进程：{time.time()-start:.2f}秒")
# # 3. 对比总结：多线程、多进程、串行三种方式在 IO 密集和 CPU 密集场景下的耗时
# import time
# import threading
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
# def io_task(n):
#     time.sleep(0.1)
#     return n
# def cpu_task(n):
#     return sum(i ** 2 for i in range(500000))
#
# def test(task, tasks, workers=8):
#     # 串行
#     start = time.time()
#     [task(i) for i in range(tasks)]
#     serial = time.time() - start
#
#     # 多线程
#     start = time.time()
#     with ThreadPoolExecutor(workers) as e:
#         list(e.map(task, range(tasks)))
#     thread = time.time() - start
#
#     # 多进程
#     start = time.time()
#     with ProcessPoolExecutor(workers) as e:
#         list(e.map(task, range(tasks)))
#     process = time.time() - start
#
#     return serial, thread, process
#
# if __name__ == '__main__':
#     print("IO密集型 (50个任务，每个sleep 0.1s)")
#     s, t, p = test(io_task, 50)
#     print(f"串行：{s:.2f}s | 多线程：{t:.2f}s ({s / t:.1f}x) | 多进程：{p:.2f}s ({s / p:.1f}x)")
#
#     print("\nCPU密集型 (8个任务，每个计算50万次)")
#     s, t, p = test(cpu_task, 8)
#     print(f"串行：{s:.2f}s | 多线程：{t:.2f}s ({s / t:.1f}x) | 多进程：{p:.2f}s ({s / p:.1f}x)")
#
#







