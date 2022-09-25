a=input()
od,ev="",''
o,e,c=0,0,0
for i in a:
    if i.isdigit():
        if int(i)&1:
            od+=i
            o+=1
        else:
            ev+=i
            e+=1
    elif i.isalpha():
        continue
    else:
        c+=1
if c&1:
    l,m=0,0
    while o or e:
        if o:
            print(od[l],end="")
            l+=1
            o-=1
        if e:
            print(ev[m],end="")
            m+=1
            e-=1
else:
    l,m=0,0
    while o or e:
        if e:
            print(ev[m],end="")
            m+=1
            e-=1
        if o:
            print(od[l],end="")
            l+=1
            o-=1