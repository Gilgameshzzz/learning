# Filename  : 02-socketClient.py
# Date  : 2018/8/7
import socket

if __name__ == '__main__':


    while True:
        # 1、创建套接字对象
        client = socket.socket()

        # 2、连接服务器
        client.connect(('10.7.181.83', 8080))

        # 3、接收信息
        data = client.recv(1024)
        print('接收到服务器的数据', data.decode(encoding='utf-8'))

        # 4、发送信息
        str1 = input('>>>')
        client.send(str1.encode(encoding='utf-8'))