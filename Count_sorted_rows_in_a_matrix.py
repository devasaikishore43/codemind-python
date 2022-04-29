a,b=map(int,input().split())
count=0
for i in range(a):
    l=list(map(int,input().split()))
    c=0
    if l[1]-l[0]>0:
        for i in range(b-1):
            if l[i]-l[i+1]<0:
                c+=1
            if c==b-1:
                count+=1
    else:
        for i in range(b-1):
            if l[i]-l[i+1]>0:
                c+=1
            if c==b-1:
                count+=1
print(count)