n = int(input())
for i in range(n):
    n,a,b = map(int,input().split())
    temp = min(n // 2 * b + n % 2 * a, n * a)
    print(temp)