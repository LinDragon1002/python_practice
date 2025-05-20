from itertools import permutations
st = input()
ans = permutations(st)
ans = list(sorted(ans,reverse=True))
ans2 = []
for i in ans:
    temp = "".join(i)
    if int(temp) != int(st):
        ans2.append(int(temp))
ans2 = sorted(set(ans2),reverse=True)
for i in ans2:
    print(i)