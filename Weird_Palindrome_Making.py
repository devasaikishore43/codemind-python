for _ in range(int(input())):
    number=int(input())
    arr=list(map(int,input().split()))
    odd=0
    total=0
    for num in arr:
        if num&1:
            odd+=1
        total+=num
    
    if total%2==0:
        print(odd//2)
    else:
        print((odd-1)//2)