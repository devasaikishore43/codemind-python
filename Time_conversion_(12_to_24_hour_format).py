n=input()
a=n.split(' ')
k=a[0].split(':')
if a[-1]=='AM' and int(k[0])!=12:
    print(k[0]+':'+k[1])
elif int(k[0])==12 and a[-1]=='AM':
    print('00:'+k[1])
elif int(k[0])==12 and a[-1]=='PM':
    print('12:'+k[1])
else:
    b=str(12+int(k[0]))
    print(b+':'+k[1])
