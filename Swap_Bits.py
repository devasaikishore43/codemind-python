a,b,c,d=map(int,input().split())
e = bin(a)[2:][::-1]
if len(e)< c+d:
    e+="0"*((c+d)-len(e))
z= e[:b]+e[c:c+d]+e[b+d:c]+e[b:b+d]+e[c+d:]
num = 0
for i in range(len(z)):
    if z[i]=="1":
        num+=(2**i)
print(num)