a=int(input())
start=list(map(int,input().split()))
b=int(input())
end=list(map(int,input().split()))
k = int(input())
count=0
for i,j in zip(start,end):
    if i-1 < k < j+1:
        count+=1
print(count)