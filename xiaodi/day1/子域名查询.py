# coding:utf-8
import socket
import time
# 子域名查询
# 1.利用字典加载爆破进行查询
# 2.利用bing或第三方接口进行查询
def zym_check(url):
    urls = url.replace('www','')
    for zym_data in open('zd'):
        zym_data = zym_data.replace('\n', '')
        url = zym_data + urls
        try:
            ip = socket.gethostbyname(url)
            print(url+'       '+ip)
            time.sleep(0.1)
        except Exception as e:
            pass
            time.sleep(0.1)
if __name__ == '__main__':
    zym_check('www.xueersi.com')