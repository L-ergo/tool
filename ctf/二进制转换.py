# coding:utf-8
f = open('a.txt','rb')
line = f.readline()
s = line.decode(encoding='utf-8')
print(s)
f.close()