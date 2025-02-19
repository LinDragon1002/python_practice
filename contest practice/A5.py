def check(a):
    temp = {}
    for i in range(len(a)):
        if a[i] not in temp:
            temp[a[i]] = 1
        else:
            temp[a[i]] += 1
    for i in range(len(temp)):
        ans = max(temp.values())
    if ans == 4:
        return "A"
    elif ans == 3:
        return "B"
    elif ans == 2:
        return "C"
    else:
        return "D"

a = input()
print(check(a))
