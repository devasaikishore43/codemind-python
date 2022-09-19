a= int(input())
b = list(map(int,input().split()))
b.sort()
i = 0
l=[]
count = 0
while i<(a-1):
    if b[i]==b[i+1]:
        i+=1
    else:
        count+=1
        l.append(b[i])
    i+=1
if count == 1:
    print(l[0],b[-1])
else:
    
    print(*l)