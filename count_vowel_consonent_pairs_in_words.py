n=input()
n=n.lower()
n=n.split(' ')
z=['a','e','i','o','u']
c=0
for d in n:
    for i in range(len(d)//2):
        if d[i] in z and d[len(d)-(i+1)] not in z:
            c+=1
        if d[i] not in z and d[len(d)-(i+1)] in z:
            c+=1
print(c)