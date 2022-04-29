n=input()
n=n.lower()
n=n.split()
count=1
for d in n[0]:
    c=0
    for i in range(1,len(n)):
        if d in n[i]:
            c+=1
    if c==len(n)-1:
        print(d,end='')
        count=0
if count:
    print('-1')
 