#!/usr/bin/env python
#coding:utf8
#实现一个脚本,,接受一个字符串参数，判断字符串是否是回文

str = raw_input("Please input a string:")

str1 = str[::-1]

if str == str1:
    print "Your's string is huiwen"
else:
    print "Your's string is not huiwen"



