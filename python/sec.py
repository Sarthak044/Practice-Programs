
def l_and_sl(l):
    largest=l[0]
    slargest= -1
    for ele in l:
        if ele > largest:
            slargest = largest 
            largest = ele
        elif ele > slargest and ele !=largest:
            slargest=ele
    return largest,slargest

l= [1,9,0,10,9,7,8]
l,sl = l_and_sl(l)
print(l,sl)      
