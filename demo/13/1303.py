# 完成1~100000000求和的计算密集型任务
from multiprocessing import Process, Queue
from time import time

def main():

    def calc(curr_list, result_queue):
        total = 0
        for i in curr_list:
            total += i
            result_queue.put(total)


    index = 0
    result_queue = Queue()
    processs = []
    arr = [x for x in range(1, 100000001)]

    for _ in range(8):
        p = Process(target=calc, args=(arr[index: index + 12500000], result_queue))
        
        index += 12500000
        processs.append(p)
        p.start()

    start = time()    
    for p in processs:
        p.join
    
    # 合并结果cled
    total = 0
    while not result_queue.empty():
        total += result_queue.get()
    print(total)
    end = time()
    print('总共用时%02f' % (end - start))

if __name__ == "__main__":
    main()