for _ in range(int(input())):
    a=input()
    s=""
    for i in a:
        if i=="A" or i=="a":
            s+="1010"
        elif i=="B" or i=="b":
            s+="1011"
        elif i=="C" or i=="c":
            s+="1100"
        elif i=="D" or i=="d":
            s+="1101"
        elif i=="E" or i=="e":
            s+="1110"
        elif i=="F" or i=="f":
            s+="1111"
        elif i=="1":
            s+="0001"
        elif i=="2":
            s+="0010"
        elif i=="3":
            s+="0011"
        elif i=="4":
            s+="0100"
        elif i=="5":
            s+="0101"
        elif i=="6":
            s+="0110"
        elif i=="7":
            s+="0111"
        elif i=="8":
            s+="1000"
        elif i=="9":
            s+="1001"
        elif i=="0":
            s+="0"
    print(s)