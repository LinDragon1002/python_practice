num = [int(i) for i in input().split(',')]
tot = sum(num)
avg = tot // 2
num = sorted(num,reverse=True)
ans = []
for i in range(len(num)):
    if avg - num[i] > 0:
        ans.append(num[i])
        avg -= num[i]
if sum(ans) == sum(num) - sum(ans) and len(ans) == len(num) - len(ans):
    print(1)
else:
    print(0)