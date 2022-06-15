s=input()
a=0
c=0
for d in s:
    if d == 'L':
        a+=1
    else:
        a-=1
    if a==0:
        c+=1
print(c)