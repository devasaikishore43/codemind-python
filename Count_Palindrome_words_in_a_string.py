n=input()
n=n.lower()
n=n.split(' ')
c=0
for d in n:
    if d==d[::-1]:
        c+=1
print(c)