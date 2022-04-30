n=int(input())
for i in range(n):
    a=str(input())
    c=0
    for i in range(len(a)):
        if a[i].isdigit():
            c+=1
    if c==len(a):
        print(True)
    else:
        print(False)