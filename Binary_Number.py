a = int(input())
for i in range(2**a):
    b = bin(i)[2:]
    if len(b)!=a:
        b = '0'*(a-len(b)) +b
    print(b)
        