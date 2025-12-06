from typing import Counter
n = int(input())
num_list = list(map(int,input().split()))
temp = list(Counter(num_list).items())
temp = sorted(temp, key=lambda x:(-x[1],x[0]))
mx = temp[0][1]
for a,b in temp:
    if b == mx:
        print(a, end=' ')
    else:
        break