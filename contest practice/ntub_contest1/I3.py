def chess():
    response = input().replace("X","1").replace("O", "0")
    ans = [[0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            ans[i][j] = int(response[i*3+j])
    temp = [0] * 3
    for i in range(3):
        temp.append(sum(ans[i]))
        for j in range(3):
            temp[i] += ans[j][i]
    # temp[6] = ans[0][0] + ans[1][1] + ans[2][2]
    # temp[7] = ans[0][2] + ans[1][1] + ans[2][0]
    temp.append(sum(ans[i][i] for i in range(3)))
    temp.append(sum(ans[i][2 - i] for i in range(3)))
    correct = [temp.count(0), temp.count(3)]
    '''
    if correct[0] > correct[1]:
        return "O"
    elif correct[0] < correct[1]:
        return "X"
    else:
        return "平手"
    '''
    return "O" if correct[0] > correct[1] else "X" if correct[0] < correct[1] else "平手"

print(chess())