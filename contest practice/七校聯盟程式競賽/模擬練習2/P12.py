nums = list(map(str,input().split()))
ans = 0
if len(nums[1]) < 3:
    nums[1] = "0" * (3-len(nums[1])) + nums[1]
if len(nums[2]) < 10:
    nums[2] = "0" * (10-len(nums[2])) + nums[2]
temp = '700602' + nums[0] + nums[1] + nums[2]
for i in range(0,len(temp)-1,2):
    ans += int(temp[i]) * 1 + int(temp[i+1]) * 7
ans += int(temp[-1]) * 1
print(str(ans)[-1])