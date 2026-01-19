from typing import Counter
nums = list(map(int,input().split(",")))
temp = sorted(Counter(nums).items(), key=lambda x:x[-1],reverse=True)
print(temp[0][0])