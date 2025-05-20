num1 = int(input())
check = int(input())
nums = list(map(int,input().split()))
nums = sorted(nums)
for i in range(1,num1+1):
    if i not in nums:
        print(i,end=" ",sep=" ")
