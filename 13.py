from time import time, sleep
from random import randint


def file_download(fname):
    print('开始下载%s' % fname)
    rd = randint(2, 5)
    sleep(rd)
    print('%s下载完成,耗费了%s秒' % (fname, rd))


def process_download():
    from multiprocessing import Process
    # 多进程
    # 创建进程时，子进程复制了父进程并有单独的内存看空间
    # 子进程的通信需要管道，python中使用multiprocessing模块中的Queue类
    # 是共享一个队列。
    start = time()
    p1 = Process(target=file_download, args=('开始学习python进程！', ))    
    p1.start()
    p2 = Process(target=file_download, args=('python入门到放弃！', ))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('一共耗时%0.2f秒下载完成！' % (end-start))

def thread_download():
    from threading import Thread
    # 多线程
    start = time()
    t1 = Thread(target=file_download, args=('开始学习python进程！', ))    
    t1.start()
    t2 = Thread(target=file_download, args=('python入门到放弃！', ))
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('一共耗时%0.2f秒下载完成！' % (end-start))



# 利用继承来实现
from threading import Thread
class thred_extend_download(Thread):
    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s' % self._filename)
        rd = randint(2, 5)
        sleep(rd)
        print('%s下载完成,耗费了%s秒' % (self._filename, rd))

def th_ex_down():
    start = time()
    t1 = thred_extend_download('开始学习python进程！')
    t1.start()
    t2 = thred_extend_download('python入门到放弃！')
    t2.start()
    t1.join()
    t2.join()
    end = time()
    print('一共耗时%0.2f秒下载完成！' % (end-start))

def main():
    # process_download()
    # thread_download()
    th_ex_down()
    
if __name__ == "__main__":
    main()