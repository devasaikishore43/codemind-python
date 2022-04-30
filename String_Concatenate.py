n=input()
m=input()
a=n+m
for i in range(65,123):
    for j in range(len(a)):
        if chr(i)==a[j]:
            print(a[j],end='')