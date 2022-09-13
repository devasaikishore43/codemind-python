s1=input()
s2=input()
s=""
count1=[]
for i in range(len(s1)):
    if s1[i]!="#":
        s+=s1[i]
        count1+=[i]
        
sa=''
count=[]
for i in range(len(s2)):
    if s2[i]!="#":
        sa+=s2[i]
        count+=[i]
if sa==s:
    j=0
    bol = True
    for i in s:
        if i=="B":
            if count1[j] > count[j]:
                bol = False
                break
        else:
            if count1[j] < count[j]:
                bol = False
                break
        j+=1
    if bol:
        print("Yes")
    else:
        print("No")
else:
    print("No")