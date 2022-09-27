a,b,c=map(int,input().split())
l=list(map(int,input().split()))
l[:] = l[a-b:]+l[:a-b]
for i in range(c):
    print(l[int(input())])