for _ in range(int(input())):
    s=input()
    opn = "({["
    lis = []
    ans = False
    for i in s:
        if i in opn:lis.append(i)
        elif len(lis): 
            if i==")" and lis[-1]=="(":
                lis.pop(-1)
            elif i=="}" and lis[-1]=="{":
                lis.pop(-1)
            elif i=="]" and lis[-1]=="[":lis.pop(-1)
            else:
                ans = True
                break
        else:
            ans = True
            break
    if ans or len(lis):print(False)
    else:
        print(True)
        