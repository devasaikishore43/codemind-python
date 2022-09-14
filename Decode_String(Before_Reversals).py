for _ in range(int(input())):
    a,b=map(int,input().split())
    l=input()
    l=list(l)
    for i in range(b,0,-1):
        l[:] = l[:i][::-1]+l[i:]
    print("".join(l))
        
        