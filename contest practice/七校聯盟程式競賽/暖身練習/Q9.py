MAX = 10 ** 6
prime = [True] * (MAX + 1)
prime[0] = prime[1] = False
for i in range(2, int(MAX**0.5)+1):
    if prime[i]:
        for j in range(i * i, MAX + 1, i):
            prime[j] = False
while True:
    ans = []
    num = input()
    if int(num) == 0:
        break
    for i in range(len(num)):
        for j in range(len(num)):
            temp = num[i:j+1]
            if 0 < len(temp) <= 6 and prime[int(temp)]:
                ans.append(int(temp))
    ans = sorted(ans,reverse=True)
    print(ans[0])
