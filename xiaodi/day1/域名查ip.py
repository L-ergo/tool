# coding:utf-8
import socket
import os

# 域名反查ip
# ip = socket.gethostbyname('www.xiaodi8.com')
# print(ip)


# 识别目标是否存在CDN
# 通过nslookup执行结果进行返回IP解析数目判断
# 利用python去调用执行系统命令
# cdn_data = os.system('nslookup www.xiaodi8.com')
# # system缺点：只能输出结果，不能对结果进行操作
# print(cdn_data)

# 可以使用
ym = input("请输入域名：")
cdn_data = os.popen('nslookup '+ ym).read()
x = cdn_data.count('.')
if x > 11:
    print("存在CDN")
else:
    print("不存在CDN")
    ip = socket.gethostbyname(ym)
    print("此域名的ip为："+ip)