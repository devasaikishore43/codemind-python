a=int(input())
l=list(map(int,input().split()))
l.sort(reverse=True)
b,c=0,0
for i in l:
    if c<b:
        c+=i
    else:
        b+=i
if c==b:
    print("YES")
else:
    print("NO")