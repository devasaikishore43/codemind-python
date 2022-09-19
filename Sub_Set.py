a = int(input())
nums=list(map(int,input().split()))
answer=[[]]
for n in nums:
    answer+=[i+[n] for i in answer]
for i in answer:
    print(*i)