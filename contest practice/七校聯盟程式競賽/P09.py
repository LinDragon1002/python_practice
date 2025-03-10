def counts():
    st = [i.strip() for i in input().split(",")]
    ans = [int(st[0],3), int(st[1],6)]
    total = ans[0] + ans[1]
    if total == 0:
        return 0
    base5 = ""
    while total > 0:
        base5 = str(total % 5) + base5
        total //= 5
    return base5
print(counts())