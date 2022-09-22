def dec_to_base(num,base):
    base_num = ""
    while num>0:
        dig = int(num%base)
        if dig<10:
            base_num += str(dig)
        else:
            base_num += chr(ord('A')+dig-10) 
        num //= base
    base_num = base_num[::-1]
    return base_num
a=int(input())
b=int(input())
z = dec_to_base(a,b)
maxi = 0
c = 0
for i in range(len(z)):
    if z[i]=='0':
        c+=1
    else:
        maxi=max(c,maxi)
        c=0
maxi=max(c,maxi)
if maxi:
    print(maxi)
else:
    print(-1)
    