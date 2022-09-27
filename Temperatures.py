def temp(temp):
    for i in range(len(temp)):
        c=0
        for j in range(i+1,len(temp)):
            if temp[i] < temp[j]:
                c=1
                break
        if c:
            temp[i] = j-i
        else:
            temp[i]=0
    return temp     
a=int(input())
l=list(map(int,input().split()))
print(*temp(l))