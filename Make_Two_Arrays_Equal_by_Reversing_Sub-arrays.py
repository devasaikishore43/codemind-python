a=int(input())
a1=list(map(int,input().split()))
b=int(input())
b1=list(map(int,input().split()))
if sorted(a1)==sorted(b1):
    print(True)
else:
    print(False)