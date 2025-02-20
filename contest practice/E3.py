def score(a,b):
    ans = 0
    for i in range(20):
        if a[i] == "E" and b[i] in "AB":
            ans += 5
        elif a[i] == "F" and b[i] in "CD":
            ans += 5
        elif a[i] == b[i]:
            ans += 5
    return ans


a = input()
b = input()
print(score(a.upper(),b.upper()))