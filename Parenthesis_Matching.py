a = input()
lis = []
opn,close="{([","})]"
for i in range(len(a)):
    if a[i] in opn:
        lis.append(a[i])
    else:
        if len(lis):
            if a[i]==")" and lis[-1]=="(":
                lis.pop()
            elif a[i]=="}" and lis[-1]=="{":
                lis.pop()
            elif a[i]=="]" and lis[-1]=="[":
                lis.pop()
            else:
                print(i+1)
                break
        else:
            print(i+1)
            break
else:
    if len(lis):print(len(a)+1)
    else: print(0)
        