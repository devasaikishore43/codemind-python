for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    sum1 = (a*c)
    if b<a:
        a-=b
        for i in range(a,0,-b):
            sum1+=(i*d)
    print(sum1)