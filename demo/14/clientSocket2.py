from socket import socket
from json import loads
from base64 import b64decode

def main():
    client = socket()
    client.connect((('192.168.1.149', 6789)))

    # 定义一个保存二进制数据的对象
    in_data = bytes()
    in_data = client.recv(1024)
    # 由于不知道服务器发送的数据有多大每次接受1024字节
    data = client.recv(1024)
    while data:
        in_data += data
        data = client.recv(1024)
    # 将接受到的二进制数据解码成JSON字符串
    # 并转换成字典
    my_dict = loads(in_data.decode('utf-8'))
    filename = my_dict['filename']
    filedata = my_dict['filedata'].encode('utf-8')
    
    with open('../../static/'+filename, 'wb') as f:
        # 将base64格式的数据解码成二进制数据并写入文件
        f.write(b64decode(filedata))
        f.close()
    print('图片已保存')
    client.close()




if __name__ == "__main__":
    main()