n = 3

k = 1
count = 2

if n == 1:
    print(2)
while True:
    if n >= k:
        k += count
        count += 1
    else:
        print(count-2)
        break

# Initialize pointers to first and last possible row lengths
left, right = 1, n

while left <= right:
    # Compute the midpoint between left and right
    mid = left + (right - left) // 2
    
    # Compute the total number of coins needed for mid complete rows
    coins = (mid * (mid + 1)) // 2
    
    # If we have enough coins, look for a smaller number of rows
    if coins <= n:
        left = mid + 1
    # Otherwise, look for a larger number of rows
    else:
        right = mid - 1
        
# Return the number of complete rows (i.e., right pointer)
# return right
print()