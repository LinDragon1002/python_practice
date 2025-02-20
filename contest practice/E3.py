def score(a,b):
    ans = 0
    for i in range(max(len(a),len(b))):
        if i >= 20:
            ans -= 5*(i-19)
            break
        if a[i] == "E":
            if b[i] in "AB":
                ans += 5
        elif a[i] == "F":
            if b[i] in "CD":
                ans += 5
        elif a[i] == b[i]:
            ans += 5
    return ans


a = input()
b = input()
print(score(a.upper(),b.upper()))