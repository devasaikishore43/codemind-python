a=int(input())
k = 0
for i in range(a):
    for j in range(a):
        if j==0 or j==a-1 or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()