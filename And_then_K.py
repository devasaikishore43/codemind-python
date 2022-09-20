for _ in range(int(input())):
    a = int(input())
    for i in range(30):
        if a < 2**(i+1):
            print((2**i)-1)
            break