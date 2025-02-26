def repeat():
    response = [i for i in input()]
    ans = []
    for i in range(len(response)):
        if i == 0:
            ans.append(response[i])
            ans.append(1)
        if i < len(response)-1:
            if response[i] == response[i+1]:
                if response[i] not in ans:
                    ans.append(response[i])
                    ans.append(1)
                else:
                    ans[ans.index(response[i])+1] += 1
            else:
                ans.append(response[i+1])
                ans.append(1)
    return "".join(map(str,ans))
print(repeat())

def repeatchatgpt():
    response = input()
    if not response:  # 若輸入為空字串，直接回傳空結果
        return ""

    ans = []
    prev_char = response[0]  # 記錄當前處理的字元
    count = 1  # 記錄該字元的出現次數

    for i in range(1, len(response)):
        if response[i] == prev_char:  # 如果當前字元與前一個相同，累加計數
            count += 1
        else:
            ans.append(prev_char)  # 將前一個字元和次數加入結果
            ans.append(str(count))
            prev_char = response[i]  # 更新 `prev_char` 為新字元
            count = 1  # 重置計數

    # 處理最後一個字元
    ans.append(prev_char)
    ans.append(str(count))

    return "".join(ans)

print(repeatchatgpt())