# 数据类型
   # 字符串： 可任意变化  str1 = 'abc'
   # 列表： 可任意变化  list1 = [1, 2, 3]
   # 元祖： 不可修改   tuple1 = [1, 2, 3]
   # 集合： 不许有重复元素  set1 = {1, 2, 3, 3, 2}
    # 字典：  键值对  age = {'小李': '26', '小明': '21'}


# 字符串
def strs():

    str1 = 'hello world'

    # find
    print(str1.find('ll'))
    print(str1.find('le'))

    # index 和find类似 但是index找不到 会抛出异常
    print(str1.index('ll'))
    print(str1.index('le'))

    # 切片


def lists():

    # 列表
    """  list1 = [1, 3, 5, 100]
    print(list1)

    list2 = ['hello'] * 5
    print(list2)

    list1.append(200)
    print(list1)

    list1.insert(1, 400)
    print(list1)

    list1 += [1000, 2000]
    print(list1)
    print(len(list1))

    list1.remove(400)  # 移除列表中的某个元素
    print(list1)

    del list1[4]
    print(list1)

    list1.clear()  # 清空列表元素
    print(list1)
    """

    """
    list1 = ['orange', 'apple', 'zoo', 'internationalization', 'blueberry']
    list2 = sorted(list1)
    # sorted函数返回列表排序后的拷贝不会修改传入的列表
    # 函数的设计就应该像sorted函数一样尽可能不产生副作用
    list3 = sorted(list1, reverse=True)
    # 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表顺序
    list4 = sorted(list1, key=len)

    print(list1)
    print(list2)
    print(list3)
    print(list4)

    # 直接在列表对象上修改
    list1.sort(reverse=True)
    print(list1)
    """

    """
    import sys

    f = [x for x in range(1, 10)]
    print(f)
    f = [x + y for x in 'ABCDE' for y in '1234567']
    print(f)

    f = [x ** 2 for x in range(1, 1000)]  # 列表生成表达式  耗费内存
    print(sys.getsizeof(f))  # 查看对象占用内存的字节数

    f = (x ** 2 for x in range(1, 1000)) # 列表生成器对象
    print(sys.getsizeof(f))  # 需要的时候再调用内部运算获得数据，耗费时间
 	"""

    def getNum(n):
        for x in range(n):
            yield x

    for x in getNum(3):
        print(x)

        # 集合


def setTest():
    set1 = {1, 2, 3, 3}
    print(set1)

    set2 = set(range(1, 10))
    print(set2)
    set1.add(4)
    set1.add(5)
    print(set2)
    set1.update([11, 12])
    print(set2)


def mapTest():
    scores = {'小李': 26, '小明': 21}
    print(scores['小李'])
    # 对字典进行遍历(遍历的其实是键再通过键取对应的值)
    for elem in scores:
        print('%s\t--->\t%d' % (elem, scores[elem]))

    scores['白元芳'] = 65
    scores['诸葛王朗'] = 71
    scores.update(冷面=67, 方启鹤=85)
    print(scores)
    print(scores.get('武则天'))
    print(scores.get('武则天', 60))

    print(scores.popitem())
    print(scores)
    print(scores.pop('骆昊', 100))
    print(scores)


