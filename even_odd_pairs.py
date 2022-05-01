n=int(input())
l=list(map(int,input().split()))
od,ev=[],[]
z=[]
for i in range(n):
    if l[i]%2:
        od.append(l[i])
    else:
        ev.append(l[i])
for i in range(min(len(od),len(ev))):
    z.append(ev[i])
    z.append(od[i])
if len(ev)<len(od):
    for i in range(len(ev),len(od)):
        z.append(od[i])
elif len(ev)>len(od):
    for i in range(len(od),len(ev)):
        z.append(ev[i])
if len(z)%2:
    z.append(0)
print(*z)