n=input()
n=n.lower()
z=['a','e','i','o','u']
con=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
c=0
for i in range(len(n)//2):
    if n[i] in z and n[len(n)-(i+1)] in con:
        c+=1
    if n[i] in con and n[len(n)-(i+1)] in z:
        c+=1
print(c)