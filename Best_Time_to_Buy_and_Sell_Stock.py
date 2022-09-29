a=int(input())
l=list(map(int,input().split()))
out = l[0]
large=0
for i in l[1:]:
    if large<(i-out):
        large = i - out
    out = min(out,i)
print(large)