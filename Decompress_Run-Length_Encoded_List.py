a=int(input())
l=list(map(int,input().split()))
out=[]
for i in range(0,a,2):
    out+=([l[i+1]]*l[i]) 
print(*out)