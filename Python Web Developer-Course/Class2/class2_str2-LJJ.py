#!/usr/bin/python
#coding=utf8

a=raw_input("Please input a string: ")
if a == a[::-1]:
    print "The string is 回文."
else:
    print "The sting is't 回文."
