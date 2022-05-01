n=input()
a=n.split(',')
z=[]
for d in a:
    b=d.split(':')
    c=len(b[0])
    if str(c) in list(b[1]):
        z.append(d[c-1])
    else:
        while c:
            c-=1
            if str(c) in list(b[1]):
                z.append(d[c-1])
                break
        if c==0:
            z.append('X')
for d in z:
    print(d,end='')