num = int(input())
tot = 0
tots = []
ans = []
for i in range(1,num+1):
    tot += i
    tots.append(i)
avg = tot / 2
for i in range(num,0,-1):
    if avg - i >= 0:
        ans.append(i)
        avg -= i
temp = []
for i in tots:
    if i not in ans:
        temp.append(i)
if sum(temp) == sum(ans):
    print(f'YES,{str(sorted(ans)).replace(" ", "")},{str(sorted(temp)).replace(" ", "")}')
else:
    print("NO")