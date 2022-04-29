n=input()
m=input()
n=list(n.lower())
m=list(m.lower())
z=[]
for i in range(97,124):
    if chr(i) in n and chr(i) not in m:
        z.append(chr(i))
    elif chr(i) in m and chr(i) not in n:
        z.append(chr(i))
for d in z:
    print(d,end='')