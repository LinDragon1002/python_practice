MAX = 10**6
prime = [True] * (MAX + 1)
prime[0] = prime[1] = False

# 建質數表（篩法）
for i in range(2, int(MAX ** 0.5) + 1):
    if prime[i]:
        for j in range(i * i, MAX + 1, i):
            prime[j] = False

num = int(input())

# 找上、下最近質數
up = num + 1
down = num - 1

while up <= MAX and not prime[up]:
    up += 1

while down >= 2 and not prime[down]:
    down -= 1

# 比較距離
if down < 2:
    print(up)
else:
    if abs(up - num) < abs(num - down):
        print(up)
    elif abs(up - num) > abs(num - down):
        print(down)
    else:
        print(min(up, down))
