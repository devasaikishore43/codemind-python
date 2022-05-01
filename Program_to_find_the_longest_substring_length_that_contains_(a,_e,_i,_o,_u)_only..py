n=input()
c,r=0,0
z=['a','e','i','o','u']
for i in range(len(n)):
    if n[i] in z:
        c+=1
    else:
        r=max(c,r)
        c=0
print(max(r,c))