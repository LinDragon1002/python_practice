num = 14
# temp = 1
# while temp <= num:
#     if temp * temp == num:
#         print(True)
#         break
#     else:
#         temp += 1
# print(False)

left= 1
right = num
if num == 1:
    # return True
    print()
while left < right:    
    mid = (right + left) // 2 
    tot = mid * mid
    if tot == num:
        # return True
        print()
    if tot < num:
        left = mid + 1
    else:
        right = mid
        
# return False
print()