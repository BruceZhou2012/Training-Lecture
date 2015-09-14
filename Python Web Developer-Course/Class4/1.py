__author__ = 'gubaoer'


X = ( lambda  a = 'chunhong',b='qingwen',c='junjie':a + b +c )
print X('gbe')


def student():
    title = 'sir'
    action = ( lambda x : title + ' ' + x)
    return action
act = student()
print act('Boyle')


'''
lambda x : title + ' ' + x

def student():
    title = 'sir'
    def x(name):
        return title + name
    action = x(name)

'''
