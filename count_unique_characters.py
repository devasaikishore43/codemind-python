n=input()
c=0
for i in range(97,123):
    a=list(n).count(chr(i))
    if a==1:
        c+=1
print(c)
