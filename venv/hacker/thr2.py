
import threading
import  time

def fun1(key):
    print('hello: %s %s'%(key,time.ctime()))
def main():
    threads = []
    keys = ['zhangsan','lisi','wangwu']
    thread_count = len(keys)  # 线程数
    for i  in  range(thread_count):
        t=threading.Thread(target=fun1,args=(keys[i],))
        threads.append(t)
    for i in  range(thread_count):
        threads[i].start()
    for i in  range(thread_count):
        threads[i].join()
if __name__ == '__main__':
    main()