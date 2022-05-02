n=int(input())
l=list(map(int,input().split()))
m=[]
for d in l:
    if d in m:
        continue
    else:
        m.append(d)
print(*m)