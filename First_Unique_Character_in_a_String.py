n=input()
for i in range(len(n)):
    a=n.count(n[i])
    if a==1:
        print(i)
        break
else:
    print('-1')