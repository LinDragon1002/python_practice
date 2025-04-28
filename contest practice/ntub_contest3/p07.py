num1 = int(input())
ans = []
for i in range(num1):
    temp = input().split()
    total = 0
    cnt = 0
    for i in range(len(temp)):
        if i > 0 and temp[i].isdigit():
            total += int(temp[i])
            cnt += 1
    avg = f'{total / cnt:.1f}'
    temp = [temp[0],temp[1],avg]
    ans.append(temp)

ans = list(sorted(ans,key=lambda x:int(x[0])))
for i in range(len(ans)):
    print(f'{ans[i][0]}-{ans[i][1]}:{ans[i][2]}')

ans = list(sorted(ans,key=lambda x:x[-1],reverse=True))
for i in range(len(ans)):
    print(f'{ans[i][0]}-{ans[i][1]}:{ans[i][2]}')