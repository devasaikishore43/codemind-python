a = int(input())
l = list(map(int,input().split()))
b = 0
for i in l:
    b = b^i
print(b)