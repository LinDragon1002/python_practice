n, k = map(int, input().split())
x = list(map(int, input().split()))

temp = sum(x[0:k])
mx = temp
last = 0
for i in range(k, n):
    temp -= x[last]
    temp += x[i]
    last += 1
    mx = max(mx,temp)
print(mx)