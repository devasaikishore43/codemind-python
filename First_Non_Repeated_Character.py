n=int(input())
for i in range(n):
    a=int(input())
    b=input()
    for j in range(a):
        c=b.count(b[j])
        if c==1:
            print(b[j])
            break
    else:
        print('-1')