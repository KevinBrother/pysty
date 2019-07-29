# coding: utf-8

from socket import socket, SOCK_STREAM, AF_INET
from datetime import datetime
from threading import Thread
from json import dumps
from base64 import b64encode

# 下面我们来设计一个使用多线程技术处理多个用户请求的服务器，该服务器会向连接到服务器的客户端发送一张图片。

def main():

    #自定义线程类
    class SendPic(Thread):
        def __init__(self, cclient):
            super().__init__()
            self._cclient = cclient

        def run(self):
            myPic = {}
            myPic['filename'] = 'sendTest.png'
            # JSON是纯文本不能携带二进制数据
            # 所以图片的二进制数据要处理成base64编码
            myPic['filedata'] = data
            # 通过dumps将字典变成JSON字符串
            json_str = dumps(myPic)
            # 发送json字符串
            self._cclient.send(json_str.encode('utf-8'))
            self._cclient.close()

    # 1.创建套接字对象并制定传输服务
    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 2.绑定ip地址和端口
    server.bind(('192.168.1.149', 6789))
    # 3. 开启监听-监听客户端连接到服务器
    server.listen(512)
    print('服务器启动开始监听...')
    with open('../../static/test1.png', 'rb') as f:
        # 4. 将二进制数据处理成base64再解码成字符串
        data = b64encode(f.read()).decode('utf-8')
    while True:
        client, addr = server.accept()
        print(str(addr) + '连接到了服务器.')
        SendPic(client).start()


if __name__ == '__main__':
    main()