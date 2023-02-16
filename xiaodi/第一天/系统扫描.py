# coding:utf-8
import nmap
# 系统判断
# 1.基于TTL值进行判断
# 2.基于第三方脚本进行判断
# 这里nmap需要在本地配置nmap，才能调用nmap
nm = nmap.PortScanner()
data = nm.scan('www.xiaodi8.com','80,8888','-sV')
print(data)