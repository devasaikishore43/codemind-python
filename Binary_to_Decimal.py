for _ in range(int(input())):
    a=input()
    count = 0
    i=0
    for j in a[::-1]:
        if j=="1":
            count+=(2**i)
        i+=1
    print(count)