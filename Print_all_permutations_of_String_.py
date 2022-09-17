from itertools import permutations 
s=input()
a=list(permutations(list(s)))
for i in a:
    print("".join(i))