nums = [9,4,1,7]
k = 2
# min_nums = []
# for i in range(len(nums)):
#     print(i)

def subtract(numbers):
    if not numbers:
        return 0
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

window_subtract = abs(subtract(nums[:k]))
min_subtract = window_subtract

for i in range(len(nums) - k):
    window_subtract = abs(window_subtract - nums[i] + nums[i+k])
    min_subtract = min(min_subtract, window_subtract)
print(min_subtract)