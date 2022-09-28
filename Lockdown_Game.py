a=int(input())
b=input()
c=len(b)
l = [i for i in range(1,a+1)]
i,j=0,0
count=0
while a!=1:
    if b[j]=="y":
        l.pop(i-count)
        count+=1
    i+=1
    j+=1
    if i==a:
        a-=count
        count=0
        i=0
    if j==c:
        j=0
print(*l)