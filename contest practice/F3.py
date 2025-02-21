def maxchar(a):
    temp = [i for i in a]
    ans = {}
    for i in range(len(a)):
        if temp[i] not in ans:
            ans[temp[i]] = 1
        else:
            ans[temp[i]] += 1
    ans = sorted(ans.items(),key= lambda i:i[1], reverse=True)

    if len(ans) == 1 or ans[0][1] > ans[1][1]:
        return ans[0][0]
    return "多"
    '''
    if len(list(dict.values(ans))) == 1:
        return list(dict.keys(ans))[0]
    elif list(dict.values(ans))[0] == list(dict.values(ans))[1]:
        return "多"
    else:
        return list(dict.keys(ans))[0]
    '''


a = input()
print(maxchar(a))