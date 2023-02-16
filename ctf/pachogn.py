# coding:utf-8
import requests
import urllib3
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

r = requests.get(url="https://vidar.club/member",verify=False )
print(r)
soup = BeautifulSoup(r.content,'lxml')
a = soup.select('.member__intro > p ')
print(r.content)
# print(a)
# for i in a:
#     resdate = []
#     herourl = "https://pvp.qq.com/web201605/" + i['href']
#     heroname = i.text
#     resdate.append(heroname)
#     r1 = requests.get(url=herourl,headers=h,verify=False)
#     soup1 = BeautifulSoup(r1.content,'lxml')
#     a2 = soup1.select('.skill-name > b')
#     for j in a2:
#         resdate.append(j.text)
#     print(resdate)



