# import sys
# input = sys.stdin.readline

# MAX = 10**6 + 1
# Prime = [True] * (MAX)
# Prime[0] = Prime[1] = False

# for i in range(2,int(MAX**0.5)+1):
#     if Prime[i]:
#         for j in range(i * i,MAX, i):
#             Prime[j] = False

# from itertools import permutations

# def check(n):
#     temp_num = str(n)
#     for j in permutations(temp_num):
#         if not Prime[int("".join(j))]:
#             return False
#     return True

# temp_list = []
# for i in range(1,1000):
#     if check(i):
#         temp_list.append(i)

# while True:
#     n = int(input())
#     if n == 0:
#         break
#     ans = '0'
#     for i in range(n+1,MAX):
#         if i * i > MAX:
#             break
#         if i in temp_list and len(str(i)) == len(str(n)):
#             ans = i
#             break
#     print(0)

import sys
input = sys.stdin.readline

MAX = 10 ** 6 + 1

Prime = [True] * MAX
Prime[0] = False
Prime[1] = False

for j in range(2, int(MAX**0.5) + 1):
    if Prime[j]:
        for i in range(j * j, MAX, j):
            Prime[i] = False

from itertools import permutations

def check(T):
    T = str(T)
    for i in permutations(T):
        if not(Prime[int("".join(i))]):
            return False
    return True

c_list = []
for i in range(1, 1000):
    if check(i):
        c_list.append(i)

while True:
    n = int(input())
    if n == 0:
        break
    ans = "0"
    n_len = len(str(n))
    for i in range(n+1, MAX):
        if i * i > MAX:
            break
        if i in c_list and n_len == len(str(i)):
            ans = i
            break
    print(ans)