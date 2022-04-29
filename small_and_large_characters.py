n=input()
n=n.split(' ')
for d in n:
    z=[]
    a=list(str(d))
    for d in a:
        z.append(ord(d))
    print(chr(min(z)),chr(max(z)),end=' ')