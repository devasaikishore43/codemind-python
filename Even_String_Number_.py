n=input()
z=[]
c=0
for i in range(len(n)):
    if n[i] in z:
        continue
    if n[i].isdigit():
        if int(n[i])%2==0:
            c=1
        z.append(n[i])
if c:
    z.sort()
    for i in range(len(z)):
        if int(z[i])%2==0:
            a=z[i]
            z.pop(i)
            break
    z=z[::-1]
    z.append(a)
    for i in range(len(z)):
        print(z[i],end='')
else:
    print('-1')
