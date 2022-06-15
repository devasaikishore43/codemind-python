n=int(input())
d=list(map(int,input().split()))
a=[]
b=0
for i in range(n):
    for j in range(i+1,n):
        c=(d[i:j+1])
        e=0
        for k in range(len(c)):
            if c[k] == 1:
                e+=1
            else:
                e-=1
            if e==0:
                a+=[[i,k]]
b=0
f=[]
if len(a):
    for d in a:
        if b < abs(d[0]-d[1]):
            b=abs(d[0]-d[1])
            if d[0]>d[1]:
                f=[d[1],d[0]]
            else:
                f=d
    print(*f)   
else:
    print('-1')

    