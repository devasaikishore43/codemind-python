s=input()
z=''
for d in s:
    if 96< ord(d) < 123:
        z+=d
z=z[::-1]
j=0
s=list(s)
for i in range(len(s)):
    if 96 < ord(s[i]) < 123:
        s[i] = z[j]
        j+=1
print(''.join(s))
    
        