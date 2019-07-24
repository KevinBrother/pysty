from threading import Thread, Lock
from time import sleep

# 100个线程分别向账户中转入1元钱
class Account(object):
    def __init__(self, money = 0):
        self._money = money
        self._lock = Lock()

    def deposit(self, money):
        # 先获取锁才能执行后面的代码
        self._lock.acquire()

        try:
            # 计算存款后的余额
            new_money = self._money + money
            # 模拟受理存款业务需要0.01秒的时间
            sleep(0.01)
            # 修改账户余额
            self._money = new_money   
        finally:
            # 在finally中释放锁，保证异常锁也能释放。
            self._lock.release()     
    
    @property
    def money(self):
        return self._money

class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._aacount = account
        self._money = money

    def run(self):
        self._aacount.deposit(self._money)

def main():
    a = Account()
    thread = []
    for _ in range(100):
        t = AddMoneyThread(a, 1)
        thread.append(t)
        t.start()

    for t in thread:
        t.join()

    print(a.money)
    

if __name__ == "__main__":
    main()