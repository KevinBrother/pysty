#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#craps赌博游戏
#两个骰子 第一次和为7或11 玩家胜，和为2、3、12玩家输
# 如果是其他数字，记录第一次的和，再次投掷至和第一次的值一样，玩家胜，
# 如果投掷出和为7，则玩家输

def craps():
    from random import randint
    one = randint(1, 7) 
    two = randint(1, 7)
    first = one + two

    if first == 7 or first == 11:
       # print('玩家胜!')
        return True
    elif first == 2 or first == 3 or first == 12:
       # print('玩家输!')
        return False
    else:
        while True:
            s_one = randint(1, 7)
            s_two = randint(1, 7)
            second = s_one + s_two

            if first == second:
                #print('玩家胜')
                #break
                return True
            elif second == 7:
                #print('玩家输')
                #break
                return False

def countCraps():
    count = 0 
    for _ in range(1000):
        if craps():
            count += 1
    print(count)
countCraps()
# craps()


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