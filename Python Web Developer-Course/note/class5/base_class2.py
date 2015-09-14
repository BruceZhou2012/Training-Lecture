__author__ = 'gubaoer'


class Father(object):
        def __init__(self):
                self.hair = 'black'

        def sport(self):
                print 'football'


class Son(Father):
        def __init__(self):
            super(Son,self).__init__()
            self.looks = 'handsome'

        def sport(self):
            Father.sport(self)
            print 'swimming'
class Grandson(Son):
        pass



d1 = Son()

print d1.hair

print d1.sport()

d2 = Grandson()
print d2.hair