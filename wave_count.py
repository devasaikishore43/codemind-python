n=int(input())
l=list(map(int,input().split()))
c=1
if l[1]-l[0]>0:
    for i in range(n-1):
        if l[i+1]-l[i]>0 and i%2==0:
            continue
        if l[i]-l[i+1]>0 and i%2:
            continue
        c=0
        break
if l[1]-l[0]<0:
    for i in range(n-1):
        if l[i]-l[i+1]>0 and i%2==0:
            continue
        if l[i+1]-l[i]>0 and i%2:
            continue
        c=0
        break
if c:
    if n%2:
        print(n//2)
    else:
        print((n//2)-1)
else:
    print('-1')