from itertools import permutations
a,b = map(int,input().split())
l = [i for i in range(1,a+1)]
z = list(permutations(l))
for i in z[b-1]:
    print(i,end="")