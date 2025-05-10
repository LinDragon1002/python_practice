num = int(input())
ans = []
ans1 = f'{num}->'
ans.append(num)
while ans[-1] != 1:
    if ans[-1] % 2 == 0 and ans[-1] >= 4:
        ans.append(int(ans[-1]/4))
    elif ans[-1] % 2 == 0 and ans[-1] < 4:
        ans.append(int(ans[-1]/2))
    elif ans[-1] % 2 != 0:
        ans.append(ans[-1]*5+1)
    if ans[-1] == 1:
        ans1 += str(ans[-1])
    else:
        ans1 += str(ans[-1]) + '->'
print(ans1)