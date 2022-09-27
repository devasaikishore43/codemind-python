for _ in range(int(input())):
    a=int(input())
    l=list(map(int,input().split()))
    if a==1:
        print(a)
    else:
        count = 1
        mn=l[0]
        for i in l[1:]:
            if mn<i:
                continue
            else:
                count+=1
                mn=i
        print(count)