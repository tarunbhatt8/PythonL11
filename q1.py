'''
Q.1- Name and handle the exception occured in the following program: 

a=3
 if a<4:
    a=a/(a-3)
     print(a)

'''

#the exception yhe program is Zero Division Error
# it occurs when during the execution flow, something gets divided by 0

try:
	a=3
	if a<4:
		a=a/(a-3)
		print(a)
except ZeroDivisionError:
	print('There was an Exception:\nSomething got divided by zero')
	