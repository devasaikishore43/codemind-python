n=input()
c=0
for i in range(len(n)):
    if n[i].isdigit():
        c+=1
if c:
    print('Contains '+str(c)+' digit')
else:
    print("Doesn't contain digit")