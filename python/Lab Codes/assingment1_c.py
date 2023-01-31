#Q) Find the factorial of a number. Take the number from the keyboard as input from the user.

#via math module
import math 
a=int (input('Enter the number you want to factorial for'))
print(math.factorial(a))

#via normal looping
a=int(input('Enter the no.'))
fact=1
for i in range(1,a+1):
    fact=fact*i
print(fact)


