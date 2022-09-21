for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    count = 0
    if b%c==0 or c%b==0:
        count = max(b//c,c//b)-1
    else:
        for i in range(1,a+1):
            if i%c==0 and i%b==0:
                continue
            elif i%c==0 or i%b==0:
                count+=1
            if count==d:
                break
    if count>=d and a>1:
        print("Win")
    else:
        print("Lose")