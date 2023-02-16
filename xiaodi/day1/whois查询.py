# coding:utf-8
# whois查询
# 第三方库进whois查询
# 利用网上接口查询
from whois import whois
data = whois("www.xiaodi8.com")
print(data  )