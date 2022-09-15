for _ in range(int(input())):
    a=input()
    a=a[::-1]
    s=""
    for i in range(0,len(a),3):
        k=0
        c=0
        for j in a[i:i+3]:
            if j=="1":
                c+=(2**k)
            k+=1
        s = str(c)+s
    print(s)