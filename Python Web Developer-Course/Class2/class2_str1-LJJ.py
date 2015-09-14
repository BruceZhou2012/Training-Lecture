#!/usr/bin/python

a=raw_input("Please input a string: ")
b=list(a)
c=list(set(a))
if len(b) == len(c):
    print False
else:
    print True
