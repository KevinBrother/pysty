#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fileTest():
    f = None
    try:
        f = open('c:\\Users\\heheda\\Desktop\\test.py', 'r', encoding='utf-8')
        print(f.read())
    except FileNotFoundError:
        print('无法打开指定的文件！')
    except LookupError:
        print('指定了位置的编码！')
    except UnicodeDecodeError:
        print('读取文件时解码错误！')
    finally:
        if f:
            f.close()

def byteTest():
    try:
        with open('./static/test1.png', 'rb') as fs1:
            data = fs1.read()
            # print(data)
        with open('./static/fromTest1.png', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('无法打开指定的文件', e)
    except IOError as e:
        print('读写文件时发生错误', e)
    print('程序执行结束')




def mian():
    # fileTest()
    byteTest()
    pass

if __name__ == "__main__":
    mian()