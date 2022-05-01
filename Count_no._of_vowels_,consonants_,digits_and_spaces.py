n=input()
ws=n.count(' ')
n=n.replace(' ','')
v=['a','e','i','o','u']
vowel,conso,digit=0,0,0
for i in range(len(n)):
    if n[i] in v:
        vowel+=1
    elif n[i].isdigit():
        digit+=1
    else:
        conso+=1
print('Vowels:',vowel)
print('Consonants:',conso)
print('Digits:',digit)
print('White spaces:',ws)
        