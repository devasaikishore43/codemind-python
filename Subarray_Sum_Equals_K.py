a,b=map(int,input().split())
l=list(map(int,input().split()))
count=0
for i in range(a):
    for j in range(i,a):
        if sum(l[i:j+1])==b:
            count+=1
print(count)