a=input()
a=list(a)
l = "aeiouAEIOU"
s = ""
ind = []
for i in range(len(a)):
    if a[i] in l:
        s+=a[i]
        ind.append(i)
k = 0
for i in ind[::-1]:
    a[i] = s[k]
    k+=1
print("".join(a))