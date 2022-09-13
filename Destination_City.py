a=int(input())
k={}
for i in range(a):
    l=list(map(str,input().split()))
    if l[0] not in k:
        k[l[0]]=-1
    else:
        k[l[0]]+=1
    if l[1] not in k:
        k[l[1]]=1
    else:
        k[l[1]]-=1
for i,j in k.items():
    if j==1:
        print(i)
