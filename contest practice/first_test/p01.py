def counts():
    st = [i for i in input()]
    temp = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E':0, 'F': 0, 'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T':0, 'U': 0, 'V':0, 'W':0, 'X': 0, 'Y': 0, 'Z': 0}
    ans = []
    for i in range(len(st)):
        temp[st[i]] += 1
    number=0
    for i in temp:
        if number < 8 and 0 < 2-temp[i] < 2:
            ans.append(i)
        elif number >= 8 and 0 < 3-temp[i] < 2:
            ans.append(i)
        number += 1
    ans = sorted(ans)
    if len(ans) > 0:
        return "".join(ans)
    return "*"
print(counts())