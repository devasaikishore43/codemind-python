a=int(input())
l=list(map(int,input().split()))
l.sort()
if 1 not in l:
    print(1)
else:
    b=l.index(1)
    for i in range(b,(a-b+1)):
        if l[i]!=i:
            print(i)
            break
    else:
        print(i+1)