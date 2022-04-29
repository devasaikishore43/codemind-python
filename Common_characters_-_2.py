n=input()
n=n.lower()
n=n.split()
count=0
for d in n[0]:
    c=0
    for i in range(1,len(n)):
        if d in n[i]:
            c+=1
    if c==len(n)-1:
        count+=1
print(count)    