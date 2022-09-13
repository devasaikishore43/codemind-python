a=input()
count=1
maxi = 0
for i in range(len(a)-1):
    if a[i] == a[i+1]:
        count+=1
    else:
        maxi = max(maxi,count)
        count=1
maxi = max(maxi,count)
print(maxi)
        
        
    