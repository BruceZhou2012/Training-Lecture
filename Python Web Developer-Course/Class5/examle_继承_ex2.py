# coding: utf-8


# 隐式继承
'''
class Parent(object):

    def implicit(self):
        print "PARENT implicit()"

class Child(Parent):
    pass

dad = Parent()
son = Child()
dad.implicit()
son.implicit()
'''

# 显示覆盖
'''
class Parent(object):

    def override(self):
        print "PARENT OVERRIDE"

class Child(Parent):

    def override(self):
        print "CHILD override()"

dad = Parent()
son=Child()

dad.override()
son.override()
'''

# 运行前和运行后的替换
'''
class Parent(object):

    def altered(self):
        print 'Parent altered()'

class Child(Parent):

    def altered(self):
        print "CHILD, BEFORE PAREND ALTERED"
        super(Child, self).altered()
        print "hahahha"
dad = Parent()
son=Child()
#dad.altered()
son.altered()
'''

# 合成
class other(object):

    def __init__(self):
        self.dd = 1
        print self.dd

    def override(self):
        print "other override()"

    def implict(self):
        print "other implicit"

    def altered(self):
        print "other altered()"

class Child(object):

    def __init__(self):
        self.other = other()
        print "df" + str(self.other.dd)

    def implicit(self):
        self.other.implict()

    def override(self):
        print "child override()"

    def altered(self):
        print "sdsdsds"
        self.other.altered()
        print "dddddddddddddddd"

son = Child()
#son.implicit()
#son.override()
