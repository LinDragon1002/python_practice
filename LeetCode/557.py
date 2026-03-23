s = "Let's take LeetCode contest"
s = s.split(' ')
ans = ""
for i in range(len(s)):
    ans += s[i][::-1]
    if i != len(s)-1:
        ans += " "
print(ans)