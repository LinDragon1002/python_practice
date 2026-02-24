pattern = "abba"
s = "dog cat cat dog"

s = s.split(" ")
ans = dict()
if len(set(pattern)) != len(set(s)) or len(pattern) != len(s):
    print(False)
else:
    for i in range(len(pattern)):
        if pattern[i] not in ans:
            ans[pattern[i]] = s[i]
        else:
            if ans[pattern[i]] == s[i]:
                continue
            else:
                print(False)
                break
    else:
        print(True)