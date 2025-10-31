tot,cho = map(int,input().split(' '))
food_full = input().split(' ')
food_r = input().split(' ')
mis_chos = []
ans = 0
for i in range(cho):
    for j in range(1,tot+1):
        mis_chos.append(int(food_full[i]) - (j - 1) * int(food_r[i]))
mis_chos = sorted(mis_chos,reverse=True)
for i in range(tot):
    if mis_chos[i] >= 0:
        ans += mis_chos[i]
print(ans)