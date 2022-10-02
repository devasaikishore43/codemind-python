def diStringMatch(s):
    ans=[]
    mn,mx=0,len(s)
    for i in s:
        if i=="I":
            ans.append(mn)
            mn+=1
        else:
            ans.append(mx)
            mx-=1
    ans.append(mn)
    return ans
a=input()
print(*diStringMatch(a))