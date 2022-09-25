l=[]
for _ in range(int(input())):
    a=input()
    loc = ''
    c = True
    for i in range(len(a)):
        if a[i]=="+":
            c=False
        if a[i]=="@":
            loc+=a[i:]
            break
        if c and a[i]!=".":
            loc+=a[i]
    if loc not in l:
        l.append(loc)
print(len(l))