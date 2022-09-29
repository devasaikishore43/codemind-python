for _ in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))
    left = 0
    right = sum(l)
    for i in range(a):
        right-=l[i]
        if left == right:
            print("YES")
            break
        left+=l[i]
    else:
        print("NO")