def main():
    def runHouse():
        # 跑马灯
        import os
        import time

        context = '曹佳丽是大笨蛋！！！'

        while True:
            os.system('clear')  # os.system('cls')
            print(context)

            time.sleep(0.2)  # 休眠 200毫秒

            context = context[1:] + context[0]

    # runHouse()

    def checkCode(code_len=4):

        from random import randint

        # 生成指定长度的验证码，由字母和数字组成
        numAndChar = '0123456789abcdefghijklmnopqrstuvwxyz'
        code = ''

        for _ in range(code_len):
            index = randint(0, len(numAndChar)-1)
            code += numAndChar[index]

        print(code)
        return code

    # checkCode(6)

    def getLastName(fName):
        # 返回给定文件的后缀名
        pos = fName.find('.')
        lastName = fName[pos:]
        print(lastName)

        """  import re
        lastName = re.findall('\..*$', fName)

        if len(lastName) == 0:
            print('请输入正确的文件名')
        else:
            print(lastName)
            return lastName """

    # getLastName('ddd.mp4')

    def biggestAndNext(list1):

        list1.sort(reverse=True)

        for i in range(0, len(list1)):
            if i == 2:
                return
            print(list1[i], end=' ')

    # biggestAndNext([2,1,-5])

    def dayOfdate(date):  # 1991-01-02  # which_day(year, month, date):
        # 输入年月日 输出是今年的第几天
        year = int(date[0: 4])
        isRun = False
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            isRun = True

        # 判断是不是闰年
        mDay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        day = 0

        for i in range(int(date[5: 7])):
            day += mDay[i]
            if i == 1 and isRun:
                day += 1

        day += int(date[8:])

        print(day)
        return day

    # dayOfdate('1991-01-02')

    def yhSan():
        # 第二行还是除了第一和最后一个都是上一行的前一位加上后一位的和
        num = int(input('请输入行数：'))
        yh = [[] for i in range(num)]   # num = 2
        for i in range(num):   # i = 0, 1, 2
            for j in range(i + 1):  # j = 0, 1, 2
                # print('i和j分别是： %i, %i' % (i, j))
                if j == 0 or j == i:
                    yh[i].append(1)
                else:
                    yh[i].append(yh[i-1][j-1] + yh[i-1][j])

        print('yh 数组为:', yh)
        # 每行的列是 2n + 1
        # 每行的开始 是 n-i-1 开始 i是行数
        for i in range(num):  #  打印 行数
            for _ in range(num - i - 1):  # 打印前空几格
                print(' ', end='')
            for j in range(len(yh[i])):  #  开始打印的长度由二维数组里面的长度决定
                print(yh[i][j], end='')
                print(' ', end='')
            print()

    # yhSan()

    from random import randint, sample
    def dubMon(choses): 
        # 双色球选号
        # 每注号由七组数字组成
        # 六个红色球，范围 1-33
        # 1个蓝色球，范围 1-16
        # 一等奖 七个号一样   一千万
        # 二等奖 六个红球一致   五百万
        # 三等奖 五红一篮   3000
        # 四等奖 五红或四红一篮   200
        # 五等奖 四红或三红一篮  10 
        # 六等奖 一篮   5元

        red_balls = [x for x in range(1, 34)]
        rball = sorted(sample(red_balls, 6))
        bball = randint(1, 16)
        # rball = [14, 12, 33, 4, 2, 1]
        # bball = 9

        redNum = 0
        blueNum = 0
        
        cs_red = sorted(choses[:6])
        for i in range(6):
            for j in range(6):
                if cs_red[i] == rball[j]:
                    redNum += 1
        if bball == choses[6]:
            blueNum = 1
        print('本次的中奖号为：')
        print((' '.join('%s' % dd for dd in rball)), end='')
        print(' | %i ' % bball)

        if redNum == 6: 
            if blueNum == 1:
                print('恭喜获得一等奖：获得一千万奖金')
            else:
                print('恭喜获得二等奖：获得五百万奖金')
        elif redNum == 5: 
            if blueNum == 1:
                print('恭喜获得三等奖等奖：获得3000元奖金')
            else:
                print('恭喜获得四等奖：获得200元奖金')
        elif redNum == 4: 
            if blueNum == 1:
                print('恭喜获得四等奖：获得200元奖金')
            else:
                print('恭喜获得五等奖：获得10元奖金')
        elif redNum == 3 and blueNum == 1:
            print('恭喜获得五等奖：获得10元奖金')
        elif blueNum == 1:
            print('恭喜获得六等奖：获得5元奖金')
        else: 
            print('很遗憾，您没有中奖，再接再厉！')

    dubMon([14, 12, 33, 4, 2, 1, 9])

if __name__ == '__main__':
   # str()
   # list()
   # setTest()
   # mapTest()
    main()
