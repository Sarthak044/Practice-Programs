
#MARKS INPUT
in_1=int (input('Enter no. first of subject\n'))
in_2=int (input('Enter no. of second subject\n'))
in_3=int (input('Enter no. of third subject\n'))
in_4=int (input('Enter no. of fourth subject\n'))
in_5=int (input('Enter no. of fifth subject\n'))

#average 
avg=(in_1+in_2+in_3+in_4+in_5)/5
print('average of the numbers are ',avg)

#total
total=in_1+in_2+in_3+in_4+in_5

#percentage
per=

#grading system
if total>=410:
    print('A')


elif total<=410 & total>=310:
    print('B')

elif total<=310 & total>=210:
    print('C')

elif  total<=210 & total>=110:
    print('D')

elif total<=110 & total>=00:
    print('fail')



