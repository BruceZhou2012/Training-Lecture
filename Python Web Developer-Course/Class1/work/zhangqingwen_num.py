#!/usr/bin/python env

print 'Select operation. '
print '1. Add'
print '2. Subtract'
print '3. Multiply'
print '4. Divide'

SELECT_NUM = int(raw_input("Enter choice (1/2/3/4): "))
if SELECT_NUM==1 or SELECT_NUM==2 or SELECT_NUM == 3 or SELECT_NUM == 4:
    if SELECT_NUM==1:
        NUM1 = int(raw_input("Enter first number: "))
        NUM2 = int(raw_input("Enter second number: "))
        SUM=NUM1+NUM2
        print "%d + %d = %d " % (NUM1,NUM2,SUM)
    elif SELECT_NUM==2:
        NUM1 = int(raw_input("Enter first number: "))
        NUM2 = int(raw_input("Enter second number: "))
        SUM=NUM1-NUM2
        print "%d - %d = %d " % (NUM1,NUM2,SUM)
    elif SELECT_NUM==3:
        NUM1 = int(raw_input("Enter first number: "))
        NUM2 = int(raw_input("Enter second number: "))
        SUM=NUM1*NUM2
        print "%d * %d = %d " % (NUM1,NUM2,SUM)
    elif SELECT_NUM==4:
        NUM1 = int(raw_input("Enter first number: "))
        NUM2 = int(raw_input("Enter second number: "))
        SUM=NUM1/NUM2
        print "%d / %d = %d " % (NUM1,NUM2,SUM)




