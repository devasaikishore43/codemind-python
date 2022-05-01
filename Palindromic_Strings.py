n=int(input())
for i in range(n):
    a=input()
    b=input()
    c=str(a+b)
    d=str(b+a)
    if d==d[::-1] or c==c[::-1]:
        print('YES')
    else:
        print("NO")