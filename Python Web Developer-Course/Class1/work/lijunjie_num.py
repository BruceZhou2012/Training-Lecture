#!/root/data/env/test1/bin/python

print """Please Select operation:
1.Add
2.Subtract
3.Multiply
4.Divide
""",

choice = raw_input("Enter choice(1/2/3/4): ")
if choice == '1' or choice == '2' or choice == '3' or choice == '4':
    pass
else:
    print "Sorry,input error." 
    exit()

num1 = int(raw_input("Enter first number: "))
num2 = int(raw_input("Enter second number: ")) 

if choice == '1':
    print num1,'+',num2,'=',num1+num2
elif choice == '2':
    print num1,'-',num2,'=',num1-num2
elif choice == '3':
    print num1,'*',num2,'=',num1*num2
else:
    print num1,'/',num2,'=',num1/num2
