# coding:utf-8
import argparse

ports = '2,2,2,2,2'
ports = list(ports.split(','))
print(ports)
print(type(ports))
for i in range(len(ports)):
    ports[i] = int(ports[i])
print(ports)

# parser = argparse.ArgumentParser(description='小工具')
# parser.add_argument('-p', type=str, help='请输入域名，端口')
# args = parser.parse_args()
# print((args.p,type(args.p)))