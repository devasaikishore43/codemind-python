def gcd(a,b):
    while b:
        if a>b:
            a,b=b,a
        b=b%a
    return a
b = int(input())
a=list(map(int,input().split()))
lcm = a[0]
for i in range(1,len(a)):
    lcm = (lcm*a[i])//(gcd(lcm, a[i]))
print(lcm)