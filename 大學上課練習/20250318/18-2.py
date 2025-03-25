from itertools import permutations
def permutation(st):
    temp = []
    for i in permutations(st):
        if int("".join(i)) % 3 == 0 or int("".join(i)) % 7 == 0:
            temp.append(''.join(i))
    return len(set(temp))

print(permutation('11435'))
print(permutation('114356'))