m=18
n=8
S = 83
for i in range(0,m):
    if i<2:
        for j in range(0,n):
            print(S + " ")
        print("\t")
        for j in range(0,n):
            print(S + " ")
        T=2
        while T>0:
            print("\t")
            for i in range(0,2):
                print(S + " ")
            for i in range(2,n-2):
                print("  ")
            for i in range(n-2,n):
                print(S + " ")
            T = T - 1
        print("\n")
    elif (i>=2 and i<6):
        for j in range(0,2):
            print(S + " ")
        for j in range(2,n):
            print("  ")
        print("\t")
        for j in range(0,2):
            print(S + " ")
        T=2;
        while(T>0):
            print("\t")
            for j in range(0,2):
                print(S + " ")
            for j in range(2,n-2):
                print("  ")
            for j in range(n-2,n):
                print(S + " ")
            T=T-1
        print("\n")
    elif i>=6 and i<8:
        for j in range(0,n):
            print(S + " ")
        print("\t")
        for j in range(0,2):
            print(S + " ")
        for j in range(2,n-2):
            print("  ")
        for j in range(n-2,n):
            print(S + " ")
        T=2
        while (T>0):
            print("\t")
            for j in range(0,n):
                print(S + " ")
            T=T-1
        print("\n")
    elif i>=6 and 1<8:
        for j in range (0,n):
            print(S + " ")
        print("\t")
        for j in range(2,n-2):
            print("  ")
        for j in range(n-2,n):
            print(S + " ")
        T=2
        while(T>0):
            print("\t")
            for j in range(0,n):
                print(S + " ")
            T=T-1
        print("\n")
    elif i>=8 and i<12:
        for j in range(0,n-2):
            print("  ")
        for j in range(n-2,n):
            print(S + "  ")
        print("\t")
        for j in range(0,2):
            print(S + " ")
        for j in range(2,n-2):
            print("  ")
        for j in range(n-2,n):
            print(S +" ")
        T=2
        while(T>0):
            print("\t")
            for j in range(0,n-2):
                print("  ")
            for j in range(n-2,n):
                print(S + " ")
            T=T-1
        print("\n")
    elif i>=12 and i<m:
        for j in range(0,n):
            print(S + " ")
        for j in range(0,n):
            print(S + " ")
        T=2
        while(T>0):
            print("\t")
            for j in range(0,n-2):
                print("  ")
            for j in range(n-2,n):
                print(S + " ")
            T=T-1
        print("\n")