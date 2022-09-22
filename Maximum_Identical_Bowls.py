a = int(input())
l = list(map(int,input().split()))
b = sum(l)
while a:
    if b%a==0:
        print(a)
        break
    a-=1