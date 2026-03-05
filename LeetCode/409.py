s = "aabccvvvvvddd"

from typing import Counter
temp = sorted(Counter(s).values(),reverse=True)
ans = 0
num = 0
for i in temp:
    if i % 2 == 0:
        ans += i
    else:
        ans += i - 1
        num = max(i,num)
if num > 0:
    print(ans+1)
else:
    print(ans)
