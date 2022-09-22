a,b = map(int,input().split())
for i in range(1,31):
    c = 2**i
    if a<=c-1 and c<=b:
        print(0)
        break
    elif c>a and c>=b:
        print(2**(i-1))
        break