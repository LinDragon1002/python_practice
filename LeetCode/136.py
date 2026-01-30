nums = [2,2,1]
from typing import Counter
ans = sorted(Counter(nums).items(), key=lambda x:x[-1])
print(ans[0][0])