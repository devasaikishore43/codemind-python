n=input()
n=n.lower()
n=n.split(' ')
c=[]
for i in range(97,123):
    c=0
    for d in n:
        if chr(i) in d:
            c+=1
    if c==len(n):
        print(chr(i))
        break
else:
    print('-1')