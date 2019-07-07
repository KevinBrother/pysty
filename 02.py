# utf-8

# 语言元素： 指令和程序，变量和类型
# 运算符


""" # 更具半径计算圆的周长和半径
def printPnA():
    import math
    radius = float(input('请输入半径：'))
    perimeter = radius * math.pi
    area = radius * radius * math.pi
    print('周长为：%.2f' % perimeter)
    print('面积为：%.2f' % area) 

printPnA()
 """


# 是否为闰年
def is_leap():
    year = int(input('请出入年份： '))
    isLeap = (year % 4 == 0 and year % 100 != 0 or
              year % 400 == 0)
    if isLeap:
        print('%i是闰年' % year)
    else:
        print('%i不是闰年' % year)

is_leap()

# 进入该目录下 控制台输入下面命令即可 
# python 01.py