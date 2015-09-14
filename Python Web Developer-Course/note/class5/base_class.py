#coding:utf-8
__author__ = 'gubaoer'

#1
'''
class Person(object):

    def getname(self):
            print 'My name is gubaoer'


gubaoer = Person()
gubaoer.getname()
junjie = Person()
junjie.getname()
'''
#2
'''
class Person(object):

    def getname(self,name):
            print 'My name is %s' %(name)

gubaoer = Person()
gubaoer.getname('gubaoer')

junjie = Person()
junjie.getname('junjie')
'''
#3
'''
class Person(object):

    def __init__(self,name):
        self.Name = name

    def getname(self):
        print self.Name

gubaoer = Person('gubaoer')
gubaoer.getname()

junjie = Person('junjie')
junjie.getname()
'''


#4

class Person(object):

    common = '他们都很优秀'

    def __init__(self,name):
        self.Name = name
        self.__Size = '尺寸很大'


    @staticmethod
    def sex():
        print '他们都很年轻'

    @property
    def hire(self):
        print '发色很黑'


    def getname(self):
        print self.Name

    @property
    def size(self):
        print self.__Size

    @size.setter
    def size(self,value):
        self.__Size = value


gubaoer = Person('gubaoer')
gubaoer.getname()
junjie = Person('junjie')
junjie.getname()
#print gubaoer.common
#print Person.sex()
#print junjie.sex()
print Person.sex
junjie.size = '很小'
print junjie.size




