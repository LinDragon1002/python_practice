import sys
input = sys.stdin.readline

MAX = 10**6
Prime = [True] * (MAX+1)
Prime[0] = Prime[1] = False

for i in range(2,int(MAX**0.5)+1):
    if Prime[i]:
        for j in range(i * i,MAX+1, i):
            Prime[j] = False

while True:
    num = int(input())
    if num == 0:
        break
    for i in range(2,num):
        if Prime[i] and Prime[num-i]:
            print(f"{num} = {i} + {num-i}")
            break