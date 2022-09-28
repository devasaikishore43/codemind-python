for _ in range(int(input())):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))
    c=False
    for i in range(a):
        for j in range(i+1,a):
            if sum(l[i:j+1])==b:
                print(i+1,j+1)
                c=True
                break
        if c:
            break
    else:
        print(-1)