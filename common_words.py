n=input()
m=input()
n=n.lower()
m=m.lower()
n=n.split(' ')
m=m.split(' ')
for d in m:
    if d in n:
        print(d,end=' ')