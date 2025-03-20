from typing import Counter

temp1 = []
temp2 = []
s = Counter(input())
for i in s:
    if s[i] % 2 == 0:
        temp1.append(s[i])
    else:
        temp2.append(s[i])

print(max(temp2)-min(temp1))