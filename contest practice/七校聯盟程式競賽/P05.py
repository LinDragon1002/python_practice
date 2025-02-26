def password():
    response =  [i for i in input()]
    ans = [0] * 3
    for i in range(len(response)):
        if response[i].isdigit():
            ans[0] += 1
        elif response[i].islower():
            ans[1] += 1
            if ans[2] > 0:
                return 0
        elif response[i].isupper():
            ans[2] += 1
    if ans.count(0) == 0:
        return 1
    return 0
print(password())