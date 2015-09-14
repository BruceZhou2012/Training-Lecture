__author__ = 'gubaoer'

class B:
    def name(self):
        print 'haa'


class A(object):
    def name(self):
        print 'haa'
b = B()
a=A()

print type(B)
print type(A)