nums = [0, 4, 7, 2, 1, 0 , 9 , 3, 5, 6, 8, 0, 3]

def add(n=0):
    n = n + 5
    return n

x = map ( add, nums)
print(list(x))
