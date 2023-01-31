#Armstrong no. is a number whose sum of digit is equal to itself

#abc=a^n+b^n+c^n=abc

#n=no. of digits of the number 

#if 153= 1*1*1+5*5*5+3*3*3=153

#so 153 is a armstrong no.
num_1=int(input('Enter the no. you want to check'))

#initialize sum
sum=0
temp=num_1
while temp>0:
    dig=temp % 10
    sum+=dig**3
    temp//=10
if num_1==sum:
    print('The no. entered is Armstrong')
else:
    print('The entered no. is not armstrong')
