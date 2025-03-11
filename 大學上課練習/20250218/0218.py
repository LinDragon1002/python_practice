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


def separate(a):
    if a[-1] == "C":
        a = a + "0"
    ans = [0,0,0]
    for i in range(len(a)):
        if a[i] == "#":
            ans[2] += 1
        if a[i] == "+":
            ans[1] += 1
        if a[i] == "C" and i != 0 and a[i] == a[i-1] or a[i] == "0":
            ans[0] += 1
    ans[1] = ans[1] // 2
    for i in ans:
        print(i)

a = input()
separate(a)

def total(a):
    temp = {"A":1,"J":11,"Q":12,"K":13}
    ans = 0
    for i in range(len(a)):
        if a[i] in temp:
            ans += temp[a[i]]
        else:
            ans += int(a[i])
    return ans
a = input()
print(total(a))
