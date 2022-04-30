n=input()
s=0
for i in range(len(n)):
    if n[i].isdigit():
        s+=int(n[i])
print(s)