def conbine():
    response1 = [i for i in input()]
    response2 = [i for i in input()]
    ans = ""
    for i in range(min(len(response1), len(response2))):
        ans += response1[i] + response2[i]
    for i in range(min(len(response1), len(response2)), max(len(response1), len(response2))):
        if len(response1) > len(response2):
            ans += response1[i]
        else:
            ans += response2[i]
    return ans
print(conbine())