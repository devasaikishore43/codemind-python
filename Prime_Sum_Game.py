def is_prime(a):
    b = int(a**0.5)+1
    for i in range(2,b):
        if a%i==0:
            return False
    return True
a,b,c,d = map(int,input().split())
z = False
for i in range(a,b+1):
    z = False
    for j in range(c,d+1):
        if is_prime(i+j) == True:
            z = True
            break
    if z==False:
        print("Takahashi")
        break
if z:
    print("Aoki")