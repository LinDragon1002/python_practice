def counts():
    ar = [int(i) for i in input().split()]
    temp = {}
    for i in range(len(ar)):
        if ar[i] not in temp:
            temp[ar[i]] = 1
        else:
            temp[ar[i]] += 1
    for i in temp:
        if temp[i] == len(ar) // 2:
            return i
print(counts())