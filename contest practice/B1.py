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