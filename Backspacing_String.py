s=input()
t=input()
s1,s2="",""
c = 0
for i in s[::-1]:
    if i=="#":
        c+=1
        continue
    elif c>0:
        c-=1
        continue
    else:
        s1+=i
c=0
for i in t[::-1]:
    if i=="#":
        c+=1
        continue
    elif c>0:
        c-=1
        continue
    else:
        s2+=i
if s1==s2:
    print(True)
else:
    print(False)

        