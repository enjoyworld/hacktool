# 多线程编程 学习示例 通常使用 thread threading（推荐）
import _thread # python3采用
import time

def fun1():
    print('current time: %s'%time.ctime())

def main():
    _thread.start_new_thread(fun1,())
    _thread.start_new_thread(fun1,())
    time.sleep(2)
    print('current time: %s' % time.ctime())
if __name__ == '__main__':
    main()