a=int(input())
nums=list(map(int,input().split()))
answer=[[]]
b = sum(nums)//2
c = False
for n in nums:
    answer+=[i+[n] for i in answer]
for i in answer:
    if sum(i)==b:
        c = True
        break
if c:
    print("YES")
else:
    print("NO")