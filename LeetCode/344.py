s = ["h","e","l","l","o"]
# ans = s.copy()
# count = 0
# for i in range(len(ans)-1,-1,-1):
#     s[count] = ans[i]  
#     count += 1
# print(s)


size = len(s)
for i in range(size // 2):
    s[i], s[size - 1 - i] = s[size - 1 - i], s[i]