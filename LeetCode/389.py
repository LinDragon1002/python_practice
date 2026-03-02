s = "a"
t = "aa"

for i in set(t):
    if t.count(i) > s.count(i):
        print(i)
        break
else:
    print()

from typing import Counter

count_s = Counter(s)
count_t = Counter(t)

for char in count_t:
    if count_t[char] != count_s[char]:
        # return char
        print()