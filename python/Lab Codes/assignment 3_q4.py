# Calculate sum of squares of first 5 natural numbers using map or reduce fucntions
from functools import reduce
print('Enter the first 5 natural numbers')
x=[]
for i in range(0,5):
    y=int(input())
    x.append(y)

result= reduce(lambda i, j: i +j * j,[x[:1][0]**2]+x[1:] ) 
print('Here is your answer')
print(result)
