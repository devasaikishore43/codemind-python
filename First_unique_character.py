n=input()
for d in list(n):
    a=list(n).count(d)
    if a==1:
        print(d)
        break
else:
    print('-1')