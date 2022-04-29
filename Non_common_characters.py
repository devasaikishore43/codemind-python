n=input()
m=input()
n=n.lower()
m=m.lower()
c=0
for i in range(97,123):
    if chr(i) not in n and chr(i) in m:
        c+=1
    if chr(i) in n and chr(i) not in m:
        c+=1
print(c)