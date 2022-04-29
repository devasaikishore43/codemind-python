n=input()
n=n.split(' ')
minsum=0
maxsum=0
for i in range(len(n)):
    z=[]
    a=list(str(n[i]))
    for d in a:
        z.append(ord(d))
    minsum+=min(z)
    maxsum+=max(z)
print(abs(maxsum-minsum))