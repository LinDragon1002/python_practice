def robotwalk():
    st = [i for i in input()]
    ans = [0,0]
    for i in st:
        if i == "U":
            ans[1] += 1
        elif i == "D":
            ans[1] -= 1
        elif i == "L":
            ans[0] -= 1
        elif i == "R":
            ans[0] += 1
    if ans[0] == ans[1] and ans[0] == 0:
        return True
    return False
print(robotwalk())