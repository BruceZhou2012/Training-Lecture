#!/usr/bin/env python
#coding:utf8
#如果a = [1,2,3],b=[3,2,1],把这两个列表中的元素一一对应求和，并返回一个新列表

a = [1,2,3]
b = [3,2,1]
newlist = []
'''for i in a:
    for t in b:
        s = i + t
        newlist.append(s)
print sorted(newlist)'''


aaa = zip(a,b)
for i in aaa:
    num = i[0] + i[1]
    newlist.append(num)
print newlist





