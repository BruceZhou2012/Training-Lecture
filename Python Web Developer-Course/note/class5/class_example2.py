#coding:utf8
__author__ = 'gubaoer'

#1.
class FirstClass(object):
    def setdata(self,value):
        self.data = value
    def display(self):
        print self.data

x = FirstClass()
y = FirstClass()
#print x.__dict__
x.setdata("king arthur")
y.setdata(3.14159)          ##类会产生多个实例，方法必须经过self参数残能获取正在处理的实例
#print x.__dict__
#print x.display()
x.data = 'new value'
print x.display()

#2.
class SecondClass(FirstClass):   ####重载
    def display(self):
        print 'Currend value = "%s"' % self.data

z = SecondClass()
z.setdata('python')
print z.display()

#3.
class ThirdClass(SecondClass):
    def __init__(self,value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return '[ThirdClass:%s]' % self.data

    def mul(self,other):
        self.data = self.data * other

a = ThirdClass('abc')
a.display()
print a
b = a + 'xyz'
print b.display()