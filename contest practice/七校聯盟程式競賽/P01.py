def most():
    response = input()
    ans = {}
    for i in response:
        if i not in ans:
            ans[i] = 1
        else:
            ans[i] += 1
    ans = sorted(ans.items(), key=lambda x: x[1], reverse=True)
    return ans[0][0]

print(most())