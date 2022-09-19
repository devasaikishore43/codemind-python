from collections import Counter
a,b=map(int,input().split())
al = list(map(int,input().split()))
bl = list(map(int,input().split()))
ca = Counter(al)
cb = Counter(bl)
c = True
for i in cb.keys():
    if i not in ca:
        c = False
        break
    if cb[i]>ca[i]:
        c = False
        break
if c:
    print("Yes")
else:
    print("No")