n=input()
n=n.split(':')
k=abs((30*int(n[0]))-(11*(int(n[1])/2)))
if k<=180:
    print(k)
else:
    a=k-180
    k=180-a
    print(k)