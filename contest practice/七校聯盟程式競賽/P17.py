for i in range(int(input())):
    temp = list(map(int,input().split()))
    if temp[1] % 2 != 0:
        temp1 = temp[1] ** 2
    else:
        temp1 = (temp[1]-1) ** 2 + 1
    if temp[0] % 2 == 0:
        temp2 = temp[0] ** 2
    else:
        temp2 = (temp[0]-1) ** 2 + 1
    if temp[0] == 1 and temp[1] == 1:
        print(1)
    elif temp[0] == 1:
        print(temp1)
    elif temp[1] == 1:
        print(temp2)
    else:
        if temp1 > temp2:
            if temp1 ** 0.5 == temp[1]:
                ans = temp1 - temp[0] + 1
            elif temp2 ** 0.5 == temp[0]:
                ans = temp1 + temp[0] - 1
            else:
                ans = temp1 + temp[0] - 1
        else:
            if temp2 ** 0.5 == temp[0]:
                ans = temp2 - temp[1] + 1
            elif temp1 ** 0.5 == temp[1]:
                ans = temp2 + temp[1] - 1
            else:
                ans = temp2 + temp[1] - 1
        print(ans)
