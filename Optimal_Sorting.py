for _ in range(int(input())):
    a=int(input())
    l = list(map(int,input().split()))
    s = sorted(l)
    count = 0
    b,c = -1,-1
    for i in range(a):
        if l[i]!=s[i]:
            b = i
            break
    for i in range(a-1,-1,-1):
        if l[i]!=s[i]:
            c = i
            break
    if c!=-1:
        print(max(l[b:c+1])-min(l[b:c+1])) 
    else:
        print(0)