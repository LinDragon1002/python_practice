st = int(input())
ans = "1"
num = 1
if str(st) != "1":
    for i in range(20):
        temp = ""
        for j in range(len(ans)-1):
            if ans[j] != ans[j+1]:
                temp += ans[j] + ","
            elif ans[j] == ans[j+1]:
                temp += ans[j]
        temp += ans[-1]
        temp = temp.split(",")
        ans = ""
        for j in range(len(temp)):
            ans += str(len(temp[j])) + temp[j][0]
        num += 1

        if int(ans) == st:
            print(num)
            break
    else:
        print(0)
else:
    print(num)