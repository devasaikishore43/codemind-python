from collections import Counter
a = input()
b = Counter(a)
c = list(b.values())
d = list(set(c))
e = len(c)
if len(d)==1:
    print("Valid String")
elif len(d)==2:
    if c.count(d[0])==1 or c.count(d[1])==1 :
        print("Valid String")
    else:
        print("Not Valid")
else:
    print("Not Valid")