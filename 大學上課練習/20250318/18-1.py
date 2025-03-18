from itertools import permutations
def permutation(st):
    temp = []
    for i in permutations(st):
        temp.append(''.join(i))
    return len(set(temp))

print(permutation('123'))
print(permutation('113'))
print(permutation('1132'))