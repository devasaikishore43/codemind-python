for _ in range(int(input())):
    a=input()
    b=input()
    c=(ord(b[0])-ord(a[0]))
    t = True
    for i,j in zip(b,a):
        d = (ord(i)-ord(j))
        if c < d or d<0:
            t = False
            break
    if t:
        print("YES")
    else:
        print("NO")
        