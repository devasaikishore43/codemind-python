l=int(input())
r=int(input())
lis = [i for i in range(l,r+1)]
count=0
for i in range(r-l+1):
    for j in range(i,r-l+1):
        if sum(lis[i:j+1])&1:
            count+=1
print(count)