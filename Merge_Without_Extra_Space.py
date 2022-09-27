for _ in range(int(input())):
    a,b=map(int,input().split())
    l=list(map(int,input().split()))+list(map(int,input().split()))
    l.sort()
    print(*l)