__author__ = 'gubaoer'




def isDuplicate(s):
    t1 = len(s)
    t2 = len("".join(set(s)))
    if t1 == t2:
        return False
    else:
        return True

def isPalindrome(s):
    return s == s[::-1]



a = [1,2,3]
b=[3,2,1]

c = []
for i in zip(a,b):
    d = i[0] + i[1]
    c.append(d)
print c