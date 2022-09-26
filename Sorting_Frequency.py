from collections import Counter
a=int(input())
l=list(map(int,input().split()))
b=Counter(l)
so = sorted(b.items(), key = lambda x : (-x[1], x[0]))
for i,j in so:
    print(i,end=" ")