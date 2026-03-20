s = "AA"

from typing import Counter
import re
temp = Counter(s)

if temp['A'] < 2:
    if re.findall(r'(L{3})',s):
        print(False)
    else:
        print(True)
else:
    print(False)

# return s.count('A')<2 and s.count('LLL') == 0