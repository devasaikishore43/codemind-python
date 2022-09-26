a=int(input())
ind = list(map(int,input().split()))
b=int(input())
val= list(map(int,input().split()))
out=[]
for i,j in zip(ind,val):
    out.insert(j,i)
print(*out)