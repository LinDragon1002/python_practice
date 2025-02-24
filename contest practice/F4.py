def guess(a,b):
    ans = 0
    ans1 = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            ans += 1
        else:
            for j in range(len(a)):
                if a[i] == b[j]:
                    ans1 += 1
                    break

    return str(ans)+"A"+str(ans1)+"B"

a = input()
b = input()
print(guess(a,b))