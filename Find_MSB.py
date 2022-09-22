for i in range(int(input())):
    a = int(input())
    for i in range(1,31):
        if a<(2**i):
            print(2**(i-1))
            break
        if a==(2**i):
            print(a)
            break