a=int(input())
l=list(map(int,input().split()))
i,j=0,a-1
while i<j:
    if l[i]==1:
        l[j],l[i]=l[i],l[j]
        j-=1
    else:
        i+=1
print(*l)