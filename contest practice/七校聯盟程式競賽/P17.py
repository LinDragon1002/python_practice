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
    if temp1 > temp2:
        ans = temp1 - temp[0] + 1
        print(ans)
    elif temp1 < temp2:
        ans = temp2 - temp[1] + 1
        print(ans)
