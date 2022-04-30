n=int(input())
for i in range(n):
    a=input()
    c=0
    for i in range(len(a)):
        if a[i].isdigit():
            c+=1
    if c:
        print('Yes')
    else:
        print("No")