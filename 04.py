#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#打印三角形图案
def printTriangle():
    num = int(input('打印几行的三角？'))
    for x in range(num):
        for y in range(num):
          if 1 < 0:
            i = 1 + 1
            print(' ', end = '')
          else:
            print('*')

    """ for x in range(1, num+1):
        #print('这是第%i行', x)
        for y in range(0, x):
            print('*', end='')
        print('\n') """

printTriangle()  

""" 
# 循环结构 for-in 和 while

def maxAppAndMinMult():
    num1 = int(input('输入第一个数字：'))
    num2 = int(input('输入第二个数字：'))

    maxApp = 1
# 找出能被两个数整除的数，
# 最大公约数是所有被整除的数的乘机
# 最小公倍数是再乘以两个数剩余的部分

    if num1 > num2:
        num1, num2 = num2, num1    

    for x in range(num1-1, 1, -1):
        print(x)
        if num1 % x == 0 and num2 % x == 0:
            print('输出值啊 ')
            num1 = num1 / x
            num2 = num2 / x
            maxApp = maxApp * x

    litMult = maxApp * num1 * num2    
    print('最大公约数： %i' % maxApp)
    print('最小公倍数： %i' % litMult)
    print('最小公倍数： %i' % (maxApp * num1 * num2))
        
maxAppAndMinMult() 
 """

""" 
# 输入一个数 是不是素数
def isPrime():
    num = int(input('请输数字： '))

    if(num < 2):
        print('请输入大于1的正整数!')

    is_prime = True

    for x in range(2, num - 1): 
        if num % x == 0:
            is_prime = False
            break
        else:
            x += 1

    if is_prime:
        print('%i是素数！' % num)
    else:
        print('%i不是素数！' % num)

isPrime() """

    
            
    
""" 
# 猜一百以内的数
def inHun():

    from random import randint
    mun = randint(1, 100)
    
    count = 0
    while True:
        value = int(input('请输入100以内的数：'))
        count += 1 
        if value > mun:
            print('小一点！')
        elif value < mun:
            print('大一点！')
        else:
            print('猜对啦！')
            print('您一共猜了%d次！' % count)
            break

    if count > 7:
        print('您的智商余额不足，请充值！')
    
inHun()     """




""" 
# 一百以内的偶数相加    
def evenAdd():
    sum = 0
    for x in range(2, 101, 2):
        sum += x
    
    print(sum)

evenAdd()

 """