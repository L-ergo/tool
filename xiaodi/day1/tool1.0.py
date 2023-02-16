# coding:utf-8
import argparse
import socket
import os
import time
from whois import whois

def ip_check(url):
    cdn_data = os.popen('nslookup ' + url).read()
    x = cdn_data.count('.')
    if x > 11:
        print("存在CDN")
    else:
        print("不存在CDN")
        ip = socket.gethostbyname(url)
        print("此域名的ip为：" + ip)
    print('\n\n\n')
def port_check(url,ports):
    print('你查询的端口如下：\n\n')
    ports = list(ports.split(','))
    for i in range(len(ports)):
        ports[i] = int(ports[i])
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    for port in ports:
        request = server.connect_ex((url, port))
        if request == 0:
            print(str(port) + ' is open')
        else:
            print(str(port) + ' is close')
    print('\n\n\n')
def whois_check(url):
    print('你查询whois信息如下：\n\n')
    data = whois(url)
    print(data)
    print('\n\n\n')
def zym_check(url):
    print('你查询的子域名如下：\n\n')
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
    parser = argparse.ArgumentParser(description='小工具')
    parser.add_argument('-ip', type=str, help='输入域名，查询IP')
    parser.add_argument('-port', type=str, help='请输入域名，端口')
    parser.add_argument('-z',type=str,help='请输入域名,查询子域名')
    parser.add_argument('-who',type=str,help='请输入域名，查询whois')
    args = parser.parse_args()
    if args.ip:
        ip_check(args.ip)
    if args.ip and args.port:
        port_check(args.ip,args.port)
    if args.z:
        zym_check(args.z)
    if args.who:
        whois_check(args.who)

