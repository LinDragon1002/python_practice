def total(a):
    a = [i for i in a.split(',')]
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