for _ in range(int(input())):
    a = int(input())
    c = 1
    for i in range(2,a+1):
        if i&1:
            c = c&i
        else:
            c = c^i
    if a>=1:
        print(c)
    else:
        print(0)