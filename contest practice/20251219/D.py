import sys
input = sys.stdin.readline

MAX = 10**6 + 1
Prime = [True] * (MAX+1)
Prime[0] = Prime[1] = False

for i in range(2,int(MAX**0.5)+1):
    if Prime[i]:
        for j in range(i * i,MAX+1, i):
            Prime[j] = False

def check(n):
    temp_num = str(n)
    for j in str(n):
        if not Prime[int(temp_num)]:
            return False
        temp_num = temp_num[1::] + j
    return True

circle_list = []
for i in range(100,MAX):
    if Prime[i] and check(i):
        circle_list.append(i)
while True:
    a = input().strip()
    if a == '-1':
        break
    ans = 0
    i,j = map(int,a.split())
    for c in circle_list:
        if i <= c <= j:
            ans += 1
    if ans > 1:
        print(f"{ans} Circular Primes.")
    elif ans == 1:
        print("1 Circular Prime.")
    else:
        print("No Circular Primes.")
        
