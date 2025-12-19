import sys
input = sys.stdin.readline

MAX = 10**6
Prime = [True] * (MAX+1)
Prime[0] = Prime[1] = False

for i in range(2,int(MAX**0.5)+1):
    if Prime[i]:
        for j in range(i * i,MAX+1, i):
            Prime[j] = False

for i in range(int(input())):
    num = int(input())
    if Prime[num] and num != int(str(num)[::-1]) and Prime[int(str(num)[::-1])]:
        print(f"{num} is an emirp number.")
    elif Prime[num]:
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
    