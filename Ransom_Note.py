a,b=map(str,input().split())
z=1
for i in range(len(a)):
    c=a.count(a[i])
    d=b.count(a[i])
    if c>d:
        z=0
        break
if z:
    print(True)
else:
    print(False)