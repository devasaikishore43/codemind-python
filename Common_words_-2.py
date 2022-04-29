n=input()
m=input()
n=n.split(' ')
m=m.split(' ')
c=0
for d in n:
    if d in m:
        c+=1
    count=0
    for j in m:
        if d==j:
            count+=1
    if count>1:
        c-=1
    count=0
    for j in n:
        if d==j:
            count+=1
    if count>1:
        c-=1
print(c)