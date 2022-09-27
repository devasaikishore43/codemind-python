a=int(input())
l=list(map(int,input().split()))
mx=-1000
for i in range(a):
    for j in range(i,a):
        mx=max(sum(l[i:j+1]),mx)
print(mx)