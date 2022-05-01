n=input()
z=str()
for i in range(len(n)):
    if int(n[i])%2:
        z=z+str(int(n[i])**2)
print(z)