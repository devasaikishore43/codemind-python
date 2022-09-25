a=int(input())
l=[]
m=[]
for i in range(a):
    l.append(int(input()))
for i in range(a):
    m.append(int(input()))
for i in l:
    for j in range(len(m)):
        if i<=m[j]:
            a-=1
            m.pop(j)
            break
print(a)