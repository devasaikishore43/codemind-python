a = int(input())
i=0
k = 0
while a:
    if a&1==0:
        k+=(2**i)
    i+=1
    a = a>>1
print(k)