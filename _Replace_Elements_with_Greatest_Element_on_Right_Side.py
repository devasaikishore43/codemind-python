a=int(input())
l=list(map(int,input().split()))
for i in range(a-1):
    l[i]=max(l[i+1:])
l[-1]=-1
print(*l)