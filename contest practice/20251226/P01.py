from itertools import permutations

st = input()
temp = sorted(set(permutations(st)),reverse=True)

for i in temp:
    if int("".join(i)) != int(st):
        print(int("".join(i)))