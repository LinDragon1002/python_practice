n,k = map(int,input().split())
num_list = list(map(int,input().split()))
ans = 0
for i in range(n):
    if num_list[i] > 0:
        if k != 0:
            ans += 1
            k -= 1
        else:
            if num_list[i] == num_list[i-1]:
                ans += 1
            else:
                break
print(ans)