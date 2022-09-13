a=input()
b=int(input())
if len(a)>=b:
    print(a[:b].count("a"))
else:
    c = a.count("a")
    c = c * (b // len(a))
    b = b % len(a)
    c+= a[:b].count("a")
    print(c)