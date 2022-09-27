for _ in range(int(input())):
    s = input()
    s=sorted(s)
    for i in range(len(s)-1):
        if int(s[i+1])-int(s[i])!=1:
            print("NO")
            break
    else:
        print("YES")