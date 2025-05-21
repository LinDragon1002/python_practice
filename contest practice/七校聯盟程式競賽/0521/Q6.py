from itertools import permutations
st = input()
ans = []
for i in permutations(st):
    ans.append(''.join(i))
ans = list(sorted(set(ans)))
print(len(ans))
for i in ans:
    print(i)