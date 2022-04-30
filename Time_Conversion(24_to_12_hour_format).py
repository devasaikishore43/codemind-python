n=input()
n=n.split(':')
if 0<int(n[0])<12:
    print(n[0]+':'+n[1]+' AM')
elif int(n[0])==0:
    print('12'+':'+n[1]+' AM')
elif int(n[0])==12:
    print(n[0]+':'+n[1]+' PM')
else:
    a=str(int(n[0])-12)
    if len(a)==1:
        a='0'+a
    print(a+':'+n[1]+' PM')