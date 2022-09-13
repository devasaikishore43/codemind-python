from collections import Counter
a=input()
d=Counter(a)
b=list(set(d.values()))
if len(b) == 1:
    print("-1")
else:
    b.sort()
    z=b[-2]
    for i,j in d.items():
        if j==z:
            print(i)
            break
    
    