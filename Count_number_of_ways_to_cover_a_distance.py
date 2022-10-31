def last(dist):
    if dist < 0:
        return 0
    if dist == 0:
        return 1
    return (last(dist-1) +
            last(dist-2) +
            last(dist-3))
a=int(input())
print(last(a))