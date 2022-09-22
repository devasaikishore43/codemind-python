a= int(input())
l = list(map(int,input().split()))
b = 0
for i in l:
    if i&1:
        b+=1
if b&1==0:
    print(1)
else:
    print(0)