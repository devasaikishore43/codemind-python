n=str(input())
x,y=0,0
for i in range(len(n)):
    if n[i]=='z':
        x+=1
    else:
        y+=1
if (2*x)==y:
    print('Yes')
else:
    print('No')