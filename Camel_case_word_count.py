n=input()
c=0
if n[0].islower():
    c+=1
for i in range(len(n)):
    if n[i].isupper():
        c+=1
print(c)