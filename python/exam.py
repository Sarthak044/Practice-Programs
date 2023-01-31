def largest2(x,x_size):
  if (x_size < 2):  
    print(" Invalid Input ")
    return
  x.sort
  for i in range(x_size-2,-1, -1):
    if (x[i] != x[x_size - 1]) :
        print("The second largest element is",x[i])
    return
    
  print("There is no second largest element")
 

x=[]
for i in range(len(x)):
    var=int(input())
    x.append(var)
    
n = len(x)
largest2(x, n)
 