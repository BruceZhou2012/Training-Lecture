 #coding:utf-8
'''
d = [1,2,3]
try:
    ''.join(d)
    d.chunjie()
    print '11111'
except TypeError,e:
    print "type error"
except AttributeError,e:
    print 'AttributeError error'
else:
    print 'succes'
finally:   ## 必须是放置异常处理最后一句
    print "running"

'''
d = [1,2,3]
''.join(d)
#except (TypeError,AttributeError),e:
    #print e
#    print '该方法不能在列表中操作'


'''
d = [1,2,3]
try:
    ''.join(d)
    print '11111'
except: # # 如果什么都不写 捕获所有的错误
    print '该方法不能在列表中操作'
d = [1,2,3]
try:
    ''.join(d)
    print '11111'
except Exception: # # 如果什么都不写 捕获所有的错误
    print '该方法不能在列表中操作'
'''