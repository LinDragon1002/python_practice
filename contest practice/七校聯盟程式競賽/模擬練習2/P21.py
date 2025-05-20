st= input()
cnt = 0
deeps = []
deeps_types = []
for i in range(len(st)):
    if st[i] == "{":
        cnt += 1
        deeps.append(cnt)
        deeps_types.append("{")
    elif st[i] == "[":
        cnt += 1
        deeps.append(cnt)
        deeps_types.append("[")
    elif st[i] == "(":
        cnt += 1
        deeps.append(cnt)
        deeps_types.append("(")
    elif st[i] == "}":
        cnt -= 1
        deeps.append(cnt)
        if cnt != -1 and deeps_types[-1] == "{":
            deeps_types.pop()
        else:
            cnt = -1
            break
    elif st[i] == "]":
        cnt -= 1
        deeps.append(cnt)
        if cnt != -1 and deeps_types[-1] == "[":
            deeps_types.pop()
        else:
            cnt = -1
            break
    elif st[i] == ")":
        cnt -= 1
        deeps.append(cnt)
        if cnt != -1 and deeps_types[-1] == "(":
            deeps_types.pop()
        else:
            cnt = -1
            break
if cnt == 0:
    print(max(deeps))
else:
    print(-1)