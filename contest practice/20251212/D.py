MAX = 2**15
Prime = [True] * (MAX+1)
Prime[0] = Prime[1] = False

for i in range(2,int(MAX**0.5)+1):
    if Prime[i]:
        for j in range(i * i,MAX+1, i):
            Prime[j] = False

while True:
    ans = 0
    temp = []
    n = int(input())
    if n == 0:
        break
    for k in range(2,n):
        if k not in temp and Prime[n-k] and Prime[k]:
            ans+=1
            temp.append(n-k)
    print(ans)