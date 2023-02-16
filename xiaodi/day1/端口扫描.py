# coding:utf-8
import socket
# 端口扫描
# 1.原生自写socket协议tcp、udp扫描
# 2.调用第三方模块等扫描
# 3.调用系统工具脚本执行
domain = input("please input domain as xxx.com:")
ports = list(input("please input port:").split(' '))
for i in range(len(ports)):
    ports[i] = int(ports[i])
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
for port in ports:
    request = server.connect_ex((domain,port))
    if request == 0:
        print(str(port)+' is open')
    else:
        print(str(port)+' is close')
