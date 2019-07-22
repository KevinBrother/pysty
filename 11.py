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

def jsonTest():
    import json

    mydict = {
        'key1': 'value1',
        'key2': 'v2',
        'age': 12,
        'name': '张三',
        'friends': ['李四', '王五'],
        '家庭成员': [
            {
                '父亲': '张狗蛋',
                '母亲': '张氏'   
            }
        ]
    }

    try:
        with open('./static/data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
            # json.dump(json.dumps(mydict), fs)
    except IOError as e:
        print(e)
    print('数据保存完成！')

def requestJson():
    import requests, json

    resp = requests.get('http://api.tianapi.com/guonei/?key=16508bc4c0816c304c76d16246a8e3d3&num=10')
    data_model = json.loads(resp.text)
    for news in data_model['newslist']:
        print(news['title'])


def mian():
    # fileTest()
    # byteTest()
    # jsonTest()
    requestJson()
    pass


if __name__ == "__main__":
    mian()