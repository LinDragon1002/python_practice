def evaluation(a):
    ans = 0
    temp = [i for i in a.split(',')]
    for i in temp:
        if int(i) >= 60:
            ans += 1
    if ans >= 5:
        return "過關"
    else:
        return "卡關"

a = input()
print(evaluation(a))