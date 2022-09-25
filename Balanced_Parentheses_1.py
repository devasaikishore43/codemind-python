a=input()
b,c,d=0,0,0
for i in a:
    if i=="(":
        b+=1
    elif i==")":
        b-=1
    elif i=="{":
        c+=1
    elif i=="}":
        c-=1
    elif i=="[":
        d+=1
    else:
        d-=1
if b or c or d:
    print(False)
else:
    print(True)