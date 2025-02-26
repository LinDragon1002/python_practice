def braves(a):
    a = sorted(a)
    temp = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E':0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T':0, 'U': 0, 'V':0, 'W':0, 'X': 0, 'Y': 0, 'Z': 0}
    ans = []
    for i in a:
        temp[i] += 1
    temp1 = 0
    for i in temp:
        if temp1 < 8 and temp[i] == 2:
            ans.append(i)
        elif temp1 >= 8 and temp[i] == 3:
            ans.append(i)
        temp1 += 1
    return ans


a = input()
print(braves(a))
