def allword():
    st = [i for i in input()]
    temp = [0] * 26
    ans = "abcdefghijklmonpqrstuvwxyz"
    if len(st) < len(ans):
        return False
    else:
        for i in range(len(st)):
            for j in range(len(ans)):
                if st[i] == ans[j]:
                    temp[j] += 1
                    break
        if 0 not in temp:
            return True
        return False
print(allword())