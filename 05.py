#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def craps():

    #craps赌博游戏
    #两个骰子 第一次和为6或11 玩家胜，和为2、3、12玩家输
    # 如果是其他数字，记录第一次的和，再次投掷至和第一次的值一样，玩家胜，
    # 如果投掷出和为6，则玩家输
    # 初始资金 1000 
    
    account = 1000

    from random import randint

    while account > 0:
        print('您的总资产为： %i' % account)

        while True:
            price = int(input('请下注！'))      
            if  price > 0 and price <= account:
                break
            else:
                print('您没有这么多的资产!')

        one = randint(1, 6) 
        two = randint(1, 6)
        first = one + two

        print('玩家第一次摇出了%i点和%i点，总共%i点' % (one, two,first))
        if first == 6 or first == 11:
            print('玩家胜!')
            account += price 
        #return True
        elif first == 2 or first == 3 or first == 12:
            print('玩家输!')
            acount -=price
            # return False
        else:
            while True:
                s_one = randint(1, 6)
                s_two = randint(1, 6)
                second = s_one + s_two
                print('玩家摇出了%i点和%i点，总共%i点' % (s_one, s_two,second))
                if first == second:
                    print('玩家胜')
                    account += price 
                    break
                    # return True
                elif second == 7:
                    print('玩家输')
                    account -=price
                    break
                    # return False
    print('您没有资产了！！')
""" def countCraps():
    count = 0 
    for _ in range(1000):
        if craps():
            count += 1
    print(count) 
countCraps()
"""

craps()


""" 
#斐波那契数列
# f(1) = 1, f(2) = 2, fn = f(n-1) + f(n-2)
def fib():
    pre = 0
    next = 1
    for num in range(10):
        # fib = pre + next
        # pre, next = next, fib
        pre, next = next, pre + next
        print(fib, end=' ')

fib()
 """


""" 
# 百钱百鸡  公鸡五钱，母鸡三钱， 三个小鸡一钱
def hundred():
    # 5x + 3y + z = 100
    # x + y + 3z = 100

    for x in range(20):
        for y in range(33):
            z = 100 - 5 * x - 3 * y
            if x + y + z * 3 == 100:
                print('公鸡：%i, 母鸡%i, 小鸡%i' % (x, y, 3 * z))
            # for z in range (34):
            #     if 5 * x + 3 * y + z == 100 and x + y + 3 * z == 100:
            #         print('公鸡：%i, 母鸡%i, 小鸡%i' % (x, y, 3 * z))

hundred()
 """



""" 
# 水仙花数。
def lily():
    for num in range(100, 1000):
        low = num % 10
        mid = num // 10 % 10 
        big = num // 100

        if num == low ** 3 + mid **3 + big ** 3:
            print(num) 

lily() """
""" 
# 完美数
def perfect():
    for num in range(1, 10000):
        count = 0   
        for i in range(1, num):
            if num % i == 0:
                count += i
        
        if num == count:
            print(num)

perfect() """