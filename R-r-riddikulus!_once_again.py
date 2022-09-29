a,b=map(int,input().split())
l = list(map(int,input().split()))
c = l[b:]+l[:b]
print(*c)