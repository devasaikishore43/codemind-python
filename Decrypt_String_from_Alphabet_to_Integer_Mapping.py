n=input()
i=0
while i<len(n)-2:
    if n[i+2]=='#':
        a=int(n[i]+n[i+1])
        print(chr(a+96),end='')
        i+=3
    else:
        print(chr(int(n[i])+96),end='')
        i+=1
if n[-1] !='#':
    for i in range(len(n)-2,len(n)):
        print(chr(int(n[i])+96),end='')