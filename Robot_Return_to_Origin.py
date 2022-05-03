n=input()
a,b=0,0
for i in range(len(n)):
    if n[i]=='L':
        b+=1
    if n[i]=='R':
        b-=1
    if n[i]=='U':
        a+=1
    if n[i]=='D':
        a-=1
if a==0 and b==0:
    print(True)
else:
    print(False)

    