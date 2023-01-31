'''
Mr. Pr can choose to move c or d units in 1 second. 
If Mr. Pr moves c units then Ms. Ad will move d units and vice versa. 
(Both of them always moved in positive x-direction)

You have to determine if Mr. Pr can meet with Ms. Ad after some integral amount of time, given that Mr. Pr chooses optimally.
Note that meeting after a fractional amount of time does not count.
'''
#Input to take 
'''
First line will contain T, number of testcases. Then the testcases follow.
Each testcase contains four space separated integers, a, b, c, and d.
'''
#output to take
'''
For each test case, output a single line containing "YES" if Mr. Pr meets with Ms. Ad, otherwise "NO".
'''
for i in range(int(input(''))):
    a,b,c,d =[int(x) for x in input().split()]
    if a==b:
        print("YES")
    elif c==d:
        print("NO")
    elif abs(a-b) % abs(c-d) == 0 :
        print("YES")
    else:
        print("NO")