'''
Q.2- Name and handle the exception occurred in the following program: 
l=[1,2,3]
print(l[3])
'''

#the eception ocuring in the program is Index Error
#it occurs when we try to access a non exixting index in any object


try:
    l=[1,2,3]
    print(l[3])
except IndexError:
        print('Exception Handled:\nThe program tried to access a non existing Index')
