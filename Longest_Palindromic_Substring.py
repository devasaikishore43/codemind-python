a = input()
a=a.lower()
count=0
strng = a[0]
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if (a[i:j+1]) == (a[i:j+1])[::-1]:
            if (j-i) > count :
                count=j-i
                strng = a[i:j+1]
print(strng)