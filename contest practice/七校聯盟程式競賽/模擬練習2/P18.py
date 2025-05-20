num = int(input())
nums = list(map(int,input().split()))
tot = []
for i in range(1,max(nums)+1):
    temp = []
    for j in range(len(nums)):
        temp.append(abs(nums[j] - i))
    tot.append(sum(temp))
print(min(tot))