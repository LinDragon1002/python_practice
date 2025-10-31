from itertools import combinations
n = int(input())
nums = []
for i in range(1,n+1):
    nums.append(i)
avg = sum(nums) // 2
nums = set(nums)
for i in range(1, n-1):
    for j in list(combinations(nums,i)):
        A = set(j)
        sum_A = sum(A)
        B = nums - A
        sum_B = sum(B)
        if sum_A == sum_B:
            list_a = sorted(list(A))
            list_b = sorted(list(B))
            print(f"YES,{list_a},{list_b}")
            exit()
print("NO")