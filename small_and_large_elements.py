n=input()
n=n.split(' ')
z=[]
a=list(n[0])
b=list(n[-1])
c=[]
for d in a:
    c.append(ord(d))
print(chr(min(c)),end=' ')
c=[]
for d in b:
    c.append(ord(d))
print(chr(max(c)))   