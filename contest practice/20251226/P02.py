from itertools import combinations

T = input().replace(" ", "").split(",")

num = []
for i in T:
    num.append(int(i))
l = len(num) // 2

s = sum(num)

for i in list(combinations(num, l)):
    r = sum(i)
    if r == s//2 and s - r == s//2:
        print(1)
        exit()
print(0)