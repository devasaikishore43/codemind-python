m=input()
b=m.count('b')
a=m.count('a')
l=m.count('l')
o=m.count('o')
n=m.count('n')
s=b+a+l+o+n
count=0
for i in range(s//7):
    if b>=1 and a>=1 and l>=2 and o>=2 and n>=1:
        b-=1
        a-=1
        l-=2
        o-=2
        n-=1
        count+=1
print(count)