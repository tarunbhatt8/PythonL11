'''

Q.5- Write a program to show and handle following exceptions:
1. Import Error
2. Value Error
3. Index Error
'''


from math import *
try:
    
    x=[1,2,3,4,5]
    a=int(input('Enter an Integer: '))
    print(factorial(a))
    print(x[a])
    from tarun import *

except ImportError:
    print("There was an import error, that got handled")

except ValueError:
        print("A value eror just got handled\n You have to enter an INTEGER ONLY")

except IndexError:
    print("An Index error got handled")


