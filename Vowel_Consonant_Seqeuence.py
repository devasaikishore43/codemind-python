a = input()
vol = "aeiou"
out="O"
for i in a:
    if i in vol and out[-1]!="V":
        out+="V"
    else:
        if out[-1]!="C":
            out+="C"
print(out[1:])