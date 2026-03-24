strs = ["c","c"]
if not strs:
    print("")
for i in range(len(strs[0])):
    char = strs[0][i]
    if len(char) == 0:
        print("")
        break
    for j in strs[1:]:
        if i >= len(j) or j[i] != char:
            print(str54.s[0][:i])
print(strs[0])

# 另解
'''for j in range(len(strs[0])):
            char = strs[0][j]
            for i in range(1, len(strs)):
                if  (len(strs[i]) == j) or (strs[i][j] != char):
                    return strs[0][:j]
'''
    