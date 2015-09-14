#coding:utf8
# __author__ = 'gubaoer'

'''
class Dog(object):
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def dark(self):
        print '汪汪汪,我是%s' %(self.name)

dog1 = Dog('chunhong','yellow')
print dog1.dark()
'''
'''
class Dog(object):
    def setname(self,name):
        self.name = name
    def setcolor(self,color):
        self.color = color
    def bark(self):
        print '汪汪汪,我是%s' %(self.name)

class GuideDog(Dog):
    def __init__(self,name):
        Dog.setname(self,name)
    def guide(self):
        print "我正在引导我的主人"

gDog1 = GuideDog('忠诚卫士')
print gDog1.bark()
print gDog1.guide()
'''



class Dog(object):
    def __init__(self,name):
        pass
