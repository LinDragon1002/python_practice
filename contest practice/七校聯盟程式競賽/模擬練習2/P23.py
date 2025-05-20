num = int(input())
tot = []
for i in range(num):
    temp = list(map(int,input().split()))
    tot.append(temp)
for i in range(len(num[0])-1):
    if abs(num[0][i] - num[0][i+1]) != 1:
        print(3)
else:
    
print(tot)  