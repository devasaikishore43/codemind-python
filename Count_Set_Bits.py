for i in range(int(input())):
    a = int(input())
    count = 0
    while a:
        if a&1:
            count+=1
        a=a>>1
    print(count)