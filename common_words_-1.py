n=input()
m=input()
n=n.lower()
m=m.lower()
n=n.split(' ')
m=m.split(' ')
c=0
for d in n:
    if d in m:
        c+=1
print(c)