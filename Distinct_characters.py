n=input()
for i in range(97,123):
    a=list(n).count(chr(i))
    if a>=1:
        print(chr(i),end='')
