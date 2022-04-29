n=input()
n=n.split(' ')
for d in n:
    z=[]
    a=list(d)
    for d in a:
        z.append(ord(d))
    print(abs(max(z)-min(z)),end=' ')
    