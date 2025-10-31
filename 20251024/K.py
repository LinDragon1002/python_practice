tot,cho = map(int,input().split(' '))
food_full = input().split(' ')
food_r = input().split(' ')
ans = 0
for i in range(tot):
    for j in range(cho):
        ans += int(food_full[j]) - (i - 1) * int(food_r[j])
print(ans)