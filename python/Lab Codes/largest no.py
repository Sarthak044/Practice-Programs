#FOR 2 NUMBERS
#first no. input
a_1=int(input('Enter the first number\n'))
#second no. input
a_2=int(input('Enter the second number\n'))

if a_1>a_2:
    print('First No. entered is the largest')
elif a_2>a_1:
    print('Second no. entered is the largest')
elif a_1==a_2:
    print('Numbers are equal')
else:
    print('***Not valid***')

#FOR 3 NUMBERS
b_1=int(input('Enter the first number\n'))
b_2=int(input('Enter the second number\n'))
b_3=int(input('Enter the third number\n'))
if b_1>b_2 and b_1>b_3:
    print('First number is the greatest')
elif b_2>b_1 and b_2>b_3:
    print('Second number the largest')
elif b_3>b_2 and b_3>b_1:
    print('Third Number is the largest')