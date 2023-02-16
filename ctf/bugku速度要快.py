# coding:utf-8
import requests
import base64
url = "http://114.67.175.224:15726/"
session = requests.Session()
myrequests = session.get(url)   # 记录下session
header_flag = myrequests.headers['flag']
header_flag_decode = base64.b64decode(header_flag)  # python3这个操作会导致生成bytes对象，python2直接可以使用decodestring
header_flag_decode = header_flag_decode.decode()    # 因为上一步解码时生成了bytes类型对象，需要转化为string，decode()默认编码是utf-8
margin_value = header_flag_decode.split(": ")[1]    # 取他说的flag内容，作为margin参数值
page = session.post(url, {"margin": base64.b64decode(margin_value)})
print(page.text)
# 上面decode两次是因为python加密base64的原理问题，需要经过一次utf-8，不行就百度一下