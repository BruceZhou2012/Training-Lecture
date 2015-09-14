#!/usr/bin/env python
#coding:utf8
#实现一个脚本接受一个字符串，判断这个字符串是否含有重复的字符（包括空格），如果有的话函数返回True，没有的话返回False

str = raw_input("Please input a string:")

N1 = len(str)
N2 = len(set(str))

if N1 != N2:
    print True
else:
    print False
