n=input()
n=n.replace(' ','')
n=list(str(n))
z=[]
for d in n:
    z.append(ord(d))
print(chr(min(z)),z.count(min(z)),end=' ')
print(chr(max(z)),z.count(max(z)),end=' ')    