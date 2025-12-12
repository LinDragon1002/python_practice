MAX = 10**6
Prime = [True] * (MAX+1)
Prime[0] = Prime[1] = False

for i in range(2,int(MAX**0.5)+1):
    if Prime[i]:
        for j in range(i * i,MAX+1, i):
            Prime[j] = False
    
n = int(input())
temp1 = 0
temp2 = n+1
for i in range(2,n):
    if Prime[i]:
        temp1 = max(temp1,i)
while True:
    if Prime[temp2]:
        break
    temp2 += 1
print(temp1,temp2)