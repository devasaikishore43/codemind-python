b = int(input())
l = list(map(int,input().split()))
a = l[-1]
for i in l[::-1]:
    if i > a:
        print(2)
        break
else:
    if len(set(l))==1:
        print(0)
    else:
        print(1)