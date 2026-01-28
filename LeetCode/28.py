haystack = "leetcode"
needle = "leeto"
for i in range(len(haystack)):
    if needle == haystack[i:i+len(needle)]:
        print(i)
        break
else:
    print(-1)