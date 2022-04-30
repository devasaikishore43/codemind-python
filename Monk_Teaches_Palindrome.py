n=int(input())
for i in range(n):
    a=input()
    if a==a[::-1]:
        if len(a)%2:
            print('YES ODD')
        else:
            print('YES EVEN')
    else:
        print('NO')