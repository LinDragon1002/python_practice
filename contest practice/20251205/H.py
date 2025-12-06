n = int(input())
for i in range(n):
    train_long = int(input())
    num_list = list(map(int,input().split()))
    ans = 0
    for j in range(train_long-1):
        for k in range(len(num_list)-1):
            temp = num_list[k]
            if num_list[k] > num_list[k+1]:
                num_list[k] = num_list[k+1]
                num_list[k+1] = temp
                ans += 1
        num_list.pop()
    print(f"Optimal train swapping takes {ans} swaps.")