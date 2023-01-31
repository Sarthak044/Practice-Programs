#push zeroes to end [0,9,6,5,0,3,4,0,1]
#output-[9,6,5,3,4,1,0,0,0]
def pushzeroestoend(li):
    nz=0
    for i in range(len(li)):
        if li[i] != 0:
            li[nz] = li[i]
            nz+=1
    
    while nz < 9:
        li[nz] = 0
        nz += 1
    print(li)

li = [0,9,6,5,0,3,4,0,1]
pushzeroestoend(li)